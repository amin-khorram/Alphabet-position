import string
def alphabet_position(inp):
    outot=[]
    for i in inp:
        if not i.isalpha():
            pass
        elif i.isalpha():
            i= i.lower()
            index = list(string.ascii_lowercase).index(i)
            outot.append(index+1)
    print(f"'{''.join(str(x) for x in outot)}'")

alphabet_position("The sunset sets at twelve o' clock.")