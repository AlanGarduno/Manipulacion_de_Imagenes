from PIL  import  Image

try:
	img = Image.open("image/im1.jpg")
	print(img.mode)
	print(img.getpixel( (100,200) ))

	img = img.convert("L")
	#img.show()
except IOError:
	print("No es posible abrir la imagen")
