### Find out total number of attributes of an xml passed ########
    # Request XMl:
    # <feed xml:lang='en'>
    #     <title>HackerRank</title>
    #     <subtitle lang='en'>Programming challenges</subtitle>
    #     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    #     <updated>2013-12-25T12:00:00</updated>
    # </feed>

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    # if len(node.attrib)>0:
    #     sum = 1
    # else:
    #     sum=0


    #print(sum)
    # return sum
    #print(len(node.attrib))
    return len(node.attrib) + sum(get_attr_number(child) for child in node)

if __name__ == '__main__':
    a = sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))