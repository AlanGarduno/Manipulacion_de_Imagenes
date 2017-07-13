from PIL  import  Image

try:
	img = Image.open("image/im2.jpg") #abre la imagen, recibe la ruta 
	#print(img.mode) #devuelve en que modo vectorial esta la imagen
	#print(img.getpixel( (100,200) )) #Nuestra los colores de los pixeles
	img.convert("L") #Cambia la imagen a vlanco y negro
	img = img.rotate(40, expand = True) #rota la imagen, recibe cuantos grados se va a rotar, expand, modifica el tamano de la imagen 
	img.save("image/news/im2.jpg") #Guarda la imagen en el disco, recibe la ruta
	
	img.show() #abre la imagen 
except IOError:
	print("No es posible abrir la imagen")
