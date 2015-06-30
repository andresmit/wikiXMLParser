# -*- coding: utf-8 -*-
__author__ = 'Andres'
import re
from itertools import chain
from pprint import pprint
from externalLink import addExternalLinks, ExtLinkBracketedRegex
from internalLink import findBalanced, addIntLinks

referencesRegEx = re.compile(r'&lt;ref(.+?)(/&gt|/ref&gt);', re.DOTALL|re.IGNORECASE)
referencesRegEx = re.compile(r'<ref>?(.+?)<?(/>|/ref>)', re.DOTALL|re.IGNORECASE)

referencesEndRegEx = re.compile(r'&lt;/ref&gt;', re.IGNORECASE)

def refsParser(refsDict):
    for key in refsDict:

        #does a ref contain external links
        value = refsDict[key]
        value = {'text':value}
        if ExtLinkBracketedRegex.search(value['text']):
            value = addExternalLinks(value)


        intlinks = [x for x in findBalanced(v['text'], openDelim='[[', closeDelim=']]')]
        #internal links
        if intlinks:
            value = addIntLinks(value)



        refsDict[key]=value
    return refsDict

refTagRegEx = re.compile('<ref (\d)+/>')

def reffinder(sectionObj, refsDict):
    text = sectionObj['text']
    reftags = [x for x in refTagRegEx.finditer(text)]
    if reftags:
        references = []
        for tag in reftags:
            references.append(int(tag.group(1)))

        sectionObj['references'] = references

        text = refTagRegEx.sub('', text)
        sectionObj['text'] = text

    return sectionObj

def referencesParser(text):
    """
    :param text: takes the whole text of an article, searches for references, cleans the text,
    marks the reference indeces from zero inside the text.
    :return: the tagged text and a tag:reference dictionary to be used in sectionParser
    """
    references = referencesRegEx.finditer(text)
    count = 0
    refs = []
    spans = []
    for i in references:
        refs.append(i.group())
        spans.append(i.span())
        count += 1
    done = set()
    nameRegEx = re.compile(r"""(name=["']*.*?["']*)(\s|/|>)""")

    for index, obj in enumerate(refs):

        if str(obj).startswith('<ref name='):
                nameTag = re.escape(nameRegEx.search(obj).group(1))

                if nameTag not in done:
                    nameTag = re.escape(nameRegEx.search(obj).group(1))
                    indeces = [i for i, x in enumerate(refs) if re.search(nameTag, x)]
                    matches = [refs[i] for i in indeces]
                    full = max(matches, key=len)

                    for i in indeces:
                        refs[i]= full

                    done.add(nameTag)

    #eliminate <ref tag or other rudiments from the ref string

    for i in range(len(refs)):
        #print('SIIT', refs[i])
        lastindex = refs[i].rindex('<')
        firstindex = refs[i].index('>')+1
        refs[i]=refs[i][firstindex:lastindex]

    #a ref string:position int dictionary
    refspos = {}
    c = 0
    for i in refs:
        if i not in refspos.keys():
            refspos[i] = c
            c +=1
        else:
            continue

    #print(refspos)

    #eliminate old, bad <ref> tags and insert clean  ones <ref 1..2..3/> to the same spot.
    newText = ''
    assert len(spans) == len(refs)
    #Could happen... havent yet.
    next = 0
    for i in range(len(spans)):
        start = spans[i][0]
        newText+=text[next:start]+'<ref '+str(refspos[refs[i]])+'/>'
        next = spans[i][1]

    newText+=text[next:]

    #switch keys:values in the dictionary for use in sectionsParser
    #positiontag:ref
    newDict  = {y:x for x,y in refspos.items()}

    return newText, newDict



if __name__ == '__main__':
    with open("armeenia.txt", encoding='utf-8') as f:
        data = f.read()

    newText, newDict = referencesParser(data)
    for i in newDict:
        print(i)
"""
    referencesRegEx = re.compile(r'&lt;ref(.+?)(/&gt|/ref&gt);', re.DOTALL|re.IGNORECASE)
    references = referencesRegEx.finditer(data)
    refend = referencesEndRegEx.finditer(data)
    count = 0
    ends = []
    for i in references:
       # print(i.end())
       print(i.group())
       print('--------------------------')
       count += 1
    print('sss', referencesParser(data))
    print(count)
"""