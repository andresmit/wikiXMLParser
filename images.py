# -*- coding: utf-8 -*-

__author__ = 'Andres'
import re

section = {'title': 'Nimi', 'text': "\n[[Pilt:Darius I the Great's inscription.jpg|pisi|[[Dareios I]] [[Behistuni raidkiri]], millel mainitakse Armeeniat. [[6. sajand eKr]].]] Kohanimi &quot;Armeenia&quot; pärineb [[Armeenia mägismaa]]l praeguse [[Malatya]] lähedal paiknenud piirkonna ''Armi-'' [[hurri keel|hurrikeelsest]] nimest. [[Aramea keeled|Aramea]] kuju ''ˊarmǝn-āiē'' vahendusel läks see üle [[vanapärsia keel]]de ning esineb [[lokatiiv]]ivormis\n''Arminiyaiy'' kuus korda [[Behistuni raidkiri|Behistuni raidkirjal]] [[6. sajand eKr|6. sajandist eKr]].&lt;ref&gt;R. Schmitt. [http://www.iranica.com/articles/armenia-i ARMENIA and IRAN i. Armina, Achaemenid province.], ''Encyclopædia Iranica'', arhiveeritud aadressil [http://www.webcitation.org/659qWLMs7]&lt;/ref&gt; Teistel andmetel on see nimi moodustatud Armeenia mägismaal elanud rahva armeenide (''arim'') nimest.&lt;ref name='Pospelov'&gt;[[Jevgeni Pospelov|Поспелов Е. М.]] ''Географические названия мира: Топонимический словарь'', М.: Русские словари 1998, lk 160, ISBN 5-89216-029-7&lt;/ref&gt;. [[Vanakreeka keel]]es võttis nimi kuju Ἀρμενία&lt;ref&gt;Фасмер М. [http://dic.academic.ru/dic.nsf/vasmer/35265/армения ''Этимологический словарь русского языка'', [[Progress|Прогресс]] 1964, kd 1, lk 87: &quot;Арме́ния, vanakreeks sõnast Ἀρμενία. Juba vanapärsia ''Armaniya-'', ''Armina-'' 'Armeenia'; vt Бартоломэ, Air. Wb. 197; Хюбшман, IF 16, 205. Vt армяни́н.''&lt;/ref&gt;. Seda nime mainis esmakordselt [[Hekataios]] Mileetoselt.\n\n [[File:Gamma phage.png|pisi|[[Bakteriofaagid]]e hulka kuuluv [[viirus]]]] Enne nime Ἀρμένιοι levikut kitsuti [[armeenlased|armeenlasi]] vanakreeka keeles Μελιττήνιοι&lt;ref name=&quot;Дьяконов1981&quot;/&gt;.\n\nArmeenia [[armeenia keel|armeeniakeelne]] nimi on Հայք (''Hajkh''). [[5. sajand]]i ajaloolase [[Movses Khorenatsi]] järgi andis selle Armeenia legendaarne patriarh [[Hajk]], kelle järglase [[Aram]]i, [[Urartu]] kuninga nimest sündis omakorda nimi ''Armeenia''.&lt;ref&gt;[http://www.vehi.net/istoriya/armenia/khorenaci/01.html Мовсес Хоренаци &quot;История Армении&quot;], arhiveeritud [http://www.webcitation.org/659qX7URz]&lt;/ref&gt; Legendi järgi lõi Hajk [[2492 eKr]] lahingus [[Assüüria]] kuningat [[Bel]]i ning hiljem moodustas esimese Armeenia riigi. See aasta on [[vanaarmeenia ajaarvamine|Vanaarmeenia ajaarvamise]] algusaasta. Teine versioon seostab seda nimetust [[Ḫajaša]] riigiga&lt;ref&gt;Hrach K. Martirosyan. ''Etymological dictionary of the Armenian inherited lexicon'', Brill Academic Publishers 2009, lk 382–385, ISBN 978-90-04-17337-8&lt;/ref&gt;. Kolmanda versiooni järgi pärineb see praeguse [[Malatya]] [[urartu keel|urartukeelsest]] nimest ''Ḫāti''&lt;ref name=&quot;Дьяконов1981&quot;&gt;[[Igor Djakonov|Дьяконов И. М.]] ''Малая Азия и Армения около 600 г. до н.э. и северные походы вавилонских царей''. – ''[[Vestnik Drevnei Istorii|Вестник древней истории]]'', 1981, nr 2, lk 34—63.&lt;/ref&gt;&lt;ref&gt;A. E. Redgate. ''The Armenians'', Oxford: Blackwell 1998, lk  24, ISBN 0-631-14372-6&lt;/ref&gt;.\n\nKeskajal asendus armeenia kohanimejärelliide ''-kh'' pärsia keelest laenatud järelliitega ''[[-stan]]''.&lt;ref&gt;Капанцян Г. ''Хайаса--колыбель армян: этногенез армян и их начальная история'', Изд-во Академии наук Армянской ССР 1947, lk 10 [http://books.google.co.uk/books?id=HDRIAAAAMAAJ&amp;q=%5B%D1%85%D0%B0%D0%B9%D0%B0%D1%81%D1%82%D0%B0%D0%BD+%D1%81%D1%83%D1%84%D1%84%D0%B8%D0%BA%D1%81%5D&amp;dq=%5B%D1%85%D0%B0%D0%B9%D0%B0%D1%81%D1%82%D0%B0%D0%BD+%D1%81%D1%83%D1%84%D1%84%D0%B8%D0%BA%D1%81%5D&amp;source=bl&amp;ots=m1mrKyyoYt&amp;sig=Nja4qrhSWUqWYfSfvuMzMeqZETg&amp;hl=ru&amp;sa=X&amp;ei=uFIqUJqfDKKo0QWUiIEI&amp;redir_esc=y Google'i raamat]&lt;/ref&gt; ja Armeeniat hakati kutsuma Հայաստան (''Hajastan'').\n"}


def imageParser(section):
    """return a list object of image data
         [
       {
             image_url = "http://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/R%C3%B5uge_Suurj%C3%A4rv_2011_10.jpg/1024px-R%C3%B5uge_Suurj%C3%A4rv_2011_10.jpg"
             text: "Rõuge Suurjärv on Eesti sügavaim järv (38 m)."
             links: [ ...] // sama loogika nagu sektsiooni tasemel lingid.
       }
   ]"""
    return []

def balancedSquareBrackets(text):
    """returns text between balanced first occurrence of [ and last """
    openbr = 0
    cur = 0
    for char in text:
        cur +=1
        if char == '[':
            openbr += 1
        if char == ']':
            openbr -= 1
        if openbr == 0:
            break
    return (text[:cur])



if __name__ == '__main__':
    imageRegEx = re.compile(r'\[\[(Pilt|File)\:.+')
    link = imageRegEx.finditer(section['text'])
    images = []
    for i in link:
        imagetag = balancedSquareBrackets(i.group())

        u = {}
        pieces = imagetag.split('|')
        url = pieces[0][2:]
        text = pieces[-1][:-2]
        u['url'] = url
        u['text'] = text
        u['links'] = None
        #TODO:Links
        images.append(u)
        print(imagetag)

    section['images'] = images
    print(section)