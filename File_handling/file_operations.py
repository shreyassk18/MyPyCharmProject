# r - open file to read only
# w - open file for writing, if file already exists, removes all data in the file and writes.
# a - open a file and append data at EOF

#Write data into a file

f = open(r"C:\Users\shreyas.kittur\PycharmProjects\Baisc_Python\File_handling\MyFile.txt", "w")
f.write("Hello\nWelcome to python world\n")
f.close()

#Read data from a file
f1 = open(r"C:\Users\shreyas.kittur\PycharmProjects\Baisc_Python\File_handling\MyFile.txt", "r")
#print(f1.read())   #Reads entire data from a file

#print(f1.read(10))  #Read 10 characters from a file

#print(f1.readlines())    #Reads entrire file and returns in an array format

print(f1.readline())    #Reads first line of a file
f1.close()

#Appending data to a file
f2 = open(r"C:\Users\shreyas.kittur\PycharmProjects\Baisc_Python\File_handling\MyFile.txt", "a")
f2.write("This is an example for file handling in python\n")

f2.close()

#Read data using for loop
f3 = open(r"C:\Users\shreyas.kittur\PycharmProjects\Baisc_Python\File_handling\MyFile.txt", "r")
for i in f3:
    print(i)

f3.close()