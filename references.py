# -*- coding: utf-8 -*-
__author__ = 'Andres'
import re
from pprint import pprint

referencesRegEx = re.compile(r'&gt;(.+)&lt;/ref&gt;')
def referencesParser(sectionObject):
    """
    :param sectionObject: takes a section, searches for references, cleans the text,
    marks the references indexes from zero
    :return: section obj with key-value pair references: [0,1,2] (list of reference indeces)
    """
    obj = sectionObject

    return obj
if __name__ == '__main__':
    with open("wiki.xml", encoding='utf-8') as f:
        data = f.read()


    references = referencesRegEx.finditer(data)
    for i in (references):
        print(i)
    print(len(references))