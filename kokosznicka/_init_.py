import re

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
sonorne_i_boczne = "nmlrłńj"

# Na ten moment nieużywane
półsamogłoskowe_wyjątki = {'ieu', 'eus', 'eum', 'pozau', 'prau', 'nauk', ' nau', 'eus '}
dwuznakowe_wyjątki = {'Tarzan', 'marznąć'}

class Kokosznicka:
    def __init__(self, version):
        self.version = "v1.0"

    def normalize(string):
        """
        Metoda normalize() przyjmuje obiekt typu string i normalizuje pisownie wieloznakową. Zwraca obiekt typu string z dezabiguowaną pisownią pół-fonetyczną.
        """
        pattern = re.compile("|".join(sorted(podmianki, key=len, reverse=True)))
        result = pattern.sub(lambda m: podmianki[m.group(0)], string)
        result = pattern.sub(lambda m: podmianki[m.group(0)], result)
        return result
    
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
                        char2 = "0"

                    if char not in samogł:
                        if overcounter == True:
                            newword = newword + char + "-"
                            hyphencounter -= 1
                            overcounter = False
                        else:
                            newword = newword + char
                    elif char in samogł and hyphencounter != 0:
                        if char2 in sonorne_i_boczne and char3 in samogł:
                            newword = newword + char + "-"
                            hyphencounter -= 1
                            overcounter = False
                        elif char2 == char3 or char2 in sonorne_i_boczne or char3 in sonorne_i_boczne:
                            if char2 in samogł:
                                newword = newword + char + "-"
                                hyphencounter -= 1
                                overcounter = False
                            else:
                                newword = newword + char
                                overcounter = True
                        else:
                            newword = newword + char + "-"
                            hyphencounter -= 1
                            overcounter = False
                    elif char in samogł and hyphencounter == 0:
                        newword = newword + char
                newlist.append(newword)
        wynik = " ".join(newlist)
            
        # Odwracamy słownik
        odwrotne_podmianki = {v: k for k, v in podmianki.items()}

        # Pobieramy klucze odwrotnego słownika
        odwrotne_klucze = list(odwrotne_podmianki.keys())

        # Sortowanie kluczy wg długości malejąco
        odwrotne_klucze_posortowane = sorted(odwrotne_klucze, key=len, reverse=True)

        # Pattern z posortowanych i "escapowanych" kluczy
        pattern_odwrotny = re.compile("|".join(re.escape(k) for k in odwrotne_klucze_posortowane))

        # Wracamy do oryginału
        # Podwójnie, aby mniejsze fragmenty tez wróciły do oryginalnej postaci
        oryginalny_tekst = pattern_odwrotny.sub(lambda m: odwrotne_podmianki[m.group(0)], wynik)
        finalresult = pattern_odwrotny.sub(lambda m: odwrotne_podmianki[m.group(0)], oryginalny_tekst)
        return finalresult
        
kkszn = Kokosznicka