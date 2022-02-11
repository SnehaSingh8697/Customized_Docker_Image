import os
from os import listdir
from os.path import isfile, join
from collections import Counter
import socket

dirName = '/home/data'
fileNames = [f for f in listdir(dirName) if isfile(join(dirName, f))]


#print (fileNames)

def count_words_in_file(filename):
    num_words = 0
    with open(filename, 'r') as f:
            for line in f:
                words = line.split()
                for w in words:
                    if w.isspace() == False:
                         num_words += 1
    return num_words

count1 = count_words_in_file('/home/data/IF.txt')
count2 = count_words_in_file('/home/data/Limerick-1.txt')
#print(count1)
#print(count2)
total_count = count1 + count2

txt = "Total word count is {}"
#print(txt.format(total_count))

def count_top_3_words(filename):
    a_dictionary = {}
    a_file = open(filename,'r')
    for line in a_file:
            words = line.split(" ")
            for w in words:
                if w.isspace() == False:
                     if w in a_dictionary:
                         a_dictionary[w] += 1
                     else:
                           a_dictionary[w]=1

    k = Counter(a_dictionary)
    high = k.most_common(3)

    return high

most_common_3 = count_top_3_words('/home/data/IF.txt')
#print("Top 3 common words in IF.txt are - ")

#for i in most_common_3:
      #  print(i[0]," :",i[1]," ")

ip_address = socket.gethostbyname(socket.gethostname())
#print(ip_address)

f= open("/home/output/result.txt","w+")

f.write("Names of text files at location /home/data are - \r\n")
for file in fileNames:
    f.write(""+file+"\r\n")

f.write("Total word count is "+str(total_count)+" \n")

f.write("Top 3 words with maximum count are - \r\n")
for i in most_common_3:
    f.write(""+i[0]+" - "+str(i[1])+"\n")

f.write("IP address of machine is "+str(ip_address)+" \n")
f.close()

with open("/home/output/result.txt", 'r') as f:
                for line in f:
                    print(line)

f.close()
		
