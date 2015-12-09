#notepad
import os
def filedisp(name):
    f=open(name,'r+')
    text=f.readlines()
    text=''.join(text)
    print(text)
    f.close()
    
def printmenu() :
    choice=0
    while choice!=1 and choice!=2 and choice!=3  :
        print('Enter your choice\n'
              '1.Write into a new file\n'
              '2.Find and replace a word in a prewritten text\n'
              '3.view the contents of your file')
        choice=input()
        choice=int(choice)
    return choice

cont='y'
while cont == 'y' or cont == 'Y':
    choice=printmenu()
    if choice==1:
        f=open('workfile.txt','a')
        f.close()
        f=open('workfile.txt','r+')
        text=input('Enter the data you want to write to the file...'
                   '"enter" to terminate ')
        f.write(text)
        name=input('What do you want to name your file ? ')
        f.close()
        os.rename('workfile.txt',name)    
    elif choice==2:
        name=input('Enter the filename you want to find and replace ')
        print('Here are the contents ')
        filedisp(name)
        findword=input('Enter the word/substring you want to find ')
        replaceword=input('Enter the word/substring you want to replace ')
        f2=open('tmp.txt','w')
        with open(name,'r') as f:
            text=f.readlines()
            text=''.join(text)
            text=text.replace(findword,replaceword)
            f2.write(text)
        f2.close()
        os.remove(name)
        os.rename('tmp.txt',name)
    elif choice==3:
        name=input('Enter the name of the file you want to view ')
        filedisp(name)
    print('continue?(y/n) ')
    cont=input()
        
        
