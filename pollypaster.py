# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 23:21:44 2021

@author: shane
"""
import pyperclip
from time import sleep

"""
Needed something quick and dirty to turn an epub I had converted to txt into
chunks with the correct sizing for me to easily paste into Amazon poly and do
so without having to come back adn grab each chunk manually. I'll probably not
use the paster fucntion again, but it's a nice thing to have handy every now
and again when you want to brute force something. 
"""
def stripfile(filename):
    with open(filename,'rb') as doc:
        lines=doc.read()
    
    line=lines.decode().split('\r\n')
    
    length=[]
    nums=0
    for i in line:
        try:
            if sum([sum([len(x) for x in y]) for y in length[nums]])<99000:
                length[nums].append(i)
            else:
                length.append([i])
                nums+=1
        except:
            length.append([i])
            
    strlist=['\n'.join([y for y in x if y!='']) for x in length]
    return(strlist)
def paster(strlist,delay):
    for ix,i in enumerate(strlist):
        print(f'This is chunk {ix}')
        pyperclip.copy(i)
        sleep(delay)
    print("Paste process complete.")