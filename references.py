# -*- coding: utf-8 -*-
__author__ = 'Andres'
import re
from pprint import pprint

referencesRegEx = re.compile(r'&gt;(.+)&lt;/ref&gt;')

if __name__ == '__main__':
    with open("wiki.xml", encoding='utf-8') as f:
        data = f.read()

    references = (re.findall(referencesRegEx, data))
    for i in (references):
        print(i)
    print(len(references))