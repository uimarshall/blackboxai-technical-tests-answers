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
