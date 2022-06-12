import json
from difflib import get_close_matches

data = json.load(open("data.json"))
print("enter a word : ")
x = input()

def look(word):
    word = word.lower()
    close = get_close_matches(word, data.keys())
    if word in data:
        if len(data[word])>1:
            for x in range(len(data[word])):
                print("-->",data[word][x])
        else:
            print("-->",data[word][0])
    elif word.capitalize() in data:
        word = word.capitalize()
        if len(data[word])>1:
            for x in range(len(data[word])):
                print("-->",data[word][x])
        else:
            print("-->",data[word][0])
    elif word.upper() in data:
        word = word.upper()
        if len(data[word])>1:
            for x in range(len(data[word])):
                print("-->",data[word][x])
        else:
            print("-->",data[word][0])
    elif len(close)>0:
        print("did you mean",close[0],"? enter Y if yes / N if no : ")
        i = input()
        if i=="Y" or i=="y":
            cl = close[0]
            if len(data[cl])>1:
                for x in range(len(data[cl])):
                    print("-->",data[cl][x])
            else:
                print(data[cl])
        elif i=="n" or i=="N":
            print("word not found")
        else:
            print("wrong input!!..please run the program again...")
    else:
        print("word not found")
if __name__=="__main__":
    look(x)