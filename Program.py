import cv2
import pytesseract
import os
from gtts import gTTS


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

img= cv2.imread('500.jpg')
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#blur = cv2.GaussianBlur(gray,(5,5),0)

#ret, img = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
#
#img = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
 #          cv2.THRESH_BINARY,11,2)
#img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
 #           cv2.THRESH_BINARY,11,2)


print(pytesseract.image_to_string(img))

cv2.imshow('Result',img)
cv2.waitKey(0)


myText = pytesseract.image_to_string(img)
#print(myText)

# Language we want to use 
language = 'en'

output = gTTS(text=myText, lang=language, slow=True)

output.save("output1.mp3")
#output.close()

# Play the converted file 
os.system("start output1.mp3")
