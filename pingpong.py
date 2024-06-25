from pygame import *
from random import randint
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    elif hasattr(sys, "_MEIPASS2"):
        return os.path.join(sys._MEIPASS2, relative_path)
    else:
        return os.path.join(os.path.abspath("."), relative_path)

image_folder = resource_path(".")
back=os.path.join(image_folder,'bg.png')
bl=os.path.join(image_folder,'balls.png')
st=os.path.join(image_folder,'stickystick.png')

mnwndw=display.set_mode((600,500))
bg=transform.scale(image.load(back),(600,500))
display.set_caption("pingpong")

class gsprite(sprite.Sprite):
    def __init__(self,pimg,px,py,psped,sizex,sizey):
        sprite.Sprite.__init__(self)
        self.image=transform.scale(image.load(pimg),(sizex,sizey))
        self.sped=psped
        self.rect=self.image.get_rect()
        self.rect.x=px
        self.rect.y=py
    def reset(self):
        mnwndw.blit(self.image,(self.rect.x,self.rect.y))

class Pl1(gsprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y-=self.sped
        if keys[K_s] and self.rect.y<350:
            self.rect.y+=self.sped

class Pl2(gsprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=self.sped
        if keys[K_DOWN] and self.rect.y<350:
            self.rect.y+=self.sped

pl1=Pl1(st,30,200,4,50,150)
pl2=Pl2(st,520,200,4,50,150)
bal=gsprite(bl,200,200,4,50,50)
clock=time.Clock()
fps=60
spedx=3
spedy=3

font.init()
font2=font.Font(None,80)
lssp2=font2.render('YOU LOSE,Pl2',True,(180,0,0))
lssp1=font2.render('YOU LOSE,Pl1',True,(180,0,0))
run=True
finish=False

while run==True:
    for e in event.get():
        if e.type==QUIT:
            run=False
    if finish!=True:
        mnwndw.blit(bg,(0,0))
        
        pl1.update()
        pl2.update()
        bal.rect.x+=spedx
        bal.rect.y+=spedy

        if sprite.collide_rect(pl1,bal) or sprite.collide_rect(pl2,bal):
            spedx=-spedx
            spedy=-spedy
        if bal.rect.y>450 or bal.rect.y<0:
            spedy=-spedy
        if bal.rect.x<0:
            finish=True
            mnwndw.blit(lssp1,(200,200))
            run=False
        if bal.rect.x>600:
            finish=True
            mnwndw.blit(lssp2,(200,200))
            run=False
        bal.reset()
        pl1.reset()
        pl2.reset()
    display.update()
    clock.tick(fps)