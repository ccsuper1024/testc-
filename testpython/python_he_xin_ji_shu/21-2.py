#!/usr/bin/env python
# coding=utf-8
#多线程下载url

import concurrent.futures
import requests
import threading
import time
import os

def download_one(url):
    resp = requests.get(url)
    print("Read {} from {}".format(len(resp.content), url))

def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one, sites)
def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts', 
        'https://en.wikipedia.org/wiki/Portal:History',  
        'https://en.wikipedia.org/wiki/Portal:Society',  
        'https://en.wikipedia.org/wiki/Portal:Biography',  
        'https://en.wikipedia.org/wiki/Portal:Mathematics',  
        'https://en.wikipedia.org/wiki/Portal:Technology',  
        'https://en.wikipedia.org/wiki/Portal:Geography',  
        'https://en.wikipedia.org/wiki/Portal:Science',  
        'https://en.wikipedia.org/wiki/Computer_science',   
        'https://en.wikipedia.org/wiki/Python_(programming_language)',   
        'https://en.wikipedia.org/wiki/Java_(programming_language)',  
        'https://en.wikipedia.org/wiki/PHP',  
        'https://en.wikipedia.org/wiki/Node.js',   
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print("Download{} sites in {} seconds".format(len(sites), end_time - start_time))

if __name__ == "__main__":
    main()
