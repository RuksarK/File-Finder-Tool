#sys module is used for command line argument[argv]

from sys import*
import os
import time

def DirectorayTravel(DirName,name):
     print("We are going to scan the directory: ",DirName)

     flag = os.path.isabs(DirName)              #isabs = absolute path(path start with /)

     if flag == False:
          DirName = os.path.abspath(DirName)                #abspath return value is string

     exist = os.path.isdir(DirName)         #to check wheteher dirname is valid or not

     if (exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                 if(fname == name):
                    print("File is Present in the directory with name: ",fname)
            break

     else:
            print("Invalid Path")

 
def main():
    print("-------------Automation Script-------------")
    print("Automation Script Name: ",argv[0])


    if(argv[1]=="-h" or argv[1]=="-H"):       #Flag for displaying help
            print("This automation script is used to perform File automation")
            exit()

    elif(argv[1]=="-u" or argv[1]=="-U"):    #Flag for displaying the usage of script
            print("Usage : Name of Script First_Argument Second_Argument")
            print("Example : Demo.py Marvellous Demo.txt")
            exit()

    if(len(argv) != 3):
        print("Invalid Number of Arguments")
        exit()

    else:
        starttime = time.time()
        DirectorayTravel(argv[1],argv[2])
        endtime = time.time()

        print("The Script took time to execute as ", endtime-starttime)

if __name__ == "__main__":
    main()


