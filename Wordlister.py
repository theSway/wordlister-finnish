import random
import xlsxwriter
from xml.dom import minidom

wrds = []
with open('3500.txt', 'r') as file:
    for line in file:
        wrds.append(line)
print(len(wrds))
print(wrds[0])
print(wrds[-1])
xmldoc = minidom.parse('kotus-sanalista_v1.xml')
itemlist = xmldoc.getElementsByTagName('s')
wordlist = []
for item in itemlist:
    sourceword = item.childNodes[0].nodeValue
    wordlist.append(sourceword.upper())

list_of_small_words = []
list_of_medium_words = []
list_of_large_words = []
for word in wordlist:
    if len(word) == 4 or len(word) == 5:
        if "-" not in word:
            list_of_small_words.append(word)
    if len(word) == 6:
        if "-" not in word:
            list_of_medium_words.append(word)
    if len(word) > 6 and len(word) < 15:
        if "-" not in word:
            list_of_large_words.append(word)


small_batch = random.sample(list_of_small_words, 600)
medium_batch = random.sample(list_of_medium_words, 600)
large_batch = random.sample(list_of_large_words, 300)
list_of_small_words = list(set(list_of_small_words).difference(small_batch))
list_of_medium_words = list(set(list_of_medium_words).difference(medium_batch))
list_of_large_words = list(set(list_of_large_words).difference(large_batch))
wrds.extend(small_batch)
wrds.extend(medium_batch)
wrds.extend(large_batch)
wrds = list(set(wrds))

print('WRDS at start: {0}'.format(len(wrds)))
print('Smaller list at start: {0}'.format(len(list_of_small_words)))

while len(wrds) != 4961:
    small_batch = random.choice(list_of_small_words)
    medium_batch = random.choice(list_of_medium_words)
    large_batch = random.choice(list_of_large_words)
    list_of_small_words.remove(small_batch)
    print(len(list_of_small_words))
    list_of_medium_words.remove(medium_batch)
    list_of_large_words.remove(large_batch)
    wrds.append(small_batch)
    if len(wrds) <= 4961:
        wrds.append(medium_batch)
        if len(wrds) <= 4961:
            wrds.append(large_batch)
    list(set(wrds))
    print('WRDS iteration length: {0}'.format(len(wrds)))
    if len(wrds) == 4961:
        break

print(len(wrds))


'''WRITE 'EM TO EXCEL'''

workbook = xlsxwriter.Workbook('All_words.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', 20)

k = 0
while k < 4961:
    worksheet.write("A{0}".format(k), '{0}'.format(wrds[k]))
    k += 1
workbook.close()
