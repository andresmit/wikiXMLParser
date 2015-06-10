# -*- coding: utf-8 -*-
__author__ = 'Andres'

# -*- coding: utf-8 -*-



import re
import json
import pprint

linkBegin = "http://et.wikipedia.org/wiki/"

infob = """iygyugyugyugyugyugyugyuyg{{See artikkel| on Altamira koopast Hispaanias; samanimeliste kohtade kohta vaata lehekülge [[Altamira (täpsustus)]]}}
{{UNESCO
|Nimi       = Altamira
|Pilt       = [[Pilt:Techo de Altamira (replica)-Museo Arqueológico Nacional.jpg|300px|Koopamaalid]]
|Pildiinfo  = Altamira koopamaalid
|Asukoht    = {{PisiLipp|Hispaania}}
|Tüüp       = Kultuurimälestis
|Kriteerium = I, III
|ID         = 310
|Regioon    = Euroopa ja Põhja-Ameerika
|Laiuskoord  = 43/22/39/N
|Pikkuskoord = 4/7/9/W
|Aasta      = 1985
|Istung     =
|Laiendatud = 2008
|Ohus       =
}}
}}yuguibguihuihiuih"""

def infoBoxParser(text):
    infobContRegEx = re.compile(r'\{\{[A-Za-zÄÖÕÜäöõü ]+\n(.+)\}\}\n', re.DOTALL)
    #TODO:regex matches some weird stuff. e.g Albaania
    infobContent = re.search(infobContRegEx, text)
    if infobContent:
        infobContent = infobContent.group(1).replace('[', '').replace(']', '').splitlines()  #.replace('|', '').split('\n'))
        infobDict = {}
        for line in infobContent:
            line = line.strip('|  ').strip(' ')
            line = line.split(' = ')
            if len(line) == 2:
                infobDict[line[0].strip(' ')]=line[1].strip('[').strip(']')

        return infobDict

    return None

#pprint.pprint(infobDict)
if __name__ == '__main__':
    ib = re.compile(r'\{\{[A-Za-zÄÖÕÜäöõü]+\n')
    if re.search(ib, infob):
        print('infobox', infoBoxParser(infob))