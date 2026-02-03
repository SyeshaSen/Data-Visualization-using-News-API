# Homework 4

## Learning Outcomes

- Reading API documentation
- Parsing JSON data
- Visualizing data
- Sorting and filtering Pandas dataframes
- Privacy implications of pushing passwords to GitHub

## Overview

### 1: News API

This assignment will use the News API (https://newsapi.org/docs), which provides users with data about news from around the internet.

Please go to the website and generate a free key (using a fake name and your university email address, if you don't want to share your info with them) here: https://newsapi.org/register

Store that key somewhere safe. Treat it like a password.

You'll notice that there is an existing library in Python that does what we are implementing. For full credit on this assignment, do not use that library.

### 2: Article

Implement the `class Article` to store the details of a news article that can be returned by the API.
Objects of this type will represent an article from the response object (https://newsapi.org/docs/endpoints/top-headlines).

It should appropriately store these strings as either attributes or properties:
- `url`
- `source`
- `author`
- `title`
- `description`
- `published_at`
- `content`

For each one, it is up to you whether you make it an attribute or a property.

Don't forget to create a test class in the `tests` directory to test your work.

### 3: SearchNews

Implement the `class SearchNews`:
- The constructor should read your API key from a separate text file, and store it as an attribute (with two underscores in its name).
- Implement the method `get_top_headlines()` which pulls from the `/top-headlines` endpoint.
- Implement the method `def get_everything()` which pulls from the `/everything` endpoint.

To pull from these endpoints, you will need to look up documentation for:
- the News API (https://newsapi.org/docs)
- the `requests` Python library (https://pypi.org/project/requests/)

Important: hide the key. Do not push it to GitHub. (This is why we read the key from the file.)

To avoid pushing it to GitHub, you can either:
- always `git add` all files except the file that contains the key
- add the file that contains the key to a `.gitignore` file, so that it never gets `git add`ed

Don't forget to create a test class in the `tests` directory to test your work.

### 4: NewsProcessor

To make the `Article`s easier to read, implement the `class NewsProcessor`:
- Implement the method `to_df()` that takes a `list[Article]` and returns it as a Pandas dataframe. Each property from the `Article` should be a column, and each article should be a row.
  - The optional argument `sort_by`, if passed a `function`, uses that function to sort the rows in the dataframe.
  - The optional argument `filter`, if passed a `function`, uses that function to filter the rows in the dataframe. It should only include rows for which the `function` returns `True`.
- Implement the method `plot_word_popularity()` which takes a `list[Article]` and a `str` search term as arguments. It should make and display a plot of the frequency of that search term in the articles' titles. The x axis should be the range of dates covered by the articles, and the y axis should be the number of articles published with the search term on that day.

Don't forget to create a test class in the `tests` directory to test your work.

## Wrap-up

Don't forget to write tests to ensure your code works!

And, of course, please make sure to answer the questions in `Summary.md`.
