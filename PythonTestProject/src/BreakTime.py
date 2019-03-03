'''
Created on 3 de mar de 2019

@author: bruno
'''
import time
import webbrowser

total_break = 3
break_count = 0


print("This program started on"+time.ctime())

while(break_count < total_break):
   time.sleep(7200)
   webbrowser.open("https://www.youtube.com/watch?v=fJ9rUzIMcZQ")
   break_count = break_count + 1