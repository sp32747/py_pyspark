phone=input("give the number :")
strlst=input("give a sentence")
inputList=strlst.split()
print(inputList)
digits_mapping={
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight"

}
output=""
for ch in phone:
    output += digits_mapping.get(ch," !")+" "
print(output)

