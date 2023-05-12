import random
from PIL import Image
class Perlin:
    def __init__(self,Longueur,Largeur,file):
        self.Tableau = Image.new("L", (Longueur*16,Largeur*16), color=0)
        self.file = file

    def ChangePixel(self,xy,value):
        '''Change la couleur du pixel(0 à 255) au coordonné xy(tuple)'''
        self.Tableau.putpixel(xy,value)

    def Polissage(self,xy1,xy2):
        '''Fait une variation de couleur de xy1 à xy2 que si les points sont alligniés. xy1<xy2'''#faire quand la différence de couleur et plus petite que la différence distance
        if xy1[1] == xy2[1] and xy1[0]!=xy2[0]:
            diff = abs(xy1[0]-xy2[0])
            diffColor = abs(self.Tableau.getpixel(xy1)-self.Tableau.getpixel(xy2))//diff
            print(self.Tableau.getpixel(xy1),self.Tableau.getpixel(xy2))
            if self.Tableau.getpixel(xy1) > self.Tableau.getpixel(xy2):
                for d in range(1,diff):
                    self.ChangePixel((xy1[0]+d,xy1[1]),(self.Tableau.getpixel(xy1)+diffColor*d))
                    print((xy1[0]+d,xy1[1]),(self.Tableau.getpixel(xy1)-diffColor*d))
            else:
                for d in range(1,diff):
                    self.ChangePixel((xy1[0]+d,xy1[1]),(self.Tableau.getpixel(xy1)+diffColor*d))
                    print((xy1[0]+d,xy1[1]),(self.Tableau.getpixel(xy1)+diffColor*d))
                

        if xy1[1] != xy2[1] and xy1[0]==xy2[0]:
            diff = abs(xy1[1]-xy2[1])
            diffColor = abs(self.Tableau.getpixel(xy1)-self.Tableau.getpixel(xy2))//diff
            print(self.Tableau.getpixel(xy1),self.Tableau.getpixel(xy2))
            if self.Tableau.getpixel(xy1) > self.Tableau.getpixel(xy2):
                for d in range(1,diff):
                    self.ChangePixel((xy1[0],xy1[1]+d),(self.Tableau.getpixel(xy1)+diffColor*d))
                    print((xy1[0],xy1[1]+d),(self.Tableau.getpixel(xy1)-diffColor*d))
            else:
                for d in range(1,diff):
                    self.ChangePixel((xy1[0],xy1[1]+d),(self.Tableau.getpixel(xy1)+diffColor*d))
                    print((xy1[0],xy1[1]+d),(self.Tableau.getpixel(xy1)+diffColor*d))
            
    def Point(self,distance):
        '''Pose les points à distance'''
        for x in range(0,self.Tableau.height,distance):
            for y in range(0,self.Tableau.width,distance):
                self.ChangePixel((x,y),random.randint(0,255))
        self.PolissagePoint(distance)
    def PolissagePoint(self,distance):
        '''Utilise la fonction polissage toute les distances'''
        for x in range(0,self.Tableau.height-distance,distance):
            for y in range(0,self.Tableau.width-distance,distance):
                print(x,y)
                self.Polissage((x,y),(x+distance,y))
                self.Polissage((x,y),(x,y+distance))
                
    def save(self):
        '''sauvegarde dans le fichier où est le programme en .PNG'''
        self.Tableau.save(self.file+".png")


Perlin = Perlin(16,16,"Perlin")
##Perlin.ChangePixel((15,45),245)
##Perlin.ChangePixel((30,45),60)
##Perlin.Polissage((15,45),(30,45))
Perlin.Point(15)

Perlin.save()
