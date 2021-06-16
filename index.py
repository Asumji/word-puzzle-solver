
from PIL import Image
import pytesseract

def spaceitout(string):
    string2 = ""
    for letter in string:
        string2 = string2 + letter + " "
    string2 = string2[:-1]
    return string2


pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files (x86)\Tesseract-OCR\tesseract")
text = pytesseract.image_to_string(Image.open("word.png"))

text = text.replace("\n", "")
text = text.replace("$", "S")
text = text.replace("0", "O")
text = text.replace("1", "I")
text = text.replace("2", "Z")
text = text.lower()

text = text.split(" ")

index = -1
index2 = -1

textSpaced = ""

for letter in text:
    index += 1
    if (len(letter) > 1):
        text[index] = spaceitout(letter)
    textSpaced += letter

textSpaced = spaceitout(textSpaced)
text = textSpaced.split(" ")

wordToFind = input("What word to find? ")

finishedText = ""

foundWord = False

foundText = ""

for letter in text:
    index2 += 1
    word = text[index2:index2 + len(wordToFind)]

    string = ""
    for i in word:
        string += i

    if (foundWord == False):
        if (string == wordToFind):
            foundWord = True
            finishedText = spaceitout(finishedText)
            finishedText = finishedText.upper()
            finishedText += " " + '\033[1m' + string + '\033[0m' + " "
        else:
            finishedText += letter
    else:
        foundText += letter

foundText = spaceitout(foundText)
foundText = foundText.upper()

finishedText += foundText
print(finishedText)
