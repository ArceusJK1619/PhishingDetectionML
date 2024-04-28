import streamlit as st
import pickle 
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup





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
def count_equals_in_url(url):
    num_equals = url.count("=")  
    return num_equals
def count_QMarks_in_url(url):
    num_qmark = url.count("?")
    return num_qmark
def count_ampersand_in_url(url):
    num_ampersand = url.count("&")
    return num_ampersand
def count_specialCharachters_in_url(url):
    special_characters = "!@#$%^&*()-_+=[]{}|;:,.<>?/~"
    num_special_chars = sum(1 for char in url if char in special_characters)   
    return num_special_chars
def count_css_files_in_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        css_links = soup.find_all('link', rel='stylesheet')
        num_css_files = len(css_links)
        return num_css_files
    except Exception as e:
        print(f"Error fetching or parsing HTML content: {e}")
        return None
def count_js_files_in_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        script_tags = soup.find_all('script')
        external_js_files = [tag['src'] for tag in script_tags if 'src' in tag.attrs]
        num_js_files = len(external_js_files)
        return num_js_files
    except Exception as e:
        print(f"Error fetching or parsing HTML content: {e}")
        return None
def count_self_referencing_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        base_url = urlparse(url).scheme + "://" + urlparse(url).netloc
        anchor_tags = soup.find_all('a', href=True)
        num_self_refs = sum(1 for tag in anchor_tags if urlparse(tag['href']).netloc == '' or urlparse(tag['href']).netloc == urlparse(url).netloc)
        
        return num_self_refs
    except Exception as e:
        print(f"Error fetching or parsing HTML content: {e}")
        return None
def count_external_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        base_url = urlparse(url).scheme + "://" + urlparse(url).netloc
        anchor_tags = soup.find_all('a', href=True)
        num_external_links = sum(1 for tag in anchor_tags if urlparse(tag['href']).netloc != base_url)
        return num_external_links
    except Exception as e:
        print(f"Error fetching or parsing HTML content: {e}")
        return None
def count_empty_references(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        empty_ref_tags = soup.find_all('a', href=False)
        num_empty_refs = len(empty_ref_tags)
        return num_empty_refs
    except Exception as e:
        print(f"Error fetching or parsing HTML content: {e}")
        return None
def classify(x):
    if x == 1:
        return True
    else :
        return False 
    




