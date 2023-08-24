import getpass #gives you the username (dell here) 
import os 
import cProfile
from os import listdir #return list of all files and folders in the directory 
from os.path import isfile,join
print(getpass.getuser())
print(os.environ) #This prints a dictionary that contains all the environment variables 
print(os.environ['PATH']) #This prints the value of the PATH environment variable
#print(os.environ['HOME']) #home directory of the current user 
for key, value in os.environ.items():
    print(f"{key}: {value}")

#{key} and {value} are placeholder for key and value will be replacesd after the execution 
#: used to seperate between key and value 
#str(age) to converte age to string 
#f"Hello, {name}! You are {age} years old." and "Hello, " + name + "! You are " + str(age) + " years old."

def sum():
    print(1,7)
cProfile.run('sum()')    

files_list = [f for f in listdir('/users') if isfile(join('/users',f))]
print(files_list)
#This is called a list comprehension in Python
#join make f into users /users/f
#sys.version to get the version of your python 
"sys.version_information"
#listdir('/users') would return a list containing the names of all files and directories in the '/users' directory.
#f in the list comprehension is simply a variable name chosen to represent each item in the list during the iteration
#f is for file
