# -*- coding: utf-8 -*-

__author__ = 'Andres'

#incremental XML parsing
import re
from infoBox import infoBoxParser
from pprint import pprint
from xml.etree.ElementTree import iterparse

def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    #next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start' in elem.tag:
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            eletag = elem.tag
            elemtext = elem.text
            yield eletag, elemtext
            #print(eletag)
            #print(elemtext)

            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass



data = parse_and_remove('wiki.xml', "wikimedia/wikimedia" )
linkBegin = "http://et.wikipedia.org/wiki/"
#G:\WikiDumper\etwiki-latest-pages-articles.xml
#def jsonbuilder:

for tag, text in data:
    tag, text = str(tag), str(text)
    if 'title' in tag:
        print('-----------')
        print('title', text)
        print('url', linkBegin+text.replace(' ', '_'))
    if 'timestamp' in tag:
        print('timestamp', text)

    ib = re.compile(r'\{\{[A-Za-zÄÖÕÜäöõü ]+\n')
    if re.search(ib, text):
        print('infoboxdata', infoBoxParser(text))







