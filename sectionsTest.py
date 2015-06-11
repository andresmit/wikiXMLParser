# -*- coding: utf-8 -*-
__author__ = 'Andres'
import re
from pprint import pprint

def sectionsParser(text):
    pass
    return {}

if __name__ == '__main__':
    with open("armeenia.txt", encoding='utf-8') as f:
        text = f.read()

    level = 0
    entries = re.split("\n=", text)
    #pprint(entries)
    print(len(entries))
    textDict = {}
    titles = []
    sectionTitleRegEx = re.compile('={,1}.+={2,}\n')
    intro = entries[0]
    print('intro ', intro)
    textDict['intro']=intro

    for i in entries[1:]:
        #TODO: add to {} form
        #TODO: manage subsections nicely
        title = re.match(sectionTitleRegEx, i)
        if title:
            titleEnd = title.end()
            print(titleEnd)
            title = title.group()
            text = i[titleEnd:]

            print(title, title.count('='))
            print(text)
            textDict[]
            #print(title.count('='))

          #print
    print(textDict)

"""
    pprint(data.splitlines())
    sectionTitles = []
    for i in data:
        sectionTitlesRegEx = re.compile(r'={2,}([^=]+)={2,}\n')
        sectionTitle = (re.findall(sectionTitlesRegEx, i))
        sectionTitles.append(sectionTitle.copy())
    pprint(sectionTitles)
    """
