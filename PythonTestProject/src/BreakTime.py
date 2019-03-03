'''
Created on 3 de mar de 2019

@author: bruno
'''
import time #Load the Time Lib
import webbrowser # Load the webbrowser lib

total_break = 3 #Total number of desired breaks
break_count = 0 #Counter for the number of breaks


print("This program started on"+time.ctime()) #Program start time

while(break_count < total_break): #Loop if the number of breaks is smaller the the number of desired breaks
   time.sleep(7200) #The video will start every 2 hours in seconds
   webbrowser.open("https://www.youtube.com/watch?v=fJ9rUzIMcZQ") #Open Bohemian Raspody on YouTube
   break_count = break_count + 1 #Increase the number of breaks by 1 on each loop