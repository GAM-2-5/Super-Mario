import pygame
import Videoplayer

pygame.init()

win=pygame.display.set_mode((960,540),pygame.RESIZABLE) #dimenzije prozora
zaslon_dužina=960
zaslon_visina=540
a=pygame.image.load('Resursi\mario ikona.png')
pygame.display.set_icon(a)
pygame.display.set_caption('Super Mario')
pygame.mixer.init() #zvučni efekti
font=pygame.font.Font('Resursi\SuperMario256.ttf',25)

try:
    pygame.mixer.music.load('Custom\Mario song.mp3')
except:
    pygame.mixer.music.load('Resursi\Zvučni efekti\Mario song.mp3')
    
pygame.mixer.music.play(loops=-1)

try:
    jump=pygame.mixer.Sound('Custom\Mario Jump.wav')
except:
    jump=pygame.mixer.Sound('Resursi\Zvučni efekti\Mario Jump.wav')

try:
    fireball=pygame.mixer.Sound('Custom/fireball.wav')
except:
    fireball=pygame.mixer.Sound('Resursi/Zvučni efekti/fireball.wav')

TIMER_EVENT=pygame.USEREVENT+1 #ubrzavanje gljive
pygame.time.set_timer(TIMER_EVENT,10000)
TIMER_EVENT1=pygame.USEREVENT+2 
pygame.time.set_timer(TIMER_EVENT1,20000)

dužina_slike=50 # sprite-ovi
visina_slike=58

try:
    bullet=pygame.image.load('Custom\metak.png')
except:
    bullet=pygame.image.load('Resursi\Sprites\metak.png')
bullet=pygame.transform.rotozoom(bullet,-90,1)

try:
    skok_desno=pygame.image.load('Custom\mario skače desno.png')
    skok_lijevo=pygame.image.load('Custom\mario skače lijevo.png')
except:
    skok_desno=pygame.image.load('Resursi\Sprites\mario skače desno.png')
    skok_lijevo=pygame.image.load('Resursi\Sprites\mario skače lijevo.png')

try:
    desni_hod=[pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png')] 
    lijevi_hod=[pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png')] 
    idle=pygame.image.load('Custom\mario.png')
    fail=pygame.image.load('Custom\mario.png')
    riba_desno=pygame.image.load('Custom\riba.png')
    riba_lijevo=pygame.image.load('Custom\riba.png')
except:
    desni_hod=[pygame.image.load('Resursi\Sprites\mario 1.png'),pygame.image.load('Resursi\Sprites\mario 2.png'),pygame.image.load('Resursi\Sprites\mario 3.png'),pygame.image.load('Resursi\Sprites\mario 4.png')] 
    lijevi_hod=[pygame.image.load('Resursi\Sprites\mario 1 obrnuti.png'),pygame.image.load('Resursi\Sprites\mario 2 obrnuti.png'),pygame.image.load('Resursi\Sprites\mario 3 obrnuti.png'),pygame.image.load('Resursi\Sprites\mario 4 obrnuti.png')]
    idle=pygame.image.load('Resursi\Sprites\mario 1.png')
    fail=pygame.image.load('Resursi\Sprites\mario fail.png')
    riba_desno=[pygame.image.load('Resursi\Sprites/riba 1 obrnuta.png'),pygame.image.load('Resursi\Sprites/riba 2 obrnuta.png')]
    riba_lijevo=[pygame.image.load('Resursi\Sprites/riba 1.png'),pygame.image.load('Resursi\Sprites/riba 2.png')]

fail=pygame.transform.scale(fail,(dužina_slike+1,visina_slike))

for i in range (len(lijevi_hod)):
    lijevi_hod[i]=pygame.transform.scale(lijevi_hod[i],(dužina_slike,visina_slike))
    desni_hod[i]=pygame.transform.scale(desni_hod[i],(dužina_slike,visina_slike))
    idle=pygame.transform.scale(idle,(dužina_slike,visina_slike))
    skok_desno=pygame.transform.scale(skok_desno,(dužina_slike,visina_slike))
    skok_lijevo=pygame.transform.scale(skok_lijevo,(dužina_slike,visina_slike))

try:
    pozadina=pygame.image.load('Custom\pozadina.png')
except:
    pozadina=pygame.image.load('Resursi\pozadina.png')

move_x=0

brojač_pogodaka=0

clock=pygame.time.Clock()

run=True

class riba(object):

    try:
        riba_desno=pygame.image.load('Custom\riba.png')
        riba_lijevo=pygame.image.load('Custom\riba.png')
    except:
        riba_desno=[pygame.image.load('Resursi\Sprites/riba 1 obrnuta.png'),pygame.image.load('Resursi\Sprites/riba 2 obrnuta.png')]
        riba_lijevo=[pygame.image.load('Resursi\Sprites/riba 1.png'),pygame.image.load('Resursi\Sprites/riba 2.png')]
    
    for j in range (len(riba_desno)):
        riba_desno[j]=pygame.transform.scale(riba_desno[j],(43,44))
        riba_lijevo[j]=pygame.transform.scale(riba_lijevo[j],(43,44))

    def __init__(self,x,y,width,height,kraj):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.put=[x,kraj]
        self.brojač_hoda=0
        self.vel=7
        self.hitbox=(self.x-5,self.y,55,45)

    def crtaj(self,win):
        self.move()
        if self.brojač_hoda+1>=24:
            self.brojač_hoda=0
            
        if self.vel>0:
            win.blit(self.riba_desno[self.brojač_hoda//12],(self.x,self.y))
            self.brojač_hoda+=1
        else:
            win.blit(self.riba_lijevo[self.brojač_hoda//12],(self.x,self.y))
            self.brojač_hoda+=1

        self.hitbox=(self.x+4,self.y+4,42,42)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def move(self):

        if self.vel>0:
            if self.x+self.vel<self.put[1]:
                self.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.brojač_hoda=0
        else:
            if self.x-self.vel>self.put[0]:
                self.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.x+=self.vel
                self.brojač_hoda=0
                
class gljiva(object):

    try:
        gljiva_hod=[pygame.image.load('Custom\gljiva.png'),pygame.image.load('Custom\gljiva.png')]
    except:
        gljiva_hod=[pygame.image.load('Resursi\Sprites\gljiva1.png'),pygame.image.load('Resursi\Sprites\gljiva2.png')]

    for i in range (len(gljiva_hod)):
        gljiva_hod[i]=pygame.transform.scale(gljiva_hod[i],(42,42))
        
    def __init__(self,x,y,width,height,kraj):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.put=[x,kraj]
        self.brojač_hoda=0
        self.vel=4
        self.hitbox=(self.x-5,self.y,55,45)

    def crtaj(self,win):
        self.move()
        if self.brojač_hoda+1>=90:
            self.brojač_hoda=0
            
        if self.vel>0:
            win.blit(self.gljiva_hod[self.brojač_hoda//45],(self.x,self.y))
            self.brojač_hoda+=1
        else:
            win.blit(self.gljiva_hod[self.brojač_hoda//45],(self.x,self.y))
            self.brojač_hoda+=1
        self.hitbox=(self.x+2,self.y+2,38,40)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def move(self):

        if self.vel>0:
            if self.x+self.vel<self.put[1]:
                self.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.brojač_hoda=0
        else:
            if self.x-self.vel>self.put[0]:
                self.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.x+=self.vel
                self.brojač_hoda=0       
                   
class igrač(object):

    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.skok=False
        self.brojač_skoka=16
        self.lijevo=False
        self.desno=False
        self.brojač_hoda=0
        self.stajanje=True
        self.hitbox=(self.x-5,self.y-5,60,65)

    def crtaj(self,win):
        if self.brojač_hoda+1>=40:
            self.brojač_hoda=0

        if not self.skok:
            if not self.stajanje: # hodanje
                if self.lijevo:
                    win.blit(lijevi_hod[self.brojač_hoda//10],(self.x,self.y))
                    self.brojač_hoda+=1
                elif self.desno:
                    win.blit(desni_hod[self.brojač_hoda//10],(self.x,self.y))
                    self.brojač_hoda+=1
            else:
                if self.desno:
                    win.blit(desni_hod[0],(self.x,self.y))
                else:
                    win.blit(lijevi_hod[0],(self.x,self.y))
        if self.skok: #skok
                if Mario.desno:
                    win.blit(skok_desno,(Mario.x,Mario.y))
                else:
                    win.blit(skok_lijevo,(Mario.x,Mario.y))
                    
        self.hitbox=(self.x+2,self.y,47,62)
        #pygame.draw.rect(win,(0,0,255),self.hitbox,2)

    def hit(self): #u slučaju sudara
        win.blit(pozadina,(move_x,0))
        win.blit(neprijatelj.gljiva_hod[1],(neprijatelj.x,neprijatelj.y))
        if riba.vel>0:
            win.blit(riba.riba_desno[1],(riba.x,riba.y))
        else:
            win.blit(riba.riba_lijevo[1],(riba.x,riba.y))
        win.blit(fail,(self.x,self.y-5))
        pygame.display.update()

        try:
            pygame.mixer.music.load('Custom\game over.mp3')
        except:
            pygame.mixer.music.load('Resursi\Zvučni efekti\game over.mp3')
        pygame.mixer.music.play()

        if brojač_pogodaka<=20:
            print('Ukupan broj bodova: {} ... Jadno!' .format(brojač_pogodaka))
        if brojač_pogodaka>20 and brojač_pogodaka<=30:
            print('Ukupan broj bodova: {} ... Meh!' .format(brojač_pogodaka))
        if brojač_pogodaka>30 and brojač_pogodaka<=40:
            print('Ukupan broj bodova: {} ... Nije loše!' .format(brojač_pogodaka))
        if brojač_pogodaka>40 and brojač_pogodaka<=50:
            print('Ukupan broj bodova: {} ... Opa!' .format(brojač_pogodaka))
        if brojač_pogodaka>60:
            print('Ukupan broj bodova: {} ... To legendo!' .format(brojač_pogodaka))

        pygame.time.delay(3050)
        pygame.quit()
               
class projektil(object):  #metci
    def __init__(self,x,y,radius,boja,smjer):
        self.x=x
        self.y=y
        self.radius=radius
        self.boja=boja
        self.smjer=smjer
        self.vel=12*smjer

    def crtaj(self,win):
        win.blit(bullet,(self.x,self.y))

def crtanje():  #crtanje objekata
    global brojač_hoda
    win.blit(pozadina,(move_x,0))#pozadina
    Mario.crtaj(win)
    neprijatelj.crtaj(win)
    riba.crtaj(win)
    for metak in municija:
        metak.crtaj(win)
    pygame.display.update()

Mario=igrač(800,435,35,35)
neprijatelj=gljiva(0,452,32,32,920)
riba=riba(-2750,220,32,32,2670)
municija=[]
shootLoop=1

# glavna petlja
while run:  

    clock.tick(60)   # FPS

    if Mario.hitbox[1]<neprijatelj.hitbox[1]+neprijatelj.hitbox[3] and Mario.hitbox[1]+Mario.hitbox[3]>neprijatelj.hitbox[1]: #sudar
        if Mario.hitbox[0]+Mario.hitbox[2]>neprijatelj.hitbox[0] and Mario.hitbox[0]<neprijatelj.hitbox[0]+neprijatelj.hitbox[2]:
            Mario.hit()
    if Mario.hitbox[1]<riba.hitbox[1]+riba.hitbox[3] and Mario.hitbox[1]+Mario.hitbox[3]>riba.hitbox[1]:
        if Mario.hitbox[0]+Mario.hitbox[2]>riba.hitbox[0] and Mario.hitbox[0]<riba.hitbox[0]+riba.hitbox[2]:
            Mario.hit()

    if shootLoop>0: #ograničavanje pucanja
        shootLoop+=1
    if shootLoop>1:
        shootLoop=0
    
    for metak in municija: # pucanje

        if metak.y-metak.radius<neprijatelj.hitbox[1]+neprijatelj.hitbox[3] and metak.y+metak.radius>neprijatelj.hitbox[1]: #pogodak
            if metak.x+metak.radius>neprijatelj.hitbox[0] and metak.x-metak.radius<neprijatelj.hitbox[0]+neprijatelj.hitbox[2]:
                brojač_pogodaka+=1
                municija.pop(municija.index(metak))

        if metak.y-metak.radius<riba.hitbox[1]+riba.hitbox[3] and metak.y+metak.radius>riba.hitbox[1]: #pogodak
            if metak.x+metak.radius>riba.hitbox[0] and metak.x-metak.radius<riba.hitbox[0]+riba.hitbox[2]:
                brojač_pogodaka+=5
                municija.pop(municija.index(metak))

        if metak.x<960 and metak.x>0:
            metak.x+=metak.vel
        else:
            municija.pop(municija.index(metak))

    tipka=pygame.key.get_pressed() #kontrole

    for event in pygame.event.get(): #zatvaranje prozora
        if event.type==pygame.QUIT or tipka[pygame.K_ESCAPE]:
            run=False
        if event.type==TIMER_EVENT:
            if neprijatelj.vel<0:
                neprijatelj.vel-=4
            else:
                neprijatelj.vel+=4
            
    if tipka[pygame.K_SPACE] and shootLoop==0: # pucanje
        
        if Mario.lijevo:
            smjer=-1
            bullet=pygame.image.load('Resursi\Sprites\metak-lijevo.png')
        else:
            bullet=pygame.image.load('Resursi\Sprites\metak-desno.png')
            smjer=1
        if len(municija)<1:
            fireball.play()
            municija.append(projektil(round(Mario.x+Mario.width//2),round(Mario.y+Mario.height//2),6,(0,0,0),smjer))

    if tipka[pygame.K_m]: # kontrole
        pygame.mixer.music.pause()
  
    if tipka[pygame.K_a] and Mario.x>Mario.vel:
        Mario.x-=Mario.vel
        Mario.lijevo=True
        Mario.desno=False
        Mario.stajanje=False

    elif tipka[pygame.K_d] and Mario.x<zaslon_dužina-Mario.width-Mario.vel:
        Mario.x+=Mario.vel
        Mario.lijevo=False
        Mario.desno=True
        Mario.stajanje=False

    else:
        Mario.stajanje=True
        Mario.brojač_hoda=0
    if tipka[pygame.K_s] and Mario.y!=435:
        Mario.y=435
        Mario.skok=False

    if not Mario.skok:  #skok
        if tipka[pygame.K_w]:
            Mario.skok=True
            Mario.desno=False
            Mario.lijevo=False
            Mario.brojač_hoda=0
            Mario.brojač_skoka=16
            jump.play()

    else:
        if Mario.brojač_skoka>=-16:
            neg=1
            if Mario.brojač_skoka<0:
                neg=-1
            if  Mario.y==262 and Mario.x>=460 and Mario.x<=678:
                Mario.y=262
            else:
                Mario.y-=(Mario.brojač_skoka**2)*0.15*neg
            Mario.brojač_skoka-=1
        else:
            Mario.skok=False
            Mario.bojač_skoka=16
    
    crtanje()
    text = font.render('Broj bodova : {}'.format(brojač_pogodaka), True, (255,0,0))
    win.blit(text,(7,8))
    
    pygame.display.update() #konstantno osvježavanje prozora

pygame.quit() #kraj programa
