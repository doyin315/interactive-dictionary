import  json
from difflib import get_close_matches
data= json.load(open("076 data.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you mean %s instead? Enter Y if yes,N if no: "%get_close_matches(w,data.keys())[0])
        yn=yn.upper()
        if yn=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return "This word doesn't exist.Please double check it."
        else:
            return "We didn't understand your query."
    else:
        return "This word doesn't exist.Please double check it."
output=translate(input("Enter a word: "))
if type(output) is list:
        for item in output:
            print(item)
else:
        print(output)


