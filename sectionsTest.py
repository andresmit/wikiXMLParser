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
    sectionTitleRegEx = re.compile('={1,}.+={2,}')
    intro = entries[0]
    print('intro ', intro)
    textDict['intro']=intro
    counts = []
    countX =0
    pprint(entries[1:])
    for i in entries[1:]:

        #TODO: add to {} form
        #TODO: manage subsections nicely
        title = re.match(sectionTitleRegEx, i)
        if title:
            titleEnd = title.end()
            print(title)
            title = title.group()
            text = i[titleEnd:]
            count =  title.count('=')
            #print(title, count)
            counts.append(count)
    print(counts)
    print(len(counts))
    print(counts[47])

"""
            if counts:
                if count == counts[-1]:
                    countX += 1

                if count > count[-1]:

            else:
                counts.append(count)
"""
            #print(text)
            #textDict[]
            #print(title.count('='))

          #print
"""    print(counts)

    r = []
    l = 3

    def append_h(sammud):
        if sammud >

    for i in counts:
        if i=l:
            r.append(i)
"""
"""
    pprint(data.splitlines())
    sectionTitles = []
    for i in data:
        sectionTitlesRegEx = re.compile(r'={2,}([^=]+)={2,}\n')
        sectionTitle = (re.findall(sectionTitlesRegEx, i))
        sectionTitles.append(sectionTitle.copy())
    pprint(sectionTitles)
    """
