import json
from difflib import SequenceMatcher
from difflib import get_close_matches

word=json.load(open("data.txt"))



def similar(a,b):
    return SequenceMatcher(None,a,b).ratio()
    
    
def translate(w):
    if w in word:
       print(word[w])
    else:
        s=get_close_matches(w,word.keys())[0]
        ratio=int(similar(s,w))
        if(ratio>=0):
            ch=input(print("did yo mean",s,"?(y/n)"))
            if(ch=='y' or ch=='Y'):
                translate(s)
        else:
            print("this word doesn't exist in dictionary")
 
ans='y'

while(ans=='y' or ans=='Y'):
    str=input("enter the word to be searched\n")
    str=str.lower()
    translate(str)
    ans=input("do you want to continue(y/n)?")
        



