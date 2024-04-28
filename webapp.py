import streamlit as st
import pickle 
from urllib.parse import urlparse








#Defining the logics required to process the url

def url_length(url):
    a = len(url)
    return a

def extract_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain
def domain_length(domain):
    a = len(domain)
    return a 
def is_https(url):
    if url[0:5]=="https":
        return 1
    else:
        return 0
def count_letters_in_url(url):
    url_lower = url.lower()
    num_letters = sum(c.isalpha() for c in url_lower)
    return num_letters

def count_digits_in_url(url):
    num_digits = sum(c.isdigit() for c in url)
    return num_digits



