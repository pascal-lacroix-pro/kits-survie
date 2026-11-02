---
titre: SOLUTIONS
cours: apps-statiques
atelier: 99
atelier_titre: MEMENTOS
ordre: 5
---

# SOLUTIONS

---

## AT-3.4.02

### Défi 1

---

### Défi 2

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>

        :root {
            --colorPrimary  : #007BFF;
            --colorSecondary: #6C757D;
            --colorSuccess  : #28A745;
            --font: Arial, sans-serif;
        }

        * {
            box-sizing: border-box;
        }

        body {
            font-family: var(--font);
        }

        .badge {
            /* BOX */
            display: inline-block;
            padding: .3em;
            border-radius: .3em;;

            /* FONT */
            color: #fff;
        }

        .badge.badge-primary {
            background: var(--colorPrimary);
        }
        .badge.badge-secondary {
            background: var(--colorSecondary);
        }
        .badge.badge-success {
            background: var(--colorSuccess);
        }





    </style>
</head>
<body>
    <h1>Example heading <span class="badge badge-primary">New</span></h1>
    <h2>Example heading <span class="badge badge-secondary">New</span></h2>
    <h3>Example heading <span class="badge badge-success">New</span></h3>
</body>
</html>
```

---

```css
/* DÉFI 6 */
* {
box-sizing: border-box;
}

.card-user {
  /* BOX */
  width: 600px;
  padding: 1em 1em 1em 132px;
  background: 1em center / 90px url('images/user3.png') no-repeat,
              linear-gradient(90deg, red, orange);
  box-shadow: rgba(0,0,0,.5) 0 0 15px;

  /* FONT */
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
  color: #fff;
  font-size: 1.2em;
}

.card-user h1 {
  /* FONT */
  font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
```

---

## AT-3.4.03

### Défi 1

```html
<!-- DÉFI 1 -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>

        * {
            box-sizing: border-box;
        }

        .card-user {
            /* BOX */
            width: 100%;
            max-width: 600px;
            padding: 2em 2em 2em calc(3em + 70px);
            background:  1em center / 90px url('images/user3.png') no-repeat,
                         linear-gradient(90deg, red, orange);
                         box-shadow: rgba(0,0,0,.5) 0 0 15px;

            /* FONT */
            font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
            color: #fff;
            font-size: 1.2em;
            margin: 2em auto;
            border-radius: 1em;
        }

        .card-user--title {
            /* BOX */
            margin: 0;
        }

        .card-user--cta {
            /* BOX */
            display: inline-block;
            padding: .5em;
            background: rgba(255,255,255, .3);
            color: rgba(255,255,255, .7);
            border-radius: .5em;

            /* FONT */
            font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            text-decoration: none;
        }
       
        .card-user--cta:hover {
          background: rgba(255,255,255, .7);
          color: #fff;
        }





    </style>
</head>
<body>
    <div class="card-user">
        <h1 class="card-user--title">John Doe</h1>
        <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aut quas dignissimos, explicabo laboriosam ullam pariatur ea fugiat.</p>
        <div><a href="#" class="card-user--cta">Contact me</a></div>
    </div>
</body>
</html>
```

---

### Défi 2

```html
<!-- DÉFI 2 -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>

        * {
            box-sizing: border-box;
        }

        .card-user {
            /* BOX */
            width: 100%;
            max-width: 300px;
            padding: calc(70px + 3em) 2em 2em 2em;
            background:  2em 2em / 70px url('images/user3.png') no-repeat,
                         linear-gradient(90deg, red, orange);
                         box-shadow: rgba(0,0,0,.5) 0 0 15px;

            /* FONT */
            font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
            color: #fff;
            font-size: 1.2em;
            margin: 2em auto;
            border-radius: 1em;
        }

        .card-user--title {
            /* BOX */
            margin: 0;
        }

        .card-user--cta {
            /* BOX */
            display: inline-block;
            padding: .5em;
            background: rgba(255,255,255, .3);
            color: #fff;
            border-radius: .5em;

            /* FONT */
            font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            text-decoration: none;
        }





    </style>
</head>
<body>
    <div class="card-user">
        <h1 class="card-user--title">John Doe</h1>
        <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aut quas dignissimos, explicabo laboriosam ullam pariatur ea fugiat.</p>
        <div><a href="#" class="card-user--cta">Contact me</a></div>
    </div>
</body>
</html>
```

---

### Défi 3

```html
<!-- DÉFI 3 -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>

        * {
            box-sizing: border-box;
        }

        .card-user {
            /* BOX */
            width: 100%;
            max-width: 300px;
            padding: calc(3em + 70px) 0 0 0;
            background:  2em 2em / 70px url('images/user3.png') no-repeat,
                         linear-gradient(90deg, red, orange);
                         box-shadow: rgba(0,0,0,.5) 0 0 15px;

            /* FONT */
            font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
            color: #fff;
            font-size: 1.2em;
            margin: 2em auto;
            border-radius: 1em;
        }

        .card-user--title {
            /* BOX */
            margin: 0;
            padding: 0 1em 1em 1em;
        }

        .card-user--content {
            /* BOX */
            background: #fff;
            color: #666;
            padding: 2em;
            border-radius: 0 0 1em 1em;
        }

        .card-user--cta {
            /* BOX */
            display: inline-block;
            padding: .5em;
            background-color:lightsteelblue ;
            color: #fff;
            border-radius: .5em;

            /* FONT */
            font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            text-decoration: none;
        }
        .card-user--cta:hover {
            background: steelblue;
            color: #fff;
        }


    </style>
</head>
<body>
    <div class="card-user">
        <h1 class="card-user--title">John Doe</h1>
        <div class="card-user--content">
            <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aut quas dignissimos, explicabo laboriosam ullam pariatur ea fugiat.</p>
            <div><a href="#" class="card-user--cta">Contact me</a></div>
        </div>
    </div>
</body>
</html>
```

---

### Défi 4

```html
<!-- DÉFI 4 -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>

        * {
            box-sizing: border-box;
        }

        .card {
            /* BOX */
            width: 100%;
            max-width: 300px;
            height: 478px;
            overflow: hidden;
            margin: 2em auto;
            background:  top left / cover url('images/montagnes.jpg') no-repeat, black;
            box-shadow: rgba(0,0,0,.5) 0 0 15px;

            /* FONT */
            font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
            color: #ffffff;
            font-size: 1.2em;
            text-align: center;
        }

        .card .card-content {
            /* BOX */
            width: 100%;
            height: 100%;
            margin-top: 380px;
            padding: 0 2em;
        }

        .card:hover .card-content {
            /* BOX */
            margin-top: 0;
            padding: 6em 2em;
            background: rgba(0,0,0,.3);
        }

        .card-title {
            font-size: 1.5em;
            margin: 0 0 3em 0;
        }

        .card:hover .card-title {
            margin: 0 0 1em 0;
        }



        .cta {
            /* BOX */
            display: inline-block;
            padding: .5em;
            background: #444 ;
            color: #fff;

            /* FONT */
            font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            font-size: .8em;
            text-decoration: none;
            text-transform: uppercase;
        }
        .cta:hover {
            background: #000;
            color: #fff;
        }


    </style>
</head>
<body>
    <div class="card">
        <div class="card-content">
            <h1 class="card-title">Mountain View</h1>
            <p>Check out all of these gorgeous mountain trips with beautiful views of, you guessed it, the mountains</p>
            <div><a href="#" class="cta">View Trips</a></div>
        </div>
    </div>
</body>
</html>
```

---

### Défi 5

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
	:root {
	    --couleur1: #FA8172;
	}

        * {
            box-sizing: border-box;
        }

        body {
            background: var(--couleur1);
        }

        .card {
            /* BOX */
            width: 100%;
            max-width: 300px;
            margin: 2em auto;
            background: #fff;
            padding: 1em;
            border-radius: .5em;
            box-shadow: rgba(0,0,0,.5) 0 0 15px;

            /* FONT */
            font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            color: #999;
            font-size: 1.1em;
        }

        .card-title {
            /* BOX */
            margin: 0 0 .5em 0;
            border-bottom: 3px solid var(--couleur1);

            /* FONT */
            color: #333;
        }



        .cta {
            /* BOX */
            display: inline-block;
            padding: 1em;
            background: var(--couleur1);

            /* FONT */
            font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            color: #fff;
            text-decoration: none;
            text-transform: uppercase;
        }

        .cta:hover {
            background: #000;
            color: #fff;
        }


    </style>
</head>
<body>
    <div class="card">
        <h1 class="card-title">Card Title</h1>
        <div class="card-content">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. </p>
            <div><a href="#" class="cta">Next</a></div>
        </div>
    </div>
</body>
</html>
```

---

### Défi 6

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            background: #333;
        }

        .card {
            /* BOX */
            width: 100%;
            max-width: 350px;
            margin: 2em auto;
            background: linear-gradient(135deg, #FFEC62, #F322D6);
            padding: 2em 3em;
            border-radius: .3em;
            box-shadow: rgba(0,0,0,.5) 0 0 15px;

            /* FONT */
            font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            color: #fff;
            font-size: 1.1em;
            text-align: center;
        }

        .icon {
            display: inline-block;
            width: 70px;
            height: 70px;
        }

        .icon-plane {
            background: 0 0 / cover url('images/plane.png') no-repeat;
        }

        .card-title {
            /* BOX */
            margin: .2em 0 1em 0;

            /* FONT */
            text-transform: uppercase;
        }

        .card-content ul {
            padding: 0;
        }

        .card-content li {
            list-style: none;
            padding: 1em;
        }

        .card-content li:not(:last-of-type) {
            border-bottom: #fff 1px solid;
        }

        .cta {
            /* BOX */
            display: inline-block;
            padding: 1em;
            background: #fff;
            border-radius: .3em;

            /* FONT */
            font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            color: #999;
            text-decoration: none;
            text-transform: uppercase;
        }

        .cta:hover {
            background: #333;
            color: #fff;
        }


    </style>
</head>
<body>
    <div class="card">
        <header class="card-header">
            <i class="icon icon-plane"></i>
            <h1 class="card-title">Plus</h1>
        </header>
        <div class="card-content">
            <ul>
                <li>Includes Basic Features</li>
                <li>Unlimited Websites</li>
                <li>Unlimited SSD Storage</li>
                <li>Unlimited Domains</li>
                <li>Unlimited Parked Domains</li>
                <li>Unlimited Sub Domains</li>
            </div>
            <div><a href="#" class="cta">Get Started</a></div>
        </div>
    </div>
</body>
</html>
```

---

## AT-3.4.04

### Défi 3

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
    <style>
        :root {
            --color1a: #28223F;
            --color1b: #231E39;
            --color1c: #1F1A36;
            --color1d: #2D2747;
            --color2 : #03BFCB;
            --color3 : #B3B8CD;
            --color4 : #FEBB0B;
            --font   : 'Montserrat', sans-serif;
        }

        * {
            box-sizing: border-box;
        }

        body {
            background : var(--color1a);
            font-family: var(--font);
            color: var(--color3);
            font-size: .9em;
        }

        /* CARD -------------------- */
            .card-user {
                /* BOX */
                width: 100%;
                max-width: 350px;
                margin: 2em auto;
                background: var(--color1b);
                border-radius: 5px;
                box-shadow: var(--color1b) 0 0 15px;
            }

            .card-user.user-pro::before {
                content: 'PRO';
                /* BOX */
                display: inline-block;
                background: var(--color4);
                padding: .2em .4em;
                border-radius: 3px;
                margin: 1em;

                /* FONT */
                text-align: left;;
                color: var(--color1a);
                font-size: .9em;
            }

        /* CARD-HEADER -------------------- */
            .card-header {
                font-size: .7em;
                text-align: center;
            }

            .card-header figure {
                margin: 0;
            }

            .card-header figcaption {
                display: none;
            }

            .card-header img {
                border-radius: 50%;
                border: var(--color2) 2px solid;
                padding: .5em;
                margin-bottom: .5em;
            }

            .card-header h1, h2 {
                margin: .4em;
            }

            .card-header h2 {
                font-size: 1em;
                text-transform: uppercase;
                font-weight: lighter;
            }

        /* CARD-CONTENT -------------------- */
            .card-content div {
                margin: 2em 3em;
                text-align: center;
            }

            .cta {
                /* BOX */
                display: inline-block;
                padding: .8em 2em;
                border-radius: 3px;
                border: var(--color2) 1px solid;

                /* FONT */
                color: var(--color2);
                text-decoration: none;
            }

            .cta.cta-primary, .cta:hover {
                background: var(--color2);
                color: var(--color1b);
            }

        /* CARD-FOOTER -------------------- */
            .card-footer {
                /* BOX */
                background: var(--color1c);
                border-radius: 0 0 1em 1em;
                padding: 2em;

                /* FONT */
                font-size: .8em;
            }
            .card-footer h3 {
                /* BOX */
                margin: 0 0 1em 0;

                /* FONT */
                font-size: .9em;
                text-transform: uppercase;
            }
            .card-footer .tag {
                display: inline-block;
                border: var(--color1d) 1px solid;
                padding: .5em;
                margin: .4em .2em;

                /* FONT */
                color: var(--color3);
                text-decoration: none;
            }

    </style>
</head>
<body>
    <div class="card-user user-pro">
        <header class="card-header">
            <figure>
                <img src="images/ricky.jpg" alt="Ricky Park - New York">
                <figcaption>Ricky Park - User Interface Designer and Front-End Developer - New York</figcaption>
            </figure>
            <h1 class="card-title">Ricky Park</h1>
            <h2>New York</h2>
        </header>
        <div class="card-content">
            <div>User Interface Designer and Front-End Developer</div>
            <div>
                <a href="#" class="cta cta-primary">Message</a>
                <a href="#" class="cta cta-secondary">Following</a>
            </div>
        </div>
        <footer class="card-footer">
            <h3>Skills</h3>
            <a href="#" class="tag">UI/UX</a>
            <a href="#" class="tag">Front-End Development</a>
            <a href="#" class="tag">HTML</a>
            <a href="#" class="tag">CSS</a>
            <a href="#" class="tag">JavaScript</a>
            <a href="#" class="tag">React</a>
            <a href="#" class="tag">Node</a>
        </footer>
    </div>
</body>
</html>
```

---

### Défi 4

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --color1: #333;
            --color2: #02456B;
            --font  : 'Roboto', sans-serif;
        }

        * {
            box-sizing: border-box;
        }

        body {
            background: var(--color1);
            font-family: var(--font);
            color: var(--color1);
            font-size: 1em;
        }

        /* CARD -------------------- */
            .card {
                /* BOX */
                width: 100%;
                max-width: 600px;
                margin: 2em auto;
                padding: 1em;
                background: 0 0 / cover url('images/waves.png') no-repeat;
                box-shadow: #000 0 0 15px;
            }

            .card-content {
                background: #fff;
                width: 50%;
                padding: 1em;
            }

            .card-content .card-title {
                text-transform: uppercase;
                font-size: 3em;
                text-align: center;
                font-weight: bolder;
                color: var(--color2);
            }



    </style>
</head>
<body>
    <div class="card">
        <div class="card-content">
            <h1 class="card-title">Enjoy Every Moment</h1>
            <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Earum iure cupiditate suscipit recusandae inventore amet dolores, aliquid eos sapiente dolor repellat odit rerum, itaque qui sit explicabo accusamus ipsam quae!</p>
        </div>
    </div>
</body>
</html>
```
