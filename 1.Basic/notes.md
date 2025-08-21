# 📝 Module 1: The Basics of Web Scraping

This module covers the fundamental tools for scraping static websites. Static websites are pages where the content is fixed and doesn't change based on user interaction. Think of a simple blog post or an "About Us" page.

## Key Concepts

### 1. **Requests** 📦
`requests` is a simple yet powerful Python library for making HTTP requests. It's the first step in any web scraping process: getting the raw HTML from a server.

* **`GET` Request**: This is the most common type of request. It's like typing a URL into your browser to *get* or *retrieve* information. You use `requests.get(url)` for this.
* **`POST` Request**: This is used to *send* data to a server, like submitting a login form or a search query. You use `requests.post(url, data=payload)` for this.
* **Status Codes**: Every HTTP response comes with a status code.
    * `200 OK`: Everything went well.
    * `404 Not Found`: The page doesn't exist.
    * `403 Forbidden`: You don't have permission to access this page.
    * `500 Internal Server Error`: The server had a problem.

### 2. **BeautifulSoup4 (BS4)** 🥣
Once you have the HTML content from `requests`, you need a way to parse and navigate it. Raw HTML is just a long string of text. BeautifulSoup turns this string into a structured object that you can easily search.

* **Parser**: BS4 needs a parser to understand the HTML. `lxml` is a popular and fast choice.
* **Finding Elements**:
    * `soup.find('tag_name')`: Finds the *first* occurrence of a tag (e.g., `soup.find('p')` for the first paragraph).
    * `soup.find_all('tag_name')`: Finds *all* occurrences of a tag and returns them as a list.
* **Searching by Attributes**: You can be more specific by searching for tags with certain attributes, like a class or ID.
    * `soup.find('div', class_='content')`
    * `soup.find('span', id='username')`
* **Extracting Data**:
    * `.text`: Gets the human-readable text inside a tag.
    * `tag['attribute']`: Gets the value of an attribute (e.g., `link['href']` to get the URL from an `<a>` tag).

### 3. **JSON and APIs** ⚙️
Many websites load data from an **API** (Application Programming Interface). Instead of sending a full HTML page, the server sends just the raw data in a structured format called **JSON** (JavaScript Object Notation). This is often easier to work with than parsing HTML.

* **JSON Structure**: JSON looks like a Python dictionary (key-value pairs) and can contain lists.
* **Parsing JSON**: The `requests` library has a built-in `.json()` method that automatically parses a JSON response into a Python dictionary, making it incredibly easy to access the data.