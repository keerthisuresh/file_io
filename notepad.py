#notepad
import os
def printmenu() :
    choice=0
    while choice!=1 and choice!=2 and choice!=3  :
        print('Enter your choice\n1.Write into a new file\n2.Find and replace a word in a prewritten text\n3.view the contents of your file')
        choice=input()
        choice=int(choice)
    return choice
    


cont='y'
while cont=='y' or cont=='Y':
    choice=printmenu()
    if choice==1:
        f=open('workfile.txt','w')
        f.close()
        f=open('workfile.txt','r+')
        print('Enter the data you want to write to the file..."enter" to terminate')
        text=input()
        f.write(text)
        print('What do you want to name your file ?')
        name=input()
        f.close()
        os.rename('workfile.txt',name)    
    if choice==2:
     print('Enter the file u wanna find and replace')
     name=input()
     f=open(name,'r+')
     print('here are the contents')
     text=f.readlines()
     print(text)
     f.close()
     print('Enter the word u wanna find ')
     findword=input()
     print('Enter the word u wanna replace ')
     replaceword=input()
     f2=open('tmp.txt','w')
     with open(name,'r') as f:
        for line in f:
            for word in line.split():
               if(word==findword):
                   f2.write(replaceword+' ')
               else:
                f2.write(word+' ')
     f2.close()
     os.remove(name)
     os.rename('tmp.txt',name)
    if choice==3:
       print('Enter the name of the file u wanna see')
       name=input()
       f=open(name,'r')
       text=f.readlines()
       print(text)
       
       
    print('continue?(y/n)')
    cont=input()
        
        
