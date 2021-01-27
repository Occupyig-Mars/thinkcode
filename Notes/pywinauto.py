from pynput.keyboard import Key, Controller
import time     
keyboard= Controller()
import keyboard
from keyboard import press
print ("what is the heading") 
text=input()
heading=text
f = open(heading+".txt", "a")
print ("any sub topic")
text=input()

Nea=0
y=90
x=0
Neb=0

    
print ("what are they")
text=input()
subtopic=text
print ("what is the content")
text=input()
content=text
f.write("\n")
f.write("\n")
f.write("\n")
f.write("Heading-")
f.write(heading)
f.write("\n")
f.write("Subtopic-") 
f.write(subtopic)
f.write("\n")
f.write("\n")
while True:
    content_len= len(content)
    print("till 1 while")
    while True:
        
        content_len=content_len-90
        print(content_len)
        if content_len >= 90:
            Neb += 1
            print("till 2 while")
            while True: 
                if Neb >= Nea:
                    c1=y-90
                    print(c1)
                    c2=x+90
                    print(c2)
                    f.write(content[c1:c2])
                    print(content[c1:c2])
                    f.write("\n")
                    y= y+90
                    print(y)
                    x= x+90
                    print(x)
                    Nea += 1
                    print("till 3 while")
                else:
                    break
        else:
            print("till 2 break")
            break 
    
    print("anything else")
    els=input()
    if els=="yes":
        print("okay")
        content=input()
    else:
        break
               
        