'''
Created on 3 de mar de 2019

@author: bruno
'''
import os #Load the OS Lib
def rename_files():
    #Get the file names from folder
    file_list = os.listdir(r"C:\Py_Practice\Prank\prank\prank") #List the files on the folder, r is for raw interpretation of the dir path
    print(file_list)
    saved_path = os.getcwd()
    print("The current directory is"+ saved_path)
    os.chdir(r"C:\Py_Practice\Prank\prank\prank")
    
    #2 Rename all the files listed removing the number from the file names
    for file_name in file_list:
        print("Old file name -"+ file_name)
        print("New file name -"+ file_name.translate(None,"0123456789"))
        os.rename(file_name, file_name.translate(None,"0123456789"))
        os.chdir(saved_path)
rename_files()
