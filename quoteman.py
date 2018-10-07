"""            Will scrape: "http://quotes.toscrape.com"
Could be customized to scrape similarly built sites for different things
"""
from csv import DictWriter
from random import choice
from time import sleep

import requests
from bs4 import BeautifulSoup

def list_all_quotes(target_url):
    """
    With a url as an argument, scrapes through each page
    WITHOUT CRAWLING, identifies quotes, & returns an all_quotes list obj
    containing separate dictionaries with 'text', 'author', and 'bio-url'
    as keys for each quote in the list.

    Should be assigned to a variable for use:
      #>>> example = list_all_quotes("http://quotes.toscrape.com/")
      #>>> type(example)      # list
      #>>> quote = randquote(example)
      #>>> type(quote)        # dict

    Useful with randquote() (defined below), which takes an instance of this
    method as an argument to provide a quote at random.
    """
    page_url = "/page/1"
    all_quotes = []
    while page_url:
        # makes quotes_obj taking the target url + the actual page number url:
        soup = make_soup_from(f"{target_url}{page_url}")
        print(f"Now scraping {target_url}{page_url} . . . .")
        quotes = get_quotes(soup)
        # iterates over the quotes obj and appends it to all_quotes list:
        for quote in quotes:
            all_quotes.append({
                "text": get_quote_text(quote),
                "author": get_authors(quote),
                "bio-url": get_urls(quote)
            })
            # looks for the next page button and continues the loop if found:
            next_page = soup.find(class_="next")
            page_url = next_page.find('a')["href"] if next_page else None
            sleep(.25)
    # if no more pages found, prints a buffer and returns the entire list:
    print('\n'*2)
    return all_quotes

def randquote(all_quotes_obj):
    """
    Takes an 'all_quotes' list obj and implements 'random.choice' method;
    returns one quote from the gathered quotes at random. Useful for a game!
    """
    randquote = choice(all_quotes_obj)
    return randquote

def write_quotes(all_quotes_obj):
    """
    Takes all_quotes obj and writes all of the quotes to a csv file.
    Headers are 'text', 'author', and 'bio-url'.
    """
    print("Writing quotes to csv . . . . ")
    with open("quotes.csv", "w", encoding="utf-8") as file:
        headers = ["text", "author", "bio-url"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in all_quotes_obj:
            csv_writer.writerow(quote)
    print("Writing complete!")

def make_soup_from(target_url):
    """Parse html from 'target_url' into bs4 soup object (soup_obj)."""
    source_data = requests.get(target_url)
    soup_obj = BeautifulSoup(source_data.text, "html.parser")
    return soup_obj

def get_quotes(soup_obj):
    """Take soup obj, return quotes obj; identifies by html class 'quote'. """
    quotes = soup_obj.find_all(class_="quote")
    return quotes

def get_quote_text(quotes_obj):
    """Take quotes obj, extracts text; returns quotes_text obj"""
    quote_text = quotes_obj.find(class_="text").get_text()
    return quote_text

def get_authors(quotes_obj):
    """Take quotes obj, extracts author names; returns authors obj"""
    authors = quotes_obj.find(class_="author").get_text()
    return authors

def get_urls(quotes_obj):
    """Take quotes obj, extracts biography stub-urls; returns bio_urls obj"""
    bio_urls = quotes_obj.find("a")["href"]
    return bio_urls

