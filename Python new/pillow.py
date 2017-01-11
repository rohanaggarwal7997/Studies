from PIL import Image

img=Image.open("2.jpg")
print(img.size)
print(img.format)
#img.show()

area =(100,100,230,165)
print(area)
cropped_img=img.crop(area)
cropped_img.show()

im2=Image.open('1.jpg')
area=(100,100,150,150)
im2.paste(img,area)
im2.show()