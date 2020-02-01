#This script helps to convert jpg files to pdf format.

from PIL import Image

image1 = Image.open(r'E:\Cognizant\Rental_agreement\rent_agreement3.jpg')
im1 = image1.convert('RGB')
im1.save(r'E:\Cognizant\Rental_agreement\rent_agreement3.pdf')