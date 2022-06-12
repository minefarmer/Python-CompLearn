'''                 SYNTAX TO OPEN FILE
f = open("myfile.txt')
f = open("myfile.txt","rt")
If the file I'm trying to interaact with is in the same directory I'm working with in my python file. then there is no nee to speify the absolute path.

    If not in the same directory, then I need to specify the path and it has to be double slashes.
f = open(c:\\myfolders\myfile.txt)


'''
f = open("quotes.txt")

print(f.readable())

