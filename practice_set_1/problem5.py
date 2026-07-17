#label problem4.py

#importing module os
import os

#specifying the path of directories or files
directory_path="/"

#we used os module to list the directory content
contents=os.listdir(directory_path)
      
#we can just simply print print(contents) OR
#loaded and printing each directory taking for 
for item in contents:
    print(item)
