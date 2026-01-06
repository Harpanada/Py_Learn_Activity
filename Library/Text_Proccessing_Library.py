import re

Input="Hello for you all in this place hello hello hello"
pola= '^h...o$'


brEak= Input.lower().split()

point=0
for b in brEak:
    result=re.match(pola, b)

    if result:
        point +=2
        print("Matched")
        
    else:
        point -=1
        print("Not Matched")

    print(f"Current Point: {point}")

print(f"Total Point: {point} ")