'''
Created on 7 de mar de 2019

@author: bruno
'''
import urllib.request
def read_text():
    quotes = open("C:\Py_Practice\quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+ urllib.parse.urlencode([('q', text_to_check)]))
    output = str(connection.read())
    connection.close()
    if "true" in output:
        print("Profanity ALert!")
    elif "false" in output:
        print("This document have no course words!")
    else:
        print("Could not scan the document!")
  
read_text()