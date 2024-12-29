#!/usr/bin/env python
import sys
import os

from bs4 import BeautifulSoup

with open("lyrics/Alcohol.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(soup.prettify())
