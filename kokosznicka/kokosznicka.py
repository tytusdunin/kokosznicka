import re

def popr_kapitalizacja(input, replace):
    """
    Ta funkcja decyduje o tym, w jakiej kapitalizacji podmiany dokonać w regexie. Przyjmuje obiekty "input" oraz "output" typu string.
    """
    if input.isupper():
        return replace.upper()
    elif input.istitle():
        return replace.capitalize()
    else:
        return replace.lower()

wyjątki = {
    # przyrostki bezproblemowe
    ' cyber': ' cyber-',
    'cyber ': 'cyber ',
    ' hiper': ' hiper-',
    'hiper ': 'hiper ',
    ' super': ' super-',
    'super ': 'super ',
    ' nie': ' nie-',
    'nie ': 'nie ',
    ' bez': ' bez-',
    'bez ': 'bez ',
    ' śród': ' śród-',
    ' naj': ' naj-',
    ' poli': ' poli-',
    ' mili': ' mili-',
    ' pra': ' pra-', #praugrofiński
    ' nau': ' na-u', #naurodzić, naubliżać
    ' prze': ' prze-',

    #ch
    'tysiąchektarow': 'tysiąc-hektarow',
    #cz
    ' specz': ' spec-z',
    ' tysiączł': ' tysiąc-zł',
    # ' tysiączn': ' tysiąc-zn', (tysiączłotowy, ale tysiączny)
    #dz, dź i dż
    ' nad': ' nad-',
    'nad ': 'nad ',
    ' nadzia': ' na-dzia',
    ' nadziel': ' na-dziel',
    ' nadziej': ' na-dziej',
    ' nadzier': ' na-dzier',
    ' nadziew': ' na-dziew',
    ' nadziw': ' na-dziw',

    ' odźwie': ' odź-wie',
    ' odzie': ' o-dzie',
    ' od': ' od-',
    'od ': 'od ',

    ' pod': ' pod-',
    'pod ': 'pod ',
    ' podziw': ' po-dziw',
    ' podzio': ' po-dzio',
    ' podzió': ' po-dzió',
    ' podziel': ' po-dziel',
    ' podziw': ' po-dziw',
    ' podzwo': 'po-dzwo', 
    ' podzwa': ' po-dzwa',

    ' ponad': ' ponad-',
    'ponad ': 'ponad ',
    ' przedzwo': ' prze-dzwo',
    ' nadzwo': ' na-dzwo',
    ' budże': " bud-że",
    'przedziw': "prze-dziw",
    'pozau': 'poza-u',
    
    #sz
    ' eks': ' eks-',
    'eks ': 'eks ',

    'nauk': 'na-uk',
    'naucz': 'na-ucz',
    'marzną': 'mar-zną',
    'marznie': 'mar-znie',
    'marzli': 'mar-zli',
    'marzły': 'mar-zły',
    'tarzan': 'tar-zan',
    'laurk': 'la-urk',
    'eus ': 'e-us ',
    'eusz': 'e-usz', #ALE jubileuszowy, więc bez spacji
    'eum ': 'e-um '

}

podmianki = {
    # Dwu- i trójznaki
    'rz': 'ž',
    'sz': 'š',
    'ch': 'ĥ',
    'cz': 'č',
    'dz': 'ʒ',
    'dż': 'ǯ',
    'dzi': 'ʒ́i',
    # Półsamogłoski
    'io': 'ĵo',
    'ia': 'ĵa',
    'ie': 'ĵe',
    'ię': 'ĵę',
    'ią': 'ĵą',
    'eu': 'eĺ',
    'au': 'aĺ',
    # Samogłoski + "dzi"
    'dzio': 'ʒ́o',
    'dzia': 'ʒ́a',
    'dzie': 'ʒ́e',
    'dzię': 'ʒ́ę',
    'dzią': 'ʒ́ą',
    'dziu': 'ʒ́u',
    'dzió': 'ʒ́ó',
    # Zmiękczenia
    'zi': 'ẑi',
    'si': 'ŝi',
    'ci': 'ĉi',
    'ki': 'k̂i',
    'gi': 'ĝi',
    'ni': 'ňi'
}

samogł = "aeiouyóęąAEIOUYÓĘĄ"
sonorne_i_boczne = "nmlrłńjň"

class Kokosznicka:
    def __init__(self, version):
        self.version = "v1.0"

    def normalize(string):
        """
        Metoda normalize() przyjmuje obiekt typu string i normalizuje pisownie wieloznakową. Zwraca obiekt typu string z dezabiguowaną pisownią pół-fonetyczną.
        """
        # dajemy wyjątki
        lookup_wyj = {k.lower(): v for k, v in wyjątki.items()}

        pattern = re.compile(
            "|".join(map(re.escape, sorted(lookup_wyj.keys(), key=len, reverse=True))), 
            re.IGNORECASE
        )

        result = pattern.sub(
            lambda m: popr_kapitalizacja(m.group(0), lookup_wyj[m.group(0).lower()]), 
            string
        )

        # DAJEMY PODMIANKI
        lookup_map = {k.lower(): v for k, v in podmianki.items()}

        pattern = re.compile(
            "|".join(map(re.escape, sorted(lookup_map.keys(), key=len, reverse=True))), 
            re.IGNORECASE
        )

        result2 = pattern.sub(
            lambda m: popr_kapitalizacja(m.group(0), lookup_map[m.group(0).lower()]), 
            result
        )
        result3 = pattern.sub(
            lambda m: popr_kapitalizacja(m.group(0), lookup_map[m.group(0).lower()]), 
            result2
        )

        # USUWAMY "- "
        result4 = result3.replace("- ", " ")
        return result4
    
    def syllablecount(string):
        """
        Metoda syllablecount() przyjmuje obiekt typu string i zwraca obiekt typu int odpowiadający liczbie sylab w przyjętym stringu.
        """
        string = Kokosznicka.normalize(string)
        counter = 0
        for char in string:
            if char in samogł:
                counter += 1
        return counter
    
    def hyphenate(string):
        """
        Metoda hyphenate() przyjmuje obiekt typu string i zwraca obiekt typu string z myślnikami ("-") rozdzielającymi sylaby.
        """
        string = Kokosznicka.normalize(string)
        wordlist = string.split()
        masterlist = []
        overcounter = False
        hyphencounter = 0
        stan = ""

        for word in wordlist:
            count = Kokosznicka.syllablecount(word)
            masterlist.append((word, count))
            # Powyższa pętla zwraca listę tupli złożonych ze słowa i liczby sylab

        newlist = []

        for word,count in masterlist:
            overcounter = 0
            if count <= 1:
                newlist.append(word)
            else:
                hyphencounter = count - 1
                newword = ""
                for i in range(len(word)):
                    char = word[i]

                    # Tworzymy zmienną "char2" do patrzenia o jedną literę w przyszłość
                    try:
                        char2 = word[i+1]
                    except:
                        char2 = "0"

                    # Tworzymy zmienną "char3" do patrzenia o jedną literę w przyszłość
                    try:
                        char3 = word[i+2]
                    except:
                        char3 = "0"

                    # Tworzymy zmienną "char4" do patrzenia o jedną literę w przyszłość
                    try:
                        char4 = word[i+3]
                    except:
                        char4 = "0"

                    if char not in samogł:
                        if overcounter == True:
                            if char2 != "-" and char3 != "-": #and char4 != "-":
                                newword = newword + char + "-"
                                hyphencounter -= 1
                                overcounter = False
                            else:
                                newword = newword + char
                                hyphencounter -= 1
                                overcounter = False
                        else:
                            newword = newword + char
                    elif char in samogł and hyphencounter != 0:
                        if char2 in sonorne_i_boczne and char3 in samogł:
                            if char2 != "-" and char3 != "-": #and char4 != "-":
                                newword = newword + char + "-"
                                hyphencounter -= 1
                                overcounter = False
                            else:
                                newword = newword + char
                                hyphencounter -= 1
                                overcounter = False
                        elif char2 == char3 or char2 in sonorne_i_boczne or char3 in sonorne_i_boczne:
                            if char2 in samogł:
                                if char2 != "-" and char3 != "-": #and char4 != "-":
                                    newword = newword + char + "-"
                                    hyphencounter -= 1
                                    overcounter = False
                                else:
                                    newword = newword + char
                                    hyphencounter -= 1
                                    overcounter = False
                            else:
                                newword = newword + char
                                overcounter = True
                        else:
                            if char2 != "-" and char3 != "-": #and char4 != "-":
                                newword = newword + char + "-"
                                hyphencounter -= 1
                                overcounter = False
                            else:
                                newword = newword + char
                                hyphencounter -= 1
                                overcounter = False
                    elif char in samogł and hyphencounter == 0:
                        newword = newword + char
                newlist.append(newword)
        wynik = " ".join(newlist)
            
        # Odwracamy słownik
        odwrotne_podmianki = {v.lower(): k for k, v in podmianki.items()}

        # Pattern z posortowanych i "escapowanych" kluczy
        pattern_odwrotny = re.compile(
            "|".join(map(re.escape, sorted(odwrotne_podmianki.keys(), key=len, reverse=True))), 
            re.IGNORECASE
        )

        # Wracamy do oryginału
        # Podwójnie, aby mniejsze fragmenty tez wróciły do oryginalnej postaci

        finalowy = pattern_odwrotny.sub(
            lambda m: popr_kapitalizacja(m.group(0), odwrotne_podmianki[m.group(0).lower()]), 
            wynik
        )
        finalresult = pattern_odwrotny.sub(
            lambda m: popr_kapitalizacja(m.group(0), odwrotne_podmianki[m.group(0).lower()]), 
            finalowy
        )
        return finalresult
        
kkszn = Kokosznicka
