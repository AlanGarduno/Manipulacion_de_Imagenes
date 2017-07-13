from PIL  import  Image

try:
	img = Image.open("image/im1.jpg")
	img.show()
except IOError:
	print("No es posible abrir la imagen")
