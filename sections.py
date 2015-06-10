# -*- coding: utf-8 -*-
__author__ = 'Andres'
import re
from pprint import pprint
text = """
{{See artikkel| räägib üldmõistest; Herodotose teose kohta vaata artiklit [[Historia]]}}
{{ToimetaAeg|kuu=oktoober|aasta=2012}}{{keeletoimeta}}

'''Ajalugu''' ([[Kreeka keel|kreeka keeles]] {{lang|el|''ἱστορία''}} - ''historia'', mis tähendab uurimust) tähendab nii [[minevik]]us toimunut kui ka mineviku taasesistamist. Ajalooteadus uurib inimkonna ajalugu alates inimese kujunemisest ja lõpetades tänapäeva sündmustega. Ajalugu on humanitaarteadus, sest uurib inimesega seounduvat. Selle harud on [[arheoloogia]] ja [[etnoloogia]].&lt;ref&gt;Kõiv, Mait. Inimene, ühiskond, kultuur. I osa: vanaaeg. 2006. Lk. 8.&lt;/ref&gt;

==Liigitus==
Ajalooteadus on üks kõige laiahaardelisemaid teadusi. See on tingitud sellest, et igal ühiskonnaelu valdkonnal on ajalugu, mida saab ajalooteaduse meetoditega uurida.

Ajalugu on traditsiooniliselt jagatud järgmiselt:
*Kronoloogiline
**Selle kohaselt jaguneb ajalugu (st minevik) eelajalooliseks ja ajalooliseks ajaks. Ajalooline aeg omakorda perioodideks, millest kõige üldisemad on [[vanaaeg]], [[keskaeg]], [[uusaeg]] ja [[uusim aeg|kaasaja ajalugu]] ehk [[lähiajalugu]]. Nende ajajärkude kronoloogilised piirid on vaieldavad. Samuti jagunevad need ajajärgud ise lühemateks perioodideks. Nii eristatakse keskajas vara-, kõrg- ja hiliskeskaega; [[uusaeg|uusajas]] [[varauusaeg]]a (1500–1800).
*Geograafiline
**Selle kohaselt eristuvad terviklikena mandrite või suuremate regioonide ajalood. Sellisteks on eriti sageli [[Euroopa ajalugu]], aga ka [[Ladina-Ameerika ajalugu]] või [[Aafrika ajalugu]]. Piirkondlike ajalugudena aga näiteks [[Baltikum]]i, [[Lähis-Ida]] või [[Balkan]]i ajalugu.
*[[Riik]]ide ja [[rahvus]]te järgi
**See on kõige enam levinud ajalookäsitlus. Seda eriti paaril viimasel aastasajal, kui [[ajalookultuur]]i juhtivad maad on olnud [[rahvusriik|rahvusriigid]]. [[Riik]]ide ja [[rahvus]]te ajalood, olgu kirjutatud selle [[riik|riigi]] elaniku või [[rahvus]]e esinadaja poolt või kellegi teise poolt, on kõige enam vaidlusi tekitanud. Seda eriti juhul kui mõnda [[riik]]i või [[rahvas]]t on ajaloos erilisele kohale tõstetud või siis teisi [[rahvas|rahvaid]], eriti väiksemaid on tahetud sootuks n-ö ajaloost välja jätta.
*Temaatiline
**Temaatiline ajalookäsitlus keskendub ühele või mitmele ajaloovaldkonnale. Sageli on valdkondlikud ajalood kõige teaduslikumad kuna kasutavad kõige laiadasemalt erinevaid uurimismeetodeid. Kuid on ka vastupidised näited, kus näiteks poliitilised ajalood on väga ideologiseeritud. Oma kujunemise ajal oli ajalooteadus suuresti poliitiline ajalugu.
**Traditsiooniliselt eristuvad järgmised teemad:
***Poliitiline ajalugu, milles omakorda on rahvusvaheliste suhete ajalugu ja diplomaatia ajalugu
***Ideede ajalugu ja mentaliteedi ajalugu
***Majandusajalugu, milles on muuhulgas kaubanduse ajalugu, tööstuse ja põllumajanduse ajalugu
***Sotsiaalajalugu, mis on äärmiselt lai valdkond ja kõige tihedamalt põimunud sotsiaalteadustega. Sellesse kuuluvad rahvastiku ajalugu, sotsiaalsete rühmade ja suhete ajalugu, milles omakorda on suurte valdkondadena naiste, tööliste ja vähemuste ajalugu
***Kultuuri- ja [[kunstiajalugu]]

==Allikad==
&lt;center&gt;&lt;div style=&quot;text-align: center; margin: 0 10% 1em 10%;&quot;&gt;
{| align=center class=&quot;disputeabout&quot; style=&quot;background: beige; border: 1px solid #aaa; padding: .2em; margin-bottom: 3px; font-size: 95%; width: auto;&quot;
| valign=&quot;top&quot; style=&quot;padding: .2em&quot; | [[Pilt:Stop_hand.png|45px|Vaidlustatud]]
| style=&quot;padding: 0.1em&quot; width = 320| '''Artikli selle osa faktiline õigsus on vaieldav.'''&lt;br&gt;
''Vaieldav on allikate selline liigitus.''
|-
|colspan=2 align=center|&lt;div style=&quot;font-size: 90%;&quot;&gt;Vaata lähemalt selle artikli [[:{{NAMESPACE}} talk:{{PAGENAME}}|aruteluleheküljelt]].&lt;/div&gt;
|}
&lt;/div&gt;&lt;/center&gt;
*[[Esemelised ajalooallikad]] ehk [[muistis]]ed: [[kinnismuistis]]ed ja [[irdmuistis]]ed
*[[Kirjalikud ajalooallikad]]: [[ürik]]ud, [[kroonika]]d, [[seadus]]ed, [[memuaarid]], [[statistilised materjalid]] jne
*[[Suulised ajalooallikad]]: [[pärimus]]ed, [[rahvaluule]] ([[legend]]id, [[müüt|müüdid]], [[muinasjutt|muinasjutud]])
*[[Etnoloogilised ajalooallikad]]: [[tava]]d, [[komme|kombed]] ja [[traditsioon]]id
*[[Lingvistilised ajalooallikad]]: [[Keel (keeleteadus)|keel]] ja [[murre|murded]]
*[[Audiovisuaalsed ajalooallikad]]: [[foto]]d, [[film]]id ja [[helisalvestis]]ed

==Abiteadused==
&lt;center&gt;&lt;div style=&quot;text-align: center; margin: 0 10% 1em 10%;&quot;&gt;
{| align=center class=&quot;disputeabout&quot; style=&quot;background: beige; border: 1px solid #aaa; padding: .2em; margin-bottom: 3px; font-size: 95%; width: auto;&quot;
| valign=&quot;top&quot; style=&quot;padding: .2em&quot; | [[Pilt:Stop_hand.png|45px|Accuracy dispute]]
| style=&quot;padding: 0.1em&quot; width = 320| '''Artikli selle osa faktiline õigsus on vaieldav.'''&lt;br&gt;
''Vaieldav on abiteaduste selline liigitus.''
|-
|colspan=2 align=center|&lt;div style=&quot;font-size: 90%;&quot;&gt;Vaata lähemalt selle artikli [[:{{NAMESPACE}} talk:{{PAGENAME}}|aruteluleheküljelt]].&lt;/div&gt;
|}&lt;/div&gt;&lt;/center&gt;
*[[Ajalooline geograafia]] - [[Allikaõpetus]] - [[Antropoloogia]] - [[Arheograafia]] - [[Arheoloogia]] - [[Arhiivindus]] - [[Diplomaatika]] - [[Etnoloogia]] - [[Filateelia]] - [[Folkloristika]] - [[Genealoogia]] - [[Heraldika]] - [[Kronoloogia]] - [[Metroloogia (ajalugu)|Metroloogia]] - [[Mütoloogia]] - [[Numismaatika]] - [[Paleograafia]] - [[Sfragistika]]

==Etümoloogia==
Eestikeelne termin &quot;ajalugu&quot; on [[neologism]], mis on kasutusel alates 19. sajandi teisest poolest. Selle kasutuselevõtjaks peetakse [[Jaan Jung]]i. Enamikus [[Euroopa]] keeltes on selle termini vasteks [[laensõna]], mis pärineb [[kreeka keel|kreekakeelsest]] sõnast ''historia''. See sõna tuleb verbist ''historein'', mis tähendab järeleuurimist.

Eestikeelses sõnas on esil pigem lugu kui sündmus.

==Historiograafia==
{{vaata|Historiograafia}}
Sõna &quot;historiograafia&quot; tuleneb kreeka sõnadest ''ιστορία'' (''historía''; 'ajalugu', 'mineviku uurimine') ja ''γράφο'' (''graphō''; 'kirjutan'), tähendades kõige lihtsamas mõttes ajaloo kirjutamist. Varem ongi ajaloolasi nimetatud [[historiograaf]]ideks. Sellel on aga ka väga palju muid definitsioone, millest olulisemad on:
*Kogu ajalookirjandus üldse või mingi osa sellest (Eesti, Euroopa jne).
*Analüüsiv ja kriitiline (teaduslik) ülevaade ajalookirjandusest mingi valdkonna, maa või perioodi kohta; see tähendus on ka levinuim.
*Ajalooteadmiste, -mõtte, -teaduse (ehk -kirjutuse) ajalugu tervikuna või mõnel üksikul maal (näiteks [[Eesti ajaloo historiograafia]]). Ajalooteadus tänases mõttes hakkas välja kujunema [[Vana-Kreeka]]s 6.–5. sajandil eKr.
*Ajalooteaduse haru, mis uurib ajalookirjutust ennast.

==Viited==
{{viited}}

==Vaata ka==
*[[Ajaloolane]]
*[[Ajaloolaste loend]]
*[[Allikakriitika]]
*[[Arheoloogia]]
*[[Eesti ajalugu]]
*[[Sõjad]]
*[[Sotsiaalajalugu]]
*[[Üldajalugu]]

[[Esiaeg]] - [[Kiviaeg]] - [[Paleoliitikum]] - [[Mesoliitikum]] - [[Neoliitikum]] - [[Eneoliitikum]] - [[Pronksiaeg]] - [[Rauaaeg]] -  [[Ajalooline aeg]] - [[Vanaaeg]] - [[Antiikaeg]] - [[Keskaeg]] - [[Uusaeg]] - [[Uusim aeg]] - [[Ajaarvamine]] - [[Kristlik ajaarvamine]] - [[Kronoloogia]]

[[Diplomaatia]] - [[Dünastiad]] - [[Muuseum]]

[[Kategooria:Ajalugu| ]]"""

def wikiLinkParser(text):
    """returns dict obj"""
    linkBegin = "http://et.wikipedia.org/wiki/"
    linkRegEx = re.compile(r"\[\[([^\]]+)\]")
    link = re.findall(linkRegEx, text)
    print(link)

    """
        link, text = linkBegin + link.group(1), link.group(1)
        return {"url":link, "text":text}
    else:
        linkRegEx = re.compile(r"\[\[([^\|]+)\|([^\]]+)")
        link = re.match(linkRegEx, text)
        link, text = linkBegin + link.group(1), link.group(2)
        return {"url":link, "text":text}
"""
if __name__ == '__main__':
    sectionsRegEx = re.compile(r'(?s)==(.+)==(?:(?!\n\n).)*?\n\n')
    sectiontitlesRegEx =re.compile(r'={2,}([^=]+)={2,}\n')

    secs = re.findall(sectiontitlesRegEx, text)
    if secs:
        print(secs)
        sections = []
        sectionsDict = {}
"""
    for sec in secs:
            sectionsDict['title']=sec[0]
            sectionsDict['text']=sec[1]
            sections.append(sectionsDict.copy())
            print(wikiLinkParser(sec[1]))"""

    #pprint(sections)

#FIXME:
#TODO: related articles, links


# {'sections' : [