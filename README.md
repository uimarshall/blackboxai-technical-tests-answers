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
