# blackboxai-technical-tests-answers

This repository is for answers to the basic questions for Microverse Developer Agency for blackbox.io project.

# 1. SIMPLE LOGIN PAGE

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Simple Login Page</title>
    <link rel="stylesheet" href="css/styles.css" />
  </head>
  <body>
    <section class="container">
      <div id="login-error-msg-holder">
        <p id="login-error-msg">
          Invalid username
          <span id="error-msg-second-line">and/or password</span>
        </p>
      </div>
      <form id="login-form" class="login-form" action="#">
        <header class="form-header">
          <h3>Login Form</h3>
        </header>
        <!--Email Input-->
        <div class="field email-field">
          <div class="form-group input-field">
            <input
              name="email"
              type="email"
              class="form-input email"
              placeholder="Enter your email"
            />
          </div>
        </div>
        <!--Password Input-->
        <div class="create-password">
          <div class="form-group input-field">
            <input
              name="password"
              type="password"
              class="form-input password"
              placeholder="password"
            />
          </div>
        </div>
        <!--Login Button-->
        <div class="form-group">
          <input
            id="login-form-submit"
            class="form-button"
            type="submit"
            value="Login"
          />
        </div>
        <div class="form-footer">
          Don't have an account? <a href="#">Sign Up</a>
        </div>
      </form>
    </section>

    <!-- JavaScript -->
    <script src="js/script.js"></script>
  </body>
</html>
```

> ![screenshot](login.png)

# 2. WEB SCRAPING WITH PYTHON

```py

# Scrape a document.

from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="asset/css/style.css" />
    <title>start up</title>
  </head>
  <body>
    <nav class="navbar">
      <ul class="nav-menu">
        <li><a class="nav-item" href="http://example.com/cloud_one" id="link1">
         Home</a></li>
        <li><a class="nav-item" href="http://example.com/cloud_two" id="link2">
         About us</a></li>
        <li><a class="nav-item" href="http://example.com/cloud_three" id="link3">
         Contact Us</a></li>
      </ul>
    </nav>
    <header class="header">
      <h1>Welcome to our start-up company</h1>
      <p class ="motto">We are here to serve you better, try us today...</p>
    </header>
    <section>
      <h2>What We Do</h2>
      <img src="https://images.unsplash.com/photo-1682965636983-29148abdb86d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=600&q=60" alt="what we do"/>

      <span>Advertising</span>
      <span>Training</span>
      <span>Workshop</span>
    </section>
    <article>
      <p class="art">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur
        voluptatibus vel laborum sunt odit quae ducimus nam veniam, soluta nisi.
      </p>
    </article>
    <article>
      <p class="art">
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Iure
        laudantium voluptatum atque a, magni delectus ad velit dolorum assumenda
        ipsum dolor excepturi vero quis explicabo. Temporibus suscipit debitis
        aliquid animi!
      </p>
    </article>
    <article>
      <p class="art">
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Iure
        laudantium voluptatum atque a, magni delectus ad velit dolorum assumenda
        ipsum dolor excepturi vero quis explicabo. Temporibus suscipit debitis
        aliquid animi!
      </p>
    </article>
  </body>
</html>
"""


# Scrape a local variable
soup = BeautifulSoup(html_doc, "html.parser")

# print(soup.prettify())
# print(soup.head.prettify())
# print(soup.head.title.prettify())
print(soup.head.title.get_text())


print(soup.title.parent.name)

# Get first span element
element = soup.find("span")
print(element)

# Second span element
second_span = soup.find_all("span")[1]
print(second_span)

# get all span elements
all_span = soup.find_all("span")
print(all_span)

# get class name of the first p tag
print(soup.p)
print(soup.p["class"])

# extract the url
urls = soup.find_all("a")

for link in urls:
    print(link.get("href"))

# Scrape Website

from csv import writer

import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find("body").find_all("a")

with open("links.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    headers = ["========urls========"]
    csv_writer.writerow(headers)

    for link in links:
        # print(link.get("href"))
        uri = link.get("href")
        csv_writer.writerow([uri])


```

# 2. WEB SCRAPING WITH NODEJS

```js
const axios = require('axios');
const cheerio = require('cheerio');
const j2csv = require('json2csv').Parser;
const fs = require('fs');

const music =
  'https://books.toscrape.com/catalogue/category/books/music_14/index.html';

const baseUrl = 'https://books.toscrape.com/catalogue/category/books/music_14/';
const booksData = [];

async function getBooks(url) {
  try {
    const response = await axios.get(url);
    const $ = cheerio.load(response.data);

    const books = $('article');
    books.each(function () {
      title = $(this).find('h3 a').text();
      price = $(this).find('.price_color').text();
      stock = $(this).find('.availability').text().trim();
      booksData.push({ title, price, stock });
    });

    // Handle pagination
    if ($('.next a').length > 0) {
      nextPage = baseUrl + $('.next a').attr('href');
      getBooks(nextPage);
    } else {
      const parser = new j2csv();
      const csv = parser.parse(booksData);
      fs.writeFileSync('./books.csv', csv);
    }

    console.log(booksData);
  } catch (error) {
    console.error(error);
  }
}

getBooks(music);
```

# 4. HOW TO CREATE A NAVIGATION BAR AND LOGIN

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Navigation bar and login</title>
    <link rel="stylesheet" href="css/styles.css" />
  </head>
  <body>
    <!-- Header -->
    <header>
      <nav class="nav">
        <a href="#" class="nav_logo">IO</a>
        <ul class="nav_items">
          <li class="nav_item">
            <a href="#" class="nav_link">Home</a>
            <a href="#" class="nav_link">Product</a>
            <a href="#" class="nav_link">Services</a>
            <a href="#" class="nav_link">Contact</a>
          </li>
        </ul>
        <button class="button" id="form-open">Login</button>
      </nav>
    </header>
    <main>
      <form
        id="login_form"
        class="form_class"
        action="login/login-access.php"
        method="post"
      >
        <div class="form_div">
          <label>Email:</label>
          <input
            class="field_class"
            name="login_txt"
            type="email"
            placeholder="Enter your email"
            autofocus
            required
          />
          <label>Password:</label>
          <input
            id="pass"
            class="field_class"
            name="password_txt"
            type="password"
            placeholder="Enter password"
          />
          <button class="submit_class" type="submit" form="login_form">
            Login
          </button>
        </div>
        <div class="info_div">
          <p>
            Not registered yet?
            <a href="#">Sign up here</a>
          </p>
        </div>
      </form>
    </main>
  </body>
</html>
```

# 5. BOOTSTRAP FOOTER

```html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- Bootstrap 5 CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>

    <title>How to create a footer page with bootstrap</title>
  </head>
  <body>

    <div class="container fixed-buttom">
      <footer class="py-5">
        <div class="row">
          <div class="col-2">
            <h5>Quick links1</h5>
            <ul class="nav flex-column">
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">Home</a>
              </li>
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">About</a>
              </li>
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">Contact</a>
              </li>
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">Get started</a>
              </li>
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">About</a>
              </li>
            </ul>
          </div>

          <div class="col-2">
            <h5>Quick links2</h5>
            <ul class="nav flex-column">
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">Home</a>
              </li>
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">About</a>
              </li>
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">Contact</a>
              </li>
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">Get started</a>
              </li>
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">About</a>
              </li>
            </ul>
          </div>

          <div class="col-2">
            <h5>Quick links3</h5>
            <ul class="nav flex-column">
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">Home</a>
              </li>
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">About</a>
              </li>
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">Contact</a>
              </li>
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">Get started</a>
              </li>
              <li class="nav-item mb-2">
                <a href="#" class="nav-link p-0 text-muted">About</a>
              </li>
            </ul>
          </div>

          <div class="col-4 offset-1">
            <form>
              <h5>Newsletter</h5>
              <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum doloribus illo autem consequatur inventore .</p>
              <div class="d-flex w-100 gap-2">
                <label for="newsletter1" class="visually-hidden"
                  >Email address</label
                >
                <input
                  id="newsletter1"
                  type="text"
                  class="form-control"
                  placeholder="Email address"
                />
                <button class="btn btn-secondary" type="button">Subscribe</button>
              </div>
            </form>
          </div>
          </footer>
        </div>

  </body>
</html>

```

# 6. CREATE ZIP FILE USING NODEJS

```js
const JSZip = require('jszip');
const fs = require('fs');

const zip = new JSZip();

try {
  const pdfData = fs.readFileSync('example.pdf');
  zip.file('PDFFile.pdf', pdfData);

  zip.file('Textfile.txt', 'I am generating this file to be zipped\n');

  const images = ['avatar-1.jpg', 'avatar-2.jpg'];
  const img = zip.folder('images');

  for (const image of images) {
    const imageData = fs.readFileSync(image);
    img.file(image, imageData);
  }

  zip
    .generateNodeStream({ type: 'nodebuffer', streamFiles: true })
    .pipe(fs.createWriteStream('example.zip'))
    .on('finish', function () {
      console.log('example.zip created.');
    });
} catch (err) {
  console.error(err);
}
```
