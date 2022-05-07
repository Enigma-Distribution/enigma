from os import getenv
import requests
import csv
import json

def json_data():
    with open('/runtime/data.json') as json_file:
        data = json.load(json_file)
        return data

map_data = ['A', 'paragraph', 'is', 'a', 'series', 'of', 'related', 'sentences', 'developing', 'a', 'central', 'idea,', 'called', 'the', 'topic.', 'Try', 'to', 'think', 'about', 'paragraphs', 'in', 'terms', 'of', 'thematic', 'unity:', 'a', 'paragraph', 'is', 'a', 'sentence', 'or', 'a', 'group', 'of', 'sentences', 'that', 'supports', 'one', 'central,', 'unified', 'idea.', 'Paragraphs', 'add', 'one', 'idea', 'at', 'a', 'time', 'to', 'your', 'broader', 'argument.']
shuffle_data = [('A', 1), ('paragraph', 9), ('is', 2), ('a', 1), ('series', 6), ('of', 2), ('related', 7), ('sentences', 9), ('developing', 10), ('a', 1), ('central', 7), ('idea,', 5), ('called', 6), ('the', 3), ('topic.', 6), ('Try', 3), ('to', 2), ('think', 5), ('about', 5), ('paragraphs', 10), ('in', 2), ('terms', 5), ('of', 2), ('thematic', 8), ('unity:', 6), ('a', 1), ('paragraph', 9), ('is', 2), ('a', 1), ('sentence', 8), ('or', 2), ('a', 1), ('group', 5), ('of', 2), ('sentences', 9), ('that', 4), ('supports', 8), ('one', 3), ('central,', 8), ('unified', 7), ('idea.', 5), ('Paragraphs', 10), ('add', 3), ('one', 3), ('idea', 4), ('at', 2), ('a', 1), ('time', 4), ('to', 2), ('your', 4), ('broader', 7), ('argument.', 9)]
reduce_data = {1: ['A', 'a', 'a', 'a', 'a', 'a', 'a'], 9: ['paragraph', 'sentences', 'paragraph', 'sentences', 'argument.'], 2: ['is', 'of', 'to', 'in', 'of', 'is', 'or', 'of', 'at', 'to'], 6: ['series', 'called', 'topic.', 'unity:'], 7: ['related', 'central', 'unified', 'broader'], 10: ['developing', 'paragraphs', 'Paragraphs'], 5: ['idea,', 'think', 'about', 'terms', 'group', 'idea.'], 3: ['the', 'Try', 'one', 'add', 'one'], 8: ['thematic', 'sentence', 'supports', 'central,'], 4: ['that', 'idea', 'time', 'your']}

def read_data():
    data = json_data()
    url = data['ENIGMA_FAE']
    dataFile = requests.get(url, allow_redirects=True)
    data = dataFile.content.decode("utf-8")
    wordlist = data.replace("  "," ").replace("\n", "").split(" ")
    return wordlist

def read_data_from_file_map():
    return read_data()

def read_data_from_file_shuffle():
    return read_data()


def read_data_from_file_reduce():
    data = json_data()
    url = data['ENIGMA_FAE']
    dataFile = requests.get(url, allow_redirects=True)
    return dataFile.content.decode("utf-8")

def get_map_data():  
    wordlist = read_data_from_file_map()
    response_list = []
    for word in wordlist:
        response_list.append(word)
    map_data = response_list
    return map_data

def get_shuffle_data():
    wordlist = read_data_from_file_shuffle()
    response_list = []
    for i in range(0,len(wordlist),2):
        temp = (wordlist[i], wordlist[i+1])
        response_list.append(temp)
    shuffle_data =  response_list
    return shuffle_data

def get_reduce_data():
    json_text = read_data_from_file_reduce()
    reduce_data = json.loads(json_text)
    return reduce_data
