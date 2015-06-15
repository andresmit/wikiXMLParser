# -*- coding: utf-8 -*-
__author__ = 'Andres'
import re
from pprint import pprint

def sectionsParser(text):
    pass
    return []

if __name__ == '__main__':
    with open("armeenia.txt", encoding='utf-8') as f:
        text = f.read()

    
    entries = re.split("\n=", text)
    #pprint(entries)
    print(len(entries))
    titles = []
    textDict = {}
    sectionTitleRegEx = re.compile(r'={1,}.+={2,}')
    intro = entries[0]
    print('intro ', intro)
    textDict['intro']=intro
    counts = []
    sections = []
    #pprint(entries[1:])
    for i in entries[1:]:
        section = {}
        
        #TODO: add to {} form
        #TODO: manage subsections nicely
        title = re.match(sectionTitleRegEx, i)
        if title:
            titleEnd = title.end()
            print(title)
            title = title.group()
            text = i[titleEnd:]
            count =  title.count('=')
            section['title']=title.strip('= ')
            section['text']=text
			#Hetkel obj tuple (taseme nr, dict)
            obj = count, section
            print(obj)
            sections.append(section)
            #print(title, count)
            counts.append(count)
    print(counts)
    print(len(counts))
    print(counts[47])

print(sections[0])