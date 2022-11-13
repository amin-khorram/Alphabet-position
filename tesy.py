import string
def alphabet_position(text):
    outot=[]
    for i in text:
        if not i.isalpha():
            pass
        elif i.isalpha():
            i= i.lower()
            index = list(string.ascii_lowercase).index(i)
            outot.append(index+1)
    return ' '.join(str(e) for e in outot)

alphabet_position("The sunset sets at twelve o' clock.")
