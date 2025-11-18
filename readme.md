# kokosznicka

🇵🇱 Prosty i efektywny sylabifikator dla języka polskiego.

🇬🇧 A simple and effective syllabificator for the Polish language.

```
Zwała się Kokosznicka, z domu Jendykowi-
czówna; jej wynalazek epokę stanowi
```
- Adam Mickiewicz, _Pan Tadeusz_ (Księga III)

> Created with ❤ by Tytus Dunin

## 💡 Introduction
**Kokosznicka** (kkszn) was created to be a fast compromise between accuracy and complexity. While not as accurate and sophisticated as the (currently unpublished) algorithm by Daniel Śledziński [[LINK]](https://journals.indexcopernicus.com/api/file/viewByFileId/113053), kokosznicka seeks to improve upon the widely used Polish hyphenation dictionary for the Knuth algorithm (created by Hanna Kołodziejska and improved upon by Bogusław Jackowski and Marek Ryćko) in that it **prioritizes accuracy in determining the correct number of syllables in each word**.

Any commits and suggestions for improvement are welcome! The ultimate goal is to create a fast and fairly simple algorithm which effectively hyphenates Polish text according to the formalized rules and produces a human-like output.

## ⏬ Installation

You can install the `kokosznicka` package from ty PyPI package repository:

```
pip install kokosznicka
```

To use the package in your project, include this line beforehand in your Python project:

```python
from kokosznicka import Kokosznicka
```

Now you're all set!

## 🔧 Usage

The class `Kokosznicka` contains three methods:

### hyphenate()
This method hyphenates a given string. It inserts a hyphen character ("-") in between syllables.

```python
str = "Genezyp Kapen nie znosił niewoli w żadnej formie — od najwcześniejszego dzieciństwa okazywał wstręt do niej nieprzezwyciężony."

print(Kokosznicka.hyphenate(str))
```
- OUTPUT: `Ge-ne-zyp Ka-pen nie zno-sił nie-wo-li w żad-nej for-mie — od naj-wcześ-niej-sze-go dzie-ciń-stwa o-ka-zy-wał wstręt do niej nie-prze-zwy-cię-żo-ny.`

### syllablecount()
This method returns an int object for the number of syllables in a given string.

```python
str = "Niektórzy ludzie mają pociąg do zbierania osobliwości kosztowniejszych lub mniej kosztownych, na jakie kogo stać"

print(Kokosznicka.syllablecount(str))
```
- OUTPUT: `33`

### normalize()
This method normalizes Polish text into a semi-phonetic stript, effectively eliminating digraphs and disambiguiating the phonetic interpretation.

```python
str = "Mroczne fortece pradawnych Tatr, na których wygrzewa się Król Wężów… wielkie jego cielsko siedem i pół razy owija górę olbrzymkę"

print(Kokosznicka.normalize(str))
```
- OUTPUT: `Mročne fortece pradawnyĥ Tatr, na któryĥ wygžewa ŝĵę Król Wężów… wĵelk̂ĵe jego ĉĵelsko ŝĵedem i pół razy owija górę olbžymkę`

## 🧭 Roadmap
✅ Determining then # of syllables in a word

✅ Phonetic disambiguation with a semi-phonetic script

✅ Hyphenation with a correct # of syllables

✅ Handling hyphenation inside words (biało-czerwony, niby-książka etc.)

✅ Creating a PIP package

❌ Handling exceptions in semivowel formation (nauka, poliester etc.)

❌ Handling exceptions in digraph normalization (marznąć, Tarzan etc.)

❌ Handling affixes in any context (pod-, nad- etc.)

❌ Creating an acronym decoding engine (PWN, PKiN, SJPDor etc.)

... and many more!

> Copyright © Tytus Dunin 2025.