import pygame
bruh=open('Resursi\Rekordi.txt')
if int(bruh.read())==0:
  import Videoplayer
else:
  fortnite=0

pygame.init()

win=pygame.display.set_mode((960,540),pygame.RESIZABLE) #dimenzije prozora
zaslon_dužina=960
zaslon_visina=540
a=pygame.image.load('Resursi\mario ikona.png')
pygame.display.set_icon(a)
pygame.display.set_caption('Super Mario | Python')
pygame.mixer.init() #zvučni efekti
izbornik=pygame.image.load('Resursi\izbornik.png')
TIMER_EVENT=pygame.USEREVENT+1 #ubrzavanje gljive
pygame.time.set_timer(TIMER_EVENT,10000)
TIMER_EVENT1=pygame.USEREVENT+2
pygame.time.set_timer(TIMER_EVENT1,20000)
dužina_slike=50 # sprite-ovi
visina_slike=58
istina=True
move_x=0
brojač_pogodaka=0

clock=pygame.time.Clock()

run=True

class riba(object):
  
    def __init__(self,x,y,width,height,kraj):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.put=[x,kraj]
        self.brojač_hoda=0
        self.vel=7
        self.hitbox=(self.x-5,self.y,55,45)
    if istina:
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
            if super_mario:
                self.hitbox=(self.x+4,self.y+4,42,42)
            else:
                if self.vel>0:
                    self.hitbox=(self.x+7,self.y+4,120,40)
                else:
                    self.hitbox=(self.x+1,self.y+4,120,40)
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
        
    def __init__(self,x,y,width,height,kraj):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.put=[x,kraj]
        self.brojač_hoda=0
        self.vel=5
        self.hitbox=(self.x-5,self.y,55,45)

    def crtaj(self,win):
        self.move()
        if self.brojač_hoda+1>=90:
            self.brojač_hoda=0
        if super_mario:   
            if self.vel>0:
                win.blit(self.gljiva_hod[self.brojač_hoda//45],(self.x,self.y))
                self.brojač_hoda+=1
            else:
                win.blit(self.gljiva_hod[self.brojač_hoda//45],(self.x,self.y))
                self.brojač_hoda+=1
        else:
            if self.vel>0:
                win.blit(self.gljiva_hod[1],(self.x,self.y))
            else:
                win.blit(self.gljiva_hod[0],(self.x,self.y))

        if super_mario:
            self.hitbox=(self.x+2,self.y+2,38,40)
        else:
            self.hitbox=(self.x+6,self.y+2,40,85)
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
        if self.brojač_hoda>=24:
            self.brojač_hoda=0

        if not self.skok:
            if not self.stajanje: # hodanje
                if self.lijevo:
                    win.blit(lijevi_hod[self.brojač_hoda//6],(self.x,self.y))
                    self.brojač_hoda+=1
                elif self.desno:
                    win.blit(desni_hod[self.brojač_hoda//6],(self.x,self.y))
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
        if super_mario:          
            self.hitbox=(self.x+2,self.y,47,62)
        else:
            self.hitbox=(self.x+2,self.y,42,87)
        #pygame.draw.rect(win,(0,0,255),self.hitbox,2)

    def hit(self): #u slučaju sudara
        if super_mario:
            font=pygame.font.Font('Resursi/SuperMario256.ttf',32)
        else:
            font=pygame.font.Font('Resursi/HeadlinerNo45.ttf',60)
        pygame.mixer.pause()
        win.blit(pozadina,(move_x,0))
        win.blit(neprijatelj.gljiva_hod[1],(neprijatelj.x,neprijatelj.y))
        if riba.vel>0:
            win.blit(riba.riba_desno[0],(riba.x,riba.y))
        else:
            win.blit(riba.riba_lijevo[0],(riba.x,riba.y))
        win.blit(fail,(self.x,self.y-10))       

        try:
            pygame.mixer.music.load('Custom\game over.mp3')
        except:
            if super_mario:
                pygame.mixer.music.load('Resursi\Zvučni efekti\Mario\game over.mp3')
            else:
               pygame.mixer.music.load('Resursi\Zvučni efekti\Blitzkrieg/rifle.wav')
        pygame.mixer.music.play()
        f=open('Resursi\Rekord.txt','r')
        x=f.read()
        f.close()
        
        if int(x)>int(brojač_pogodaka):
            if brojač_pogodaka<=20:
                text = font.render('Ukupan broj bodova : {}  Jadno!'.format(brojač_pogodaka), True, (255,0,0))
            if brojač_pogodaka>20 and brojač_pogodaka<=30:
                text = font.render('Ukupan broj bodova : {}  Meh!' .format(brojač_pogodaka), True, (255,0,0))
            if brojač_pogodaka>30 and brojač_pogodaka<=45:
                text = font.render('Ukupan broj bodova : {}  Nije loše!' .format(brojač_pogodaka), True, (255,0,0))
            if brojač_pogodaka>45 and brojač_pogodaka<=60:
                text = font.render('Ukupan broj bodova : {}  Opa!' .format(brojač_pogodaka), True, (255,0,0))
            if brojač_pogodaka>60:
                text = font.render('Ukupan broj bodova : {}  To legendo!' .format(brojač_pogodaka), True, (255,0,0))
        else:
            text = font.render('Ukupan broj bodova : {} Novi rekord!'.format(brojač_pogodaka), True, (255,0,0))
            f=open('Resursi\Rekord.txt','w')
            f.write('{}' .format(brojač_pogodaka))
            f.close()
        if super_mario:
            win.blit(text,(160,180))
        else:
            win.blit(text,(200,180))
        pygame.display.update()
        if super_mario:
            pygame.time.delay(3000)
        else:
            pygame.time.delay(1850)
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
    if istina:
        win.blit(izbornik,(0,0))
        gljiva.vel=0
        Mario.vel=0
    else:
        win.blit(pozadina,(0,0))      
        text = font.render('Broj bodova : {}'.format(brojač_pogodaka), True, (255,0,0))
        Mario.crtaj(win)
        neprijatelj.crtaj(win)
        riba.crtaj(win)
        win.blit(text,(10,9))
        for metak in municija:
            metak.crtaj(win)
        gljiva.vel=5      
        Mario.vel=4
    pygame.display.update()

Mario=igrač(800,435,35,35)
neprijatelj=gljiva(0,452,32,32,920)
riba=riba(-3550,220,32,32,3550)
municija=[]
shootLoop=1
brojač=0
brojač2=0

if istina:
    pygame.mixer.music.load('Resursi\Zvučni efekti\menu.mp3')
    pygame.mixer.music.play(loops=-1)
if not istina:
    pygame.mixer.music.pause()
    
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
        if event.type==pygame.QUIT or tipka[pygame.K_q]:
            run=False
        if event.type==TIMER_EVENT:
            if neprijatelj.vel<0:
                neprijatelj.vel-=3
            else:
                neprijatelj.vel+=3
            riba.put[0]+=200
            riba.put[1]-=200
        if event.type==TIMER_EVENT1:
            brojač+=1

    if riba.x>-1100 and riba.x<2060:
        if not super_mario and brojač%2==0:
            avion=pygame.mixer.Sound('Resursi\Zvučni efekti\Blitzkrieg/avion.wav')
            avion.play()
            brojač+=1
           
    if tipka[pygame.K_LEFT] and brojač2==0:
        brojač2+=1
        font=pygame.font.Font('Resursi\SuperMario256.ttf',25)
        super_mario=True
        try:
            gljiva.gljiva_hod=[pygame.image.load('Custom\gljiva.png'),pygame.image.load('Custom\gljiva.png')]
        except:
            gljiva.gljiva_hod=[pygame.image.load('Resursi\Sprites\Mario\gljiva1.png'),pygame.image.load('Resursi\Sprites\Mario\gljiva2.png')]
    
        for i in range (len(gljiva.gljiva_hod)):
            gljiva.gljiva_hod[i]=pygame.transform.scale(gljiva.gljiva_hod[i],(42,42))
        istina=False
        try:
            riba.riba_desno=pygame.image.load('Custom\riba.png')
            riba.riba_lijevo=pygame.image.load('Custom\riba.png')
        except:
            riba.riba_desno=[pygame.image.load('Resursi\Sprites/Mario/riba 1 obrnuta.png'),pygame.image.load('Resursi\Sprites/Mario/riba 2 obrnuta.png')]
            riba.riba_lijevo=[pygame.image.load('Resursi\Sprites/Mario/riba 1.png'),pygame.image.load('Resursi\Sprites/Mario/riba 2.png')]
        for j in range (len(riba.riba_desno)):
            riba.riba_desno[j]=pygame.transform.scale(riba.riba_desno[j],(43,44))
            riba.riba_lijevo[j]=pygame.transform.scale(riba.riba_lijevo[j],(43,44))
        try:
            pygame.mixer.music.load('Custom\Mario song.mp3')
        except:
            pygame.mixer.music.load('Resursi\Zvučni efekti\Mario\Mario song.mp3')
        try:
            jump=pygame.mixer.Sound('Custom\Mario Jump.wav')
        except:
            jump=pygame.mixer.Sound('Resursi\Zvučni efekti\Mario\Mario Jump.wav')

        try:
            fireball=pygame.mixer.Sound('Custom/fireball.wav')
        except:
            fireball=pygame.mixer.Sound('Resursi/Zvučni efekti/Mario/fireball.wav')

        try:
            skok_desno=pygame.image.load('Custom\mario.png')
            skok_lijevo=pygame.image.load('Custom\mario.png')
        except:
            skok_desno=pygame.image.load('Resursi\Sprites\Mario\mario skače desno.png')
            skok_lijevo=pygame.image.load('Resursi\Sprites\Mario\mario skače lijevo.png')

        try:
            desni_hod=[pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png')] 
            lijevi_hod=[pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png')]
            idle=pygame.image.load('Custom\mario.png')
            fail=pygame.image.load('Custom\mario.png')
        except:
            desni_hod=[pygame.image.load('Resursi\Sprites\Mario\mario 1.png'),pygame.image.load('Resursi\Sprites\Mario\mario 2.png'),pygame.image.load('Resursi\Sprites\Mario\mario 3.png'),pygame.image.load('Resursi\Sprites\Mario\mario 4.png')] 
            lijevi_hod=[pygame.image.load('Resursi\Sprites\Mario\mario 1 obrnuti.png'),pygame.image.load('Resursi\Sprites\Mario\mario 2 obrnuti.png'),pygame.image.load('Resursi\Sprites\Mario\mario 3 obrnuti.png'),pygame.image.load('Resursi\Sprites\Mario\mario 4 obrnuti.png')]
            idle=pygame.image.load('Resursi\Sprites\Mario\mario 1.png')
            fail=pygame.image.load('Resursi\Sprites\Mario\mario fail.png')

        try:
            riba_desno=pygame.image.load('Custom\riba.png')
            riba_lijevo=pygame.image.load('Custom\riba.png')
        except:
            riba_desno=[pygame.image.load('Resursi\Sprites/Mario/riba 1 obrnuta.png'),pygame.image.load('Resursi\Sprites/Mario/riba 2 obrnuta.png')]
            riba_lijevo=[pygame.image.load('Resursi\Sprites/Mario/riba 1.png'),pygame.image.load('Resursi\Sprites/Mario/riba 2.png')]

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
        pygame.mixer.music.play(loops=-1)

    if tipka[pygame.K_RIGHT] and brojač2==0:
        brojač2+=1
        dužina_slike=45
        visina_slike=90
        font=pygame.font.Font('Resursi\HeadlinerNo45.ttf',40)
        super_mario=False
        try:
            gljiva.gljiva_hod=[pygame.image.load('Custom\gljiva.png'),pygame.image.load('Custom\gljiva.png')]
        except:
            gljiva.gljiva_hod=[pygame.image.load('Resursi\Sprites\Blitzkrieg\gljiva1.png'),pygame.image.load('Resursi\Sprites\Blitzkrieg\gljiva2.png')]
        neprijatelj.y=400
        Mario.y=400
        riba.y=190
        for i in range (len(gljiva.gljiva_hod)):
            gljiva.gljiva_hod[i]=pygame.transform.scale(gljiva.gljiva_hod[i],(55,87))
        try:
            riba.riba_desno=pygame.image.load('Custom\riba.png')
            riba.riba_lijevo=pygame.image.load('Custom\riba.png')
        except:
            riba.riba_desno=[pygame.image.load('Resursi\Sprites/Blitzkrieg/riba 1 obrnuta.png'),pygame.image.load('Resursi\Sprites/Blitzkrieg/riba 2 obrnuta.png')]
            riba.riba_lijevo=[pygame.image.load('Resursi\Sprites/Blitzkrieg/riba 1.png'),pygame.image.load('Resursi\Sprites/Blitzkrieg/riba 2.png')]
    
        for j in range (len(riba.riba_desno)):
            riba.riba_desno[j]=pygame.transform.scale(riba.riba_desno[j],(128,45))
            riba.riba_lijevo[j]=pygame.transform.scale(riba.riba_lijevo[j],(128,45))
        istina=False
        try:
            pygame.mixer.music.load('Custom\Mario song.mp3')
        except:
            pygame.mixer.music.load('Resursi\Zvučni efekti\Blitzkrieg\Mario song.mp3')
        try:
            jump=pygame.mixer.Sound('Custom\Mario Jump.wav')
        except:
            jump=pygame.mixer.Sound('Resursi\Zvučni efekti\Blitzkrieg\Mario Jump.wav')

        try:
            fireball=pygame.mixer.Sound('Custom/fireball.wav')
        except:
            fireball=pygame.mixer.Sound('Resursi/Zvučni efekti/Blitzkrieg/fireball.wav')

        try:
            skok_desno=pygame.image.load('Custom\mario.png')
            skok_lijevo=pygame.image.load('Custom\mario.png')
        except:
            skok_desno=pygame.image.load('Resursi\Sprites\Blitzkrieg\mario skače desno.png')
            skok_lijevo=pygame.image.load('Resursi\Sprites\Blitzkrieg\mario skače lijevo.png')

        try:
            desni_hod=[pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png')] 
            lijevi_hod=[pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png')]
            idle=pygame.image.load('Custom\mario.png')
            fail=pygame.image.load('Custom\mario.png')
        except:
            desni_hod=[pygame.image.load('Resursi\Sprites\Blitzkrieg\mario 1.png'),pygame.image.load('Resursi\Sprites\Blitzkrieg\mario 2.png'),pygame.image.load('Resursi\Sprites\Blitzkrieg\mario 3.png'),pygame.image.load('Resursi\Sprites\Blitzkrieg\mario 4.png')] 
            lijevi_hod=[pygame.image.load('Resursi\Sprites\Blitzkrieg\mario 1 obrnuti.png'),pygame.image.load('Resursi\Sprites\Blitzkrieg\mario 2 obrnuti.png'),pygame.image.load('Resursi\Sprites\Blitzkrieg\mario 3 obrnuti.png'),pygame.image.load('Resursi\Sprites\Blitzkrieg\mario 4 obrnuti.png')]
            idle=pygame.image.load('Resursi\Sprites\Blitzkrieg\mario 1.png')
            fail=pygame.image.load('Resursi\Sprites\Blitzkrieg\mario fail.png')
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
            pozadina=pygame.image.load('Resursi\pozadina2.png')
        pygame.mixer.music.play(loops=-1)        

    if tipka[pygame.K_SPACE] and shootLoop==0: # pucanje
        
        if Mario.lijevo:
            smjer=-1
            if super_mario:
                bullet=pygame.image.load('Resursi\Sprites\Mario\metak-lijevo.png')
            else:
                bullet=pygame.image.load('Resursi\Sprites\Blitzkrieg\metak-lijevo.png')
                bullet=pygame.transform.scale(bullet,(55,20))
        else:
            if super_mario:
                bullet=pygame.image.load('Resursi\Sprites\Mario\metak-desno.png')
            else:
                bullet=pygame.image.load('Resursi\Sprites\Blitzkrieg\metak-desno.png')
                bullet=pygame.transform.scale(bullet,(55,20))
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
        if super_mario:
            Mario.y=435
        else:
            Mario.y=400
        Mario.skok=False

    if not Mario.skok:  #skok
        if tipka[pygame.K_w]:
            Mario.skok=True
            Mario.desno=False
            Mario.lijevo=False
            Mario.brojač_hoda=0
            Mario.brojač_skoka=16
            if super_mario:
                jump=pygame.mixer.Sound('Resursi\Zvučni efekti\Mario\Mario Jump.wav')
            else:
                jump=pygame.mixer.Sound('Resursi\Zvučni efekti\Blitzkrieg\Mario Jump.wav')
            jump.play()

    else:
        if Mario.brojač_skoka>=-16:
            neg=1
            if Mario.brojač_skoka<0:
                neg=-1
            if  Mario.y==262:
                Mario.y=262

            else:
                Mario.y-=(Mario.brojač_skoka**2)*0.15*neg
            Mario.brojač_skoka-=1
        else:
            Mario.skok=False
            Mario.bojač_skoka=16
       
    crtanje()    
    pygame.display.update() #osvježavanje prozora

pygame.quit() #kraj programa
