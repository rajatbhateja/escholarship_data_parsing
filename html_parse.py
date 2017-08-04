import glob
import os.path
from bs4 import BeautifulSoup
import csv
import re
import psycopg2
from psycopg2.extensions import *

# local directory path where the html files are stored
path = 'C:/Users/USER/Documents/Fellowship/etd-data/etd-data/index-files'


l = []
list_text = []
Dest = {}
final_result = ""
list_text2 = []

cedilla2latin = [[u'Á', u'A'], [u'á', u'a'], [u'Č', u'C'], [u'č', u'c'], [u'Š', u'S'], [u'š', u's'], [u'è', u'e'], [u'é', u'e'], [u'ê', u'e'], [u'ë', u'e'], [u'ç', u'c'], [u'à', u'a'], [u'â', u'a'], [u'ù', u'u'], [u'û', u'u'], [u'ü', u'u'], [u'ÿ', u'y']]
tr = dict([(a[0], a[1]) for (a) in cedilla2latin])

def transliterate(line):
    new_line = ""
    for letter in line:
        if letter in tr:
            new_line += tr[letter]
        else:
            new_line += letter
    return new_line

# traversing through the file names to get the pid from file name and text in the file using Beautiful Soup
for file_name in glob.glob(os.path.join(path, "*.html")):
    with open(file_name, encoding="utf8") as html_file:
        soup = BeautifulSoup(html_file, "lxml")
        visible_text = soup.getText()
        l.append(visible_text)
        start = '\\'
        end = '__'
        result = file_name[file_name.find(start)+1:file_name.find(start)+7]
        for char in result:
            if char in "_":
                final_result = result.replace(char, '')
            else:
                final_result = result
        Dest = dict(pid=final_result, content=visible_text)
        line = Dest['content']
        punctuation = "–~`'!@#$%^&*,;.?:\/]}[{()\"_\\>|<+=\n\r"
        replace = "                                   "
        filter = str.maketrans(punctuation, replace)
        line = line.translate(filter)
        # remove digits with regex
        line = re.sub("(^|\W)\d+($|\W)", " ", line)
        #remove http links
        line = re.sub(r'https?:\/\/.*[\r\n]*', '', line, flags=re.MULTILINE)
        # transliterate to Latin characters
        line = transliterate(line)
        line = line.lower()
        line = line.strip(' ')
        # print(line)
        Dest['content'] = line
        list_text.append(Dest)


#list_text is the list of dictionaries which contains the pids and corresponding parsed html text.
print(list_text)
