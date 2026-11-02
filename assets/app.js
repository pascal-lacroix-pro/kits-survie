(() => {
  'use strict';
  const $ = (sel, racine = document) => racine.querySelector(sel);
  const menu = $('#menu'), contenu = $('#contenu'), champ = $('#recherche');
  const btnMenu = $('#btn-menu'), statut = $('#statut');
  const mouvementReduit = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let notes = [], textes = null, noteCourante = null, observateurVideo = null, minuteur;

  const esc = s => s.replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const norm = s => s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const idDe = chemin => chemin.replace(/\.md$/, '');
  const lien = n => '#' + idDe(n.chemin);

  /* ---------- Démarrage ---------- */
  async function demarrer() {
    let index;
    try {
      const r = await fetch('notes/index.json');
      if (!r.ok) throw new Error(r.status);
      index = await r.json();
    } catch (e) {
      menu.innerHTML = '';
      return erreur("Impossible de charger le sommaire. Si tu ouvres le fichier directement, passe par un serveur web (par exemple « python3 -m http.server »).");
    }
    notes = index.cours.flatMap(c => c.ateliers.flatMap(a => a.notes));
    construireMenu(index);
    route();
  }

  function construireMenu(index) {
    menu.innerHTML = index.cours.map(c => `
      <section aria-labelledby="c-${esc(c.id)}">
        <h2 class="cours" id="c-${esc(c.id)}">${esc(c.titre)}</h2>
        ${c.ateliers.map(a => `
          <details>
            <summary>${a.numero < 99 ? `<span class="num">${a.numero}</span>` : ''}<span>${esc(a.titre)}</span></summary>
            <ul>${a.notes.map(n => `<li><a href="${lien(n)}" data-chemin="${esc(n.chemin)}">${esc(n.titre)}</a></li>`).join('')}</ul>
          </details>`).join('')}
      </section>`).join('');
  }

  /* ---------- Routage : #dossier/atelier/note ---------- */
  function route() {
    const id = decodeURIComponent(location.hash.slice(1));
    if (!id) return accueil();
    const note = notes.find(n => idDe(n.chemin) === id);
    note ? afficher(note) : erreur(`Cette note n'existe pas : ${id}`);
  }

  function marquerMenu(note) {
    menu.querySelectorAll('[aria-current]').forEach(a => a.removeAttribute('aria-current'));
    if (!note) return;
    const a = menu.querySelector(`a[data-chemin="${CSS.escape(note.chemin)}"]`);
    if (!a) return;
    a.setAttribute('aria-current', 'page');
    a.closest('details').open = true;
    a.scrollIntoView({ block: 'nearest' });
  }

  function accueil() {
    noteCourante = null;
    marquerMenu(null);
    document.title = 'Kits de survie';
    contenu.innerHTML = `
      <article class="note">
        <h1>Kits de survie</h1>
        <p>Les notes de cours, à lire à ton rythme. Choisis un atelier dans le sommaire, ou tape un mot dans la barre de recherche.</p>
        <p><a class="bouton" href="${lien(notes[0])}">Commencer par la première note</a></p>
      </article>`;
    debut();
  }

  function erreur(message) {
    noteCourante = null;
    contenu.innerHTML = `
      <article class="note">
        <h1>Impossible d'afficher cette page</h1>
        <p class="erreur" role="alert">${esc(message)}</p>
        <p><a href="#">Retour à l'accueil</a></p>
      </article>`;
  }

  function debut() {
    window.scrollTo(0, 0);
    contenu.focus({ preventScroll: true });
  }

  /* ---------- Affichage d'une note ---------- */
  async function afficher(note) {
    noteCourante = note;
    marquerMenu(note);
    let md;
    try {
      const r = await fetch('notes/' + note.chemin);
      if (!r.ok) throw new Error(r.status);
      md = await r.text();
    } catch (e) {
      return erreur(`Impossible de charger « ${note.titre} ». Vérifie ta connexion puis recharge la page.`);
    }
    if (noteCourante !== note) return; // on a déjà changé de note
    const corps = md.replace(/^---\n[\s\S]*?\n---\n/, '');
    const base = new URL('notes/' + note.chemin.split('/').slice(0, -1).join('/') + '/', location.href);
    contenu.innerHTML = `<article class="note">${marked.parse(corps)}</article>${pager(note)}`;
    const article = $('.note', contenu);
    corrigerRessources(article, base);
    colorerCode(article);
    gererVideos(article);
    document.title = `${note.titre} – Kits de survie`;
    debut();
  }

  function pager(note) {
    const i = notes.indexOf(note);
    const bloc = (n, cls, etiquette) => n ? `<a class="${cls}" href="${lien(n)}"><span>${etiquette}</span>${esc(n.titre)}</a>` : '';
    return `<nav class="pager" aria-label="Notes voisines">${bloc(notes[i - 1], 'prec', 'Note précédente')}${bloc(notes[i + 1], 'suiv', 'Note suivante')}</nav>`;
  }

  function corrigerRessources(racine, base) {
    racine.querySelectorAll('[src],[href]').forEach(el => {
      const attr = el.hasAttribute('src') ? 'src' : 'href';
      const v = el.getAttribute(attr);
      if (/^(https?:|mailto:|data:|#|\/)/i.test(v)) {
        if (attr === 'href' && /^https?:/i.test(v)) { el.target = '_blank'; el.rel = 'noopener'; }
        return;
      }
      el.setAttribute(attr, new URL(v, base).href);
    });
    racine.querySelectorAll('img').forEach(i => { i.loading = 'lazy'; i.decoding = 'async'; });
  }

  function colorerCode(racine) {
    racine.querySelectorAll('pre').forEach(pre => {
      const code = $('code', pre);
      if (code && /language-/.test(code.className)) hljs.highlightElement(code);
      const enveloppe = document.createElement('div');
      enveloppe.className = 'bloc-code';
      pre.replaceWith(enveloppe);
      const bouton = document.createElement('button');
      bouton.type = 'button';
      bouton.className = 'copier';
      bouton.textContent = 'Copier';
      bouton.setAttribute('aria-label', 'Copier ce code');
      bouton.addEventListener('click', async () => {
        try {
          await navigator.clipboard.writeText((code || pre).innerText);
          bouton.textContent = 'Copié';
          statut.textContent = 'Code copié';
        } catch (e) {
          bouton.textContent = 'Échec';
        }
        setTimeout(() => { bouton.textContent = 'Copier'; statut.textContent = ''; }, 1800);
      });
      enveloppe.append(pre, bouton);
    });
  }

  /* Les animations ne tournent que lorsqu'elles sont visibles, et jamais si l'utilisateur a demandé moins de mouvement. */
  function gererVideos(racine) {
    if (observateurVideo) observateurVideo.disconnect();
    const videos = racine.querySelectorAll('video');
    if (!videos.length) return;
    observateurVideo = new IntersectionObserver(entrees => entrees.forEach(e => {
      if (mouvementReduit) return;
      e.isIntersecting ? e.target.play().catch(() => {}) : e.target.pause();
    }), { threshold: 0.4 });
    videos.forEach(v => {
      v.removeAttribute('autoplay');
      v.preload = 'metadata';
      v.muted = true;
      observateurVideo.observe(v);
    });
  }

  /* ---------- Recherche ---------- */
  async function chargerTextes() {
    if (textes) return textes;
    const r = await fetch('notes/search.json');
    if (!r.ok) throw new Error(r.status);
    textes = (await r.json()).map(t => ({ ...t, n: norm(`${t.t} ${t.a} ${t.x}`), nt: norm(t.t), nx: norm(t.x) }));
    return textes;
  }

  function extrait(t, mots) {
    const positions = mots.map(m => [t.nx.indexOf(m), m]).filter(([i]) => i >= 0).sort((a, b) => a[0] - b[0]);
    if (!positions.length) return '';
    const [i, m] = positions[0];
    const d = Math.max(0, i - 60), f = Math.min(t.x.length, i + m.length + 120);
    return (d ? '…' : '') + esc(t.x.slice(d, i)) + '<mark>' + esc(t.x.slice(i, i + m.length)) + '</mark>'
      + esc(t.x.slice(i + m.length, f)) + (f < t.x.length ? '…' : '');
  }

  async function chercher() {
    const q = champ.value.trim();
    if (q.length < 2) { statut.textContent = ''; return route(); }
    let base;
    try { base = await chargerTextes(); } catch (e) { return erreur('La recherche est indisponible pour le moment.'); }
    const mots = norm(q).split(/\s+/).filter(Boolean);
    const trouves = base
      .filter(t => mots.every(m => t.n.includes(m)))
      .map(t => ({ t, score: mots.reduce((s, m) => s + (t.nt.includes(m) ? 10 : 0) + t.n.split(m).length - 1, 0) }))
      .sort((a, b) => b.score - a.score)
      .slice(0, 30);
    const titre = trouves.length
      ? `${trouves.length} note${trouves.length > 1 ? 's' : ''} pour « ${esc(q)} »`
      : `Aucune note ne contient « ${esc(q)} »`;
    noteCourante = null;
    document.title = `Recherche – Kits de survie`;
    contenu.innerHTML = `
      <section class="note">
        <h1>${titre}</h1>
        ${trouves.length ? '' : '<p>Essaie avec un seul mot, ou avec le début d\'un mot.</p>'}
        <ol class="resultats">${trouves.map(({ t }) => {
          const n = notes.find(x => x.chemin === t.c);
          return `<li><a class="resultat" href="${lien(n)}"><span class="r-titre">${esc(t.t)}</span><span class="r-at">${esc(t.a)}</span><span class="r-ext">${extrait(t, mots)}</span></a></li>`;
        }).join('')}</ol>
      </section>`;
    statut.textContent = titre.replace(/&[a-z#0-9]+;/g, '');
  }

  champ.addEventListener('focus', () => chargerTextes().catch(() => {}));
  champ.addEventListener('input', () => { clearTimeout(minuteur); minuteur = setTimeout(chercher, 150); });
  champ.addEventListener('keydown', e => { if (e.key === 'Escape') { champ.value = ''; chercher(); } });
  $('#form-recherche').addEventListener('submit', e => e.preventDefault());
  contenu.addEventListener('click', e => {
    const a = e.target.closest('a.resultat');
    if (!a) return;
    champ.value = '';
    if (a.hash === location.hash) { e.preventDefault(); route(); }
  });

  /* ---------- Sommaire sur mobile ---------- */
  function basculer(ouvert = !document.body.classList.contains('menu-ouvert')) {
    document.body.classList.toggle('menu-ouvert', ouvert);
    btnMenu.setAttribute('aria-expanded', String(ouvert));
    if (ouvert) menu.focus();
  }
  btnMenu.addEventListener('click', () => basculer());
  menu.addEventListener('click', e => { if (e.target.closest('a')) basculer(false); });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && document.body.classList.contains('menu-ouvert')) { basculer(false); btnMenu.focus(); }
  });

  $('#saut').addEventListener('click', e => { e.preventDefault(); contenu.focus(); });
  window.addEventListener('hashchange', () => { champ.value = ''; route(); });
  demarrer();
})();
