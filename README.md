# Detecting-Text-and-TexttoSpeech
This project is about extracting text from images and speaking up that text for the childrens to understand properly. 

# Procedure:

For extracting text -->
1) Import libraries
2) Load the model
3) Read the image
4) Convert the image from RGB to Grayscale
5) Perform thresholding
6) Create and mention size of bounding box
7) Apply Dilation(Dilation adds pixels to the boundaries of objects in an image)
8) Find contours(boundaries of the object or text)
9) Creating a text file to store text extracted from image
10) Looping through all the contours and bounding box is cropped and passed on to pytesseract for extracting text from it. Extracted text is then written into the text file.

For text-to-speech -->
11) import libraries
12) assign the text into a variable
13) mention the language
14) Save and play

Print('Thank You')


