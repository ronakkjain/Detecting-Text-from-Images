# Detecting-Text-and-TexttoSpeech
This project is about extracting text from images and speaking up that text for the childrens to understand properly. 

# Procedure:

For extracting text -->
Import libraries
Load the model
Read the image
Convert the image from RGB to Grayscale
Perform thresholding
Create and mention size of bounding box
Apply Dilation(Dilation adds pixels to the boundaries of objects in an image)
Find contours(boundaries of the object or text)
Creating a text file to store text extracted from image
Looping through all the contours and bounding box is cropped and passed on to pytesseract for extracting text from it. Extracted text is then written into the text file.

For text-to-speech -->
import libraries
assign the text into a variable
mention the language
Save and play

Print('Thank You')


