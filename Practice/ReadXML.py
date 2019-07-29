import os
from xml.etree import ElementTree

path='F:/Python/TextFiles/Empdetails.xml'
doc=ElementTree.parse(path)

ele = doc.findall('Emp')
print(ele[1].find('Name').text)    #To read a single element
for i in ele:                       #To read all elements
    ID = i.find('ID').text
    Name = i.find('Name').text
    Location= i.find('Location').text

    print('ID ''{} Name:{} Location: {}'.format(ID,Name,Location))