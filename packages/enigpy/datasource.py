from os import getenv
<<<<<<< HEAD
import requests
=======
import csv
import json
>>>>>>> fd0fd472b5f388cc0c588a097cc380778468ecf6


map_data = ['A', 'paragraph', 'is', 'a', 'series', 'of', 'related', 'sentences', 'developing', 'a', 'central', 'idea,', 'called', 'the', 'topic.', 'Try', 'to', 'think', 'about', 'paragraphs', 'in', 'terms', 'of', 'thematic', 'unity:', 'a', 'paragraph', 'is', 'a', 'sentence', 'or', 'a', 'group', 'of', 'sentences', 'that', 'supports', 'one', 'central,', 'unified', 'idea.', 'Paragraphs', 'add', 'one', 'idea', 'at', 'a', 'time', 'to', 'your', 'broader', 'argument.']
shuffle_data = [('A', 1), ('paragraph', 9), ('is', 2), ('a', 1), ('series', 6), ('of', 2), ('related', 7), ('sentences', 9), ('developing', 10), ('a', 1), ('central', 7), ('idea,', 5), ('called', 6), ('the', 3), ('topic.', 6), ('Try', 3), ('to', 2), ('think', 5), ('about', 5), ('paragraphs', 10), ('in', 2), ('terms', 5), ('of', 2), ('thematic', 8), ('unity:', 6), ('a', 1), ('paragraph', 9), ('is', 2), ('a', 1), ('sentence', 8), ('or', 2), ('a', 1), ('group', 5), ('of', 2), ('sentences', 9), ('that', 4), ('supports', 8), ('one', 3), ('central,', 8), ('unified', 7), ('idea.', 5), ('Paragraphs', 10), ('add', 3), ('one', 3), ('idea', 4), ('at', 2), ('a', 1), ('time', 4), ('to', 2), ('your', 4), ('broader', 7), ('argument.', 9)]
reduce_data = {1: ['A', 'a', 'a', 'a', 'a', 'a', 'a'], 9: ['paragraph', 'sentences', 'paragraph', 'sentences', 'argument.'], 2: ['is', 'of', 'to', 'in', 'of', 'is', 'or', 'of', 'at', 'to'], 6: ['series', 'called', 'topic.', 'unity:'], 7: ['related', 'central', 'unified', 'broader'], 10: ['developing', 'paragraphs', 'Paragraphs'], 5: ['idea,', 'think', 'about', 'terms', 'group', 'idea.'], 3: ['the', 'Try', 'one', 'add', 'one'], 8: ['thematic', 'sentence', 'supports', 'central,'], 4: ['that', 'idea', 'time', 'your']}

def read_data_from_csv(file_path): 
    with open(file_path, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        content = ""
        for i, line in enumerate(reader):
            temp = " ".join(line).strip()
            content+=temp
        
        wordlist = content.replace("  "," ").split(" ")
        # print(content)
        # print(wordlist)
    return wordlist

def get_map_data():
    # Request to file access end point,
    # Send necessary params by using env.
<<<<<<< HEAD
    url = getenv("ENIGMA_FAE")
    dataFile = requests.get(url, allow_redirects=True)   
=======
    file_path = ""
    wordlist = read_data_from_csv(file_path)
    response_list = []
    for word in wordlist:
        response_list.append(word)
        response_list.append(12)
    print(response_list)
#   ['lgns', 12, 'fg', 12, 'silf', 12, 'as', 12]
    map_data = response_list
>>>>>>> fd0fd472b5f388cc0c588a097cc380778468ecf6
    return map_data

def get_shuffle_data():
    file_path = ""
    wordlist = read_data_from_csv(file_path)
    response_list = []
    for i in range(0,len(wordlist),2):
        temp = (wordlist[i], wordlist[i+1])
        response_list.append(temp)
    print(response_list)
#   [('Priority', 12), ('for', 12)]
    shuffle_data =  response_list
    return shuffle_data

def get_reduce_data():
    file_path = ""
    fObj = open(file_path)
    ogdata = json.load(fObj)
    for i in ogdata:
        print(i, ogdata[i])
    fObj.close()
    return reduce_data
