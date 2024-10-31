import time
from tkinter import PanedWindow
from wsgiref.util import shift_path_info


#
#
# class Door:
#     def __init__(self, color,white,height,):
#         self.color = color
#         self.white = white
#         self.heigt = height
#
#     def open(self):
#         print(f'bacvec:')
#         time.sleep(2)
#         self.close()
#
#     def close(self):
#         print(f'pakvec:')
#
# class Windows(Door):
#     def __init__(self,color,weight,height):
#         super().__init__(color,weight,height)
#
#     def openW(self):
#         print('kisabacvac')
#
# door1 = Door(color='red',white='2',height='3')
# door2 = Door(color='green',white='3',height='4')
# door3 = Door(color='black',white='1',height='5')
# window1 = Windows(color='yellow',weight='2',height='3')
# door1.open()
# door2.open()
# door3.open()
# window1.open()

class Animals:
    def __init__(self,votq,aragutyun,morti,havatarmutyun):
        self.votq = votq
        self.aragutyun = aragutyun
        self.morti = morti
        self.havatarmutyun = havatarmutyun

class Shun(Animals):
    def __init__(self,votq,aragutyun,morti,havatarmutyun,yntani):
        super().__init__(votq,aragutyun,morti,havatarmutyun)
        self.yntani = yntani

    def display_info_shun(self):
        print(f'VOTQ: {self.votq}')
        print(f'ARAGUTYUN: {self.aragutyun}')
        print(f'MORTI: {self.morti}')
        print(f'HAVATARMUTYUN: {self.havatarmutyun}')
        print(f'YNTANI KENDANI: {self.yntani}')

class Katu(Animals):
    def __init__(self,votq,aragutyun,morti,havatarmutyun,mlavel,yntani):
        super().__init__(votq,aragutyun,morti,havatarmutyun)
        self.mlavel = mlavel
        self.yntani = yntani

    def displey_info_katu(self):
        print(f'VOTQ: {self.votq}')
        print(f'ARAGUTYUN: {self.aragutyun}')
        print(f'MORTI: {self.morti}')
        print(f'HAVATARMUTYUN: {self.havatarmutyun}')
        print(f'YNTANI KENDANI: {self.yntani}')

class Gayl(Animals):
    def __init__(self,votq,aragutyun,morti,havatarmutyun,gishatich,yntani):
        super().__init__(votq,aragutyun,morti,havatarmutyun)
        self.yntani = yntani
        self.gishatich = gishatich

    def displey_info_gayl(self):
        print(f'VOTQ: {self.votq}')
        print(f'ARAGUTYUN: {self.aragutyun}')
        print(f'MORTI: {self.morti}')
        print(f'HAVATARMUTYUN: {self.havatarmutyun}')
        print(f'YNTANI KENDANI: {self.yntani}')
        print(f'GISHATICH: {self.gishatich}')


Ans = Animals(votq='4',aragutyun='23KM/J',morti='papuk',havatarmutyun='uni')
Shun1 = Shun(votq='4',aragutyun='23KM/J',morti='papuk',havatarmutyun='uni',yntani='Ayo')
Katu1 = Katu(votq='4',aragutyun='20KM/J',morti='papuk',havatarmutyun='uni',yntani='Ayo',mlavel='Ayo')
Gayl1 = Gayl(votq='4',aragutyun='70KM/J',morti='dziq',havatarmutyun='chuni',yntani='voch',gishatich='Ayo')
Shun1.display_info_shun()
print('------------------')
Katu1.displey_info_katu()
print('------------------')
Gayl1.displey_info_gayl()

