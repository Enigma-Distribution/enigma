from os import getenv
import requests
import csv
import json

# def json_data():
#     with open('/runtime/data.json') as json_file:
#         data = json.load(json_file)
#         return data

def read_data(separator=" "):
    url = getenv('ENIGMA_FAE')
    dataFile = requests.get(url, allow_redirects=True)
    data = dataFile.content.decode("utf-8")
    wordlist = data.replace("  "," ").replace("\n", "").split(separator)
    wordlist = [ word.strip() for word in wordlist ]
    return wordlist

def read_data_from_file_map():
    return read_data()

def read_data_from_file_shuffle():
    return read_data(separator=",")


def read_data_from_file_reduce():
    url = getenv('ENIGMA_FAE')
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
