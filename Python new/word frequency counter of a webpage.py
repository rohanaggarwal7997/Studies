import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list=[]
    source_code=requests.get(url).text
    soup =BeautifulSoup(source_code)
    for post_text in soup.find_all('a'):
        try:
            content=post_text.string
            words=content.lower().split()
        except:
            continue
        for each_word in words:
            #print(each_word)
            word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list=[]
    symbols = r"!@#$%^&*()-_=+[{]}\|:;\"\'"
    for word in word_list:
        for i in range(len(symbols)):
            word=word.replace(symbols[i],"")
        if len(word)>0:
        #    print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count={}
    for word in clean_word_list:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    for key,value in sorted(word_count.items(),key=operator.itemgetter(1)):         #itemgetter(1) means sort by value
        print(key,value)



start(r'https://108foundation.wordpress.com/about/')