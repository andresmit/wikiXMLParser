# -*- coding: utf-8 -*-

__author__ = 'Andres'

# Example of incremental XML parsing


from xml.etree.ElementTree import iterparse

def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            print(elem.tag)
            print(elem.text)
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass

# Find zip code with most potholes


data = parse_and_remove('wiki.xml', "wikimedia/wikimedia" )
i=0
for page in data:
  print("Page", i)
  i+=1
