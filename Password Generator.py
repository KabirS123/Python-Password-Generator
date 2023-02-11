import random

alphabet = {
  1: "A",
  2: "B",
  3: "C",
  4: "D",
  5: "E",
  6: "F",
  7: "G",
  8: "H",
  9: "I",
  10: "J",
  11: "K",
  12: "L",
  13: "M",
  14: "N",
  15: "O",
  16: "P",
  17: "Q",
  18: "R",
  19: "S",
  20: "T",
  21: "U",
  22: "V",
  23: "W",
  24: "X",
  25: "Y",
  26: "Z",
  27: "a",
  28: "b",
  29: "c",
  30: "d",
  31: "e",
  32: "f",
  33: "g",
  34: "h",
  35: "i",
  36: "j",
  37: "k",
  38: "l",
  39: "m",
  40: "n",
  41: "o",
  42: "p",
  43: "q",
  44: "r",
  45: "s",
  46: "t",
  47: "u",
  48: "v",
  49: "w",
  50: "x",
  51: "y",
  52: "z",
  53: "1",
  54: "2",
  55: "3",
  56: "4",
  57: "5",
  58: "6",
  59: "7",
  60: "8",
  61: "9",
  62: "0",
  63: "!",
  64: "£",
  65: "$",
  66: "%",
  67: "^",
  68: "&",
  69: "*"
}

length = int(input("How many digits would you like your password to be? \n"))



def passwordgenerator(x):
  global password
  password = ""
  while x != length:
    digit = random.randint(1,69)
    digit = alphabet[digit]
    password = password + digit
    x = x + 1


passwordgenerator(0)
print("This is your password:",password)

def storepassword(password):
  file = open("Passwords.txt","a")
  file.write(password + "\n")
  file.close()

store = str(input("Would you like me to store it for you?"))
if store.lower() == "yes" or store.lower() == "y":
  storepassword(password)


def showpasswords():
  database = open("Passwords.txt","r")
  database = database.read()
  print("These are your passwords: \n" + database)


see = str(input("Would you like to see your passwords? \n"))


if see.lower() == "yes" or see.lower() == "y":
  showpasswords()
