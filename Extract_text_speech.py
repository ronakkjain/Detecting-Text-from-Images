!pip install pytesseract
!pip install tesseract

# Import required packages 
import cv2 
import pytesseract 

# Mention the installed location of Tesseract-OCR in your system 
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\RONAK JAIN\AppData\Local\Tesseract-OCR\tesseract'

# Read image from which text needs to be extracted 
img = cv2.imread("C:/Users/RONAK JAIN/Pictures/Screenshots/input.jpg") 


# Preprocessing the image starts 

# Convert the image to gray scale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# Performing OTSU threshold 
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 

# Specify structure shape and kernel size. 
# Kernel size increases or decreases the area 
# of the rectangle to be detected. 
# A smaller value like (10, 10) will detect 
# each word instead of a sentence. 
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18)) 

# Appplying dilation on the threshold image 
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 

# Finding contours 
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
												cv2.CHAIN_APPROX_NONE) 

# Creating a copy of image 
im2 = img.copy() 

# A text file is created and flushed 
file = open("sample.txt", "w+") 
file.write("") 
file.close() 

# Looping through the identified contours 
# Then rectangular part is cropped and passed on 
# to pytesseract for extracting text from it 
# Extracted text is then written into the text file 
for cnt in contours: 
	x, y, w, h = cv2.boundingRect(cnt) 
	
	# Drawing a rectangle on copied image 
	rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2) 
	
	# Cropping the text block for giving input to OCR 
	cropped = im2[y:y + h, x:x + w] 
	
	# Open the file in append mode 
	file = open("sample.txt", "a") 
	
	# Apply OCR on the cropped image 
	text = pytesseract.image_to_string(cropped) 
	print(text)
	# Appending the text into file 
	file.write(text) 
	file.write("\n") 
	
	# Close the file 
	file.close 

# Import the required module for text 
# to speech conversion 
from gtts import gTTS 
from playsound import playsound
import os 
mytext = text
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("welcome.mp3")
playsound("welcome.mp3")

# Playing the converted file 
os.system("mpg321 welcome.mp3") 
