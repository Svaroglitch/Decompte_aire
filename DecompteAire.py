"""
Piece_comptageAir
Creator: Lehag

Ce code créé une image ou il va simuler le jets aléatoire de piece de 20pixel de rayon dans un carré de 1000*1000 pixel.
Il sortira en resultat une image pour visualiser les resultat, ainsi qu'un decompte des pixel "rempli"

"""

import random
from PIL import Image, ImageDraw




####Ecriture de l'image
    # initialisation des parametres de la simulation
        #Indiquez le dossier ou sera enregistrer l'image
outp_dir = "C:\\Users\\Lehag\\OneDrive\\Bureau\\Decomptageduneaire\\Image_test"

raypiece = 100
nobpiece = 20
size_img = 1000

    # Creer une nouvelle image blanche
img_dess = Image.new(mode = "RGB", size = (size_img, size_img),color = (255, 255, 255))

    # [BOUCLE] déssiner les pieces en noir

x = 0
while x < nobpiece :
    posx = float(random.randint(0 , size_img - raypiece))
    posy = float(random.randint(0 , size_img - raypiece))
    print((posx,20),(posy,20))
    draw = ImageDraw.Draw(img_dess)

    draw.ellipse(((posx,posy),(posx+raypiece,posy+raypiece)), fill="#000000", width=raypiece)

    x +=1

    # Affichage de l'image
img_dess.show()


#### Decompte du nombre de pixel noir

nbpixNoir = 0
px = 0
py = 0
while px < size_img :
    while py < size_img :
        colorpix = img_dess.getpixel((px,py))
        if colorpix == (0,0,0):
            nbpixNoir +=1

        py +=1
    py = 0
    px += 1




#### Resultat
img_dess = img_dess.save(outp_dir +"\\Imgnbpix_"+str(nbpixNoir)+".png","PNG")
print(nbpixNoir)
