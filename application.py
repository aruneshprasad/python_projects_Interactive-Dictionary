import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    if w.lower() in data:
        return data[w.lower()]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8))>0:
        yn = input("Did you mean %s instead? Enter y for yes, or n for no: " %get_close_matches(w, data.keys())[0])
        if yn == ("y" or "Y"):
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == ("n" or "N"):
            return "The word doesn't exist."
        else:
            return "We didnot understand your query."
    else:
        return "The word doesn't exist."


word = input("Enter a word: ")

result = translate(word)

if type(result) == list:
    for i in result:
        print(i)
else:
    print(result)
