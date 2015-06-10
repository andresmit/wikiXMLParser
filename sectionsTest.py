# -*- coding: utf-8 -*-
__author__ = 'Andres'
import re
from pprint import pprint

if __name__ == '__main__':
    with open("armeenia.txt", encoding='utf-8') as f:
        text = f.read()


    entries = re.split("\n=", text)
    pprint(entries)
    print(len(entries))
    titles = []
    for i in entries:
        if i.startswith('='):
            print(i)
            try:
                titleEnd = i.index(r'\n')
                print(titleEnd)
                titles.append(i[:titleEnd])
                print(i[:titleEnd])
            except Exception:
                titles.append(i)
    print(titles)
"""
    pprint(data.splitlines())
    sectionTitles = []
    for i in data:
        sectionTitlesRegEx = re.compile(r'={2,}([^=]+)={2,}\n')
        sectionTitle = (re.findall(sectionTitlesRegEx, i))
        sectionTitles.append(sectionTitle.copy())
    pprint(sectionTitles)
    """