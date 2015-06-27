# -*- coding: utf-8 -*-
__author__ = 'Andres'
import re
from itertools import chain
from pprint import pprint
from externalLink import addExternalLinks
from internalLink import findBalanced

referencesRegEx = re.compile(r'&lt;ref(.+?)(/&gt|/ref&gt);', re.DOTALL|re.IGNORECASE)
referencesRegEx = re.compile(r'<ref>?(.+?)<?(/>|/ref>)', re.DOTALL|re.IGNORECASE)

referencesEndRegEx = re.compile(r'&lt;/ref&gt;', re.IGNORECASE)

def referencesParser(sectionObject):
    """
    :param sectionObject: takes a section, searches for references, cleans the text,
    marks the references indexes from zero
    :return: section obj with key-value pair references: [0,1,2] (list of reference indeces)
    """
    obj = sectionObject

    return obj

def referencesCounter(text):
    references = referencesRegEx.finditer(text)
    count = 0
    refs = []
    spans = []
    for i in references:
        refs.append(i.group())
        spans.append(i.span())
        # print(i.end())
        #print(':'+i.group(1))
        #print('--------------------------')
        count += 1
    done = set()

    nameRegEx = re.compile(r"""(name=["']*.*?["']*)(\s|/|>)""")
    for index, obj in enumerate(refs):


        if str(obj).startswith('<ref name='):
                nameTag = re.escape(nameRegEx.search(obj).group(1))
                if nameTag not in done:
            #fulldddRegex = re.compile(obj.rstrip()+'\s*(>|&gt|)')

                    nameTag = re.escape(nameRegEx.search(obj).group(1))
                    indeces = [i for i, x in enumerate(refs) if re.search(nameTag, x)]
                    matches = [refs[i] for i in indeces]
                    print('MATCHES', matches)
                    #full = [i for i in refs if fullRegex.match(i)]
                    print(obj, nameTag, indeces, matches)
                    full = max(matches, key=len)
                    for i in indeces:

                        refs[i]= full
                    done.add(nameTag)

        #nrefs = [i[i.index('>')+1:i.rindex('<')] for i in range(len(refs))]
    for i in range(len(refs)):
        #print('SIIT', refs[i])
        lastindex = refs[i].rindex('<')
        firstindex = refs[i].index('>')+1
        refs[i]=refs[i][firstindex:lastindex]
    #TODO: eliminate all but firs
    refspos = {}
    c = 0
    for i in refs:
        if i not in refspos.keys():
            refspos[i] = c
            c +=1
        else:
            continue
    print(refspos)
    newText = ''
    assert len(spans) == len(refs)
#    for i in spans:
#        newtext+=text[spans[0]:]
    return len(refs), refs
#TODO:add ref indeces to text
if __name__ == '__main__':
    with open("armeenia.txt", encoding='utf-8') as f:
        data = f.read()

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
    print('sss', referencesCounter(data))
    print(count)
