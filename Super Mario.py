#unošenje potrebnih datoteka
import pygame
import Videoplayer
#inicijalizacija Pygame-a
pygame.init()
pygame.font.init()
#izgled prozora
win=pygame.display.set_mode((960,540),pygame.RESIZABLE)#dimenzije prozora
zaslon_dužina=960
zaslon_visina=540
a=pygame.image.load('Resursi\mario ikona.png')
pygame.display.set_icon(a)
pygame.display.set_caption('Super Mario')

pygame.mixer.init() #zvučni efekti
pygame.mixer.pre_init(channels=2)

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
#izgled fonta
font = pygame.font.SysFont('Comis Sans MS', 32)
#timer za evente
TIMER_EVENT=pygame.USEREVENT+1 #ubrzavanje gljive
pygame.time.set_timer(TIMER_EVENT,10000)
TIMER_EVENT1=pygame.USEREVENT+2 
pygame.time.set_timer(TIMER_EVENT1,20000)
#sprite-ovi
dužina_slike=50 # sprite-ovi
visina_slike=58
try:
    bullet=pygame.image.load('Custom\metak.png')
except:
    bullet=pygame.image.load('Resursi\Sprites\metak.png')
bullet=pygame.transform.rotozoom(bullet,-90,1)

try:
    desni_hod=[pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png')] 
    lijevi_hod=[pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png'),pygame.image.load('Custom\mario.png')] 
    idle=pygame.image.load('Custom\mario.png')
    fail=pygame.image.load('Custom\mario.png')
except:
    desni_hod=[pygame.image.load('Resursi\Sprites\mario 1.png'),pygame.image.load('Resursi\Sprites\mario 2.png'),pygame.image.load('Resursi\Sprites\mario 3.png'),pygame.image.load('Resursi\Sprites\mario 4.png')] 
    lijevi_hod=[pygame.image.load('Resursi\Sprites\mario 1 obrnuti.png'),pygame.image.load('Resursi\Sprites\mario 2 obrnuti.png'),pygame.image.load('Resursi\Sprites\mario 3 obrnuti.png'),pygame.image.load('Resursi\Sprites\mario 4 obrnuti.png')]
    idle=pygame.image.load('Resursi\Sprites\mario 1.png')
    fail=pygame.image.load('Resursi\Sprites\mario fail.png')

fail=pygame.transform.scale(fail,(dužina_slike+4,visina_slike+1))

for i in range (len(lijevi_hod)):
    lijevi_hod[i]=pygame.transform.scale(lijevi_hod[i],(dužina_slike,visina_slike))
    desni_hod[i]=pygame.transform.scale(desni_hod[i],(dužina_slike,visina_slike))
    idle=pygame.transform.scale(idle,(dužina_slike,visina_slike))

try:
    pozadina=pygame.image.load('Custom\pozadina.png')
except:
    pozadina=pygame.image.load('Resursi\pozadina.png')
#pozicija pozadine
move_x=0
#brojač pogodaka
brojač_pogodaka=0
#fps
clock=pygame.time.Clock()

run=True

#podaci za gljivu
class gljiva(object):
    #animacija hoda   
    gljiva_hod=[pygame.image.load('Resursi\Sprites\gljiva1.png'),pygame.image.load('Resursi\Sprites\gljiva2.png')]
    for i in range (len(gljiva_hod)):
        gljiva_hod[i]=pygame.transform.scale(gljiva_hod[i],(44,40))
    #vrijednosti za igled i kretanje        
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
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2) #zadržao sam hitbox kako bih kasnije znao prilagoditi ga po potrebi
    #obrazac kretanja gljive
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
#podaci za Maria        
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
        if self.brojač_hoda+1>=60:
            self.brojač_hoda=0

        if not (self.stajanje):   # hodanje
            if self.lijevo:
                win.blit(lijevi_hod[self.brojač_hoda//15],(self.x,self.y))
                self.brojač_hoda+=1
            elif self.desno:
                win.blit(desni_hod[self.brojač_hoda//15],(self.x,self.y))
                self.brojač_hoda+=1
        else:
            if self.desno:
                win.blit(desni_hod[0],(self.x,self.y))
            else:
                win.blit(lijevi_hod[0],(self.x,self.y))
        self.hitbox=(self.x+2,self.y,47,62)
        #pygame.draw.rect(win,(0,0,255),self.hitbox,2)
    #kraj igre
    def hit(self):
        win.blit(pozadina,(move_x,0))
        win.blit(neprijatelj.gljiva_hod[1],(neprijatelj.x,neprijatelj.y))
        win.blit(fail,(self.x,self.y-3))
        pygame.display.update()
        try:
            pygame.mixer.music.load('Custom\game over.mp3')
        except:
            pygame.mixer.music.load('Resursi\Zvučni efekti\game over.mp3')
        pygame.mixer.music.play()
        if brojač_pogodaka<=40:
            print('Ukupan broj pogodaka: {} ... Jadno!' .format(brojač_pogodaka))
        if brojač_pogodaka>40 and brojač_pogodaka<=50:
            print('Ukupan broj pogodaka: {} ... Meh!' .format(brojač_pogodaka))
        if brojač_pogodaka>50 and brojač_pogodaka<=60:
            print('Ukupan broj pogodaka: {} ... Nije loše!' .format(brojač_pogodaka))
        if brojač_pogodaka>60 and brojač_pogodaka<=80:
            print('Ukupan broj pogodaka: {} ... Opa!' .format(brojač_pogodaka))
        if brojač_pogodaka>80:
            print('Ukupan broj pogodaka: {} ... To legendo!' .format(brojač_pogodaka))
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

def crtanje():  #crtač objekata
    global brojač_hoda
    win.blit(pozadina,(move_x,0))#pozadina
    
    Mario.crtaj(win)#lik Maria
    neprijatelj.crtaj(win)#lik gljive
    for metak in municija:#metak
        metak.crtaj(win)
    pygame.display.update()#osvježavanje prozora
#pozicija objekata
Mario=igrač(870,435,35,35)
neprijatelj=gljiva(0,453,32,32,960-40)
#ograničavanje municije
municija=[]
shootLoop=1

# glavna petlja
while run:  

    clock.tick(60)   # FPS
    #određivanje pogotka        
    if Mario.hitbox[1]<neprijatelj.hitbox[1]+neprijatelj.hitbox[3] and Mario.hitbox[1]+Mario.hitbox[3]>neprijatelj.hitbox[1]:
        if Mario.hitbox[0]+Mario.hitbox[2]>neprijatelj.hitbox[0] and Mario.hitbox[0]<neprijatelj.hitbox[0]+neprijatelj.hitbox[2]:
            Mario.hit()
    if shootLoop>0:
        shootLoop+=1
    if shootLoop>1:
        shootLoop=0
    
    for metak in municija: # pucanje
        if metak.y-metak.radius<neprijatelj.hitbox[1]+neprijatelj.hitbox[3] and metak.y+metak.radius>neprijatelj.hitbox[1]:
            if metak.x+metak.radius>neprijatelj.hitbox[0] and metak.x-metak.radius<neprijatelj.hitbox[0]+neprijatelj.hitbox[2]:
                brojač_pogodaka+=1
                municija.pop(municija.index(metak))
        if metak.x<960 and metak.x>0:
            metak.x+=metak.vel
        else:
            municija.pop(municija.index(metak))
       # if  metak.y!=neprijatelj.y and metak.x!=neprijatelj.x:
         #   win.blit(gljiva_mrtva,(neprijatelj.x,neprijatelj.y+10))
          #  pygame.display.update()
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
        
        if Mario.lijevo:#smjer metka
            smjer=-1
            bullet=pygame.image.load('Resursi\Sprites\metak-lijevo.png')
        else:
            bullet=pygame.image.load('Resursi\Sprites\metak-desno.png')
            smjer=1
        if len(municija)<1:
            fireball.play()#zvučni efekt metka
            municija.append(projektil(round(Mario.x+Mario.width//2),round(Mario.y+Mario.height//2),6,(0,0,0),smjer))#ograničavanje pucanja

    if tipka[pygame.K_m]: # isključivanje glazbe
        pygame.mixer.music.pause()
  
    if tipka[pygame.K_a] and Mario.x>Mario.vel:#kretanje lijevo 
        Mario.x-=Mario.vel
        Mario.lijevo=True
        Mario.desno=False
        Mario.stajanje=False

    elif tipka[pygame.K_d] and Mario.x<zaslon_dužina-Mario.width-Mario.vel:#kretanje desno
        Mario.x+=Mario.vel
        Mario.lijevo=False
        Mario.desno=True
        Mario.stajanje=False

    else:#stajanje
        Mario.stajanje=True
        Mario.brojač_hoda=0
    if tipka[pygame.K_s] and Mario.y!=435:
        Mario.y=435
        Mario.skok=False

    if not (Mario.skok):  #skok
        if tipka[pygame.K_w]:
            Mario.skok=True
            Mario.desno=False
            Mario.lijevo=False
            Mario.brojač_hoda=0
            Mario.brojač_skoka=16
            jump.play()

    else:#skok u smjeru kretanje igrača
        if Mario.brojač_skoka>=-16:
            neg=1
            if Mario.brojač_skoka <0:
                neg=-1
            if  Mario.y==262 and Mario.x>=460 and Mario.x<=678:
                Mario.y=262
            else:
                Mario.y-=(Mario.brojač_skoka**2)*0.15*neg
            Mario.brojač_skoka-=1
        else:
            Mario.skok=False
            Mario.bojač_skoka=16
    #prekid igre pri sudaru gljive i Maria
    if Mario.hitbox[1]+Mario.hitbox[3]<neprijatelj.hitbox[1]+neprijatelj.hitbox[3] and Mario.hitbox[1]>neprijatelj.hitbox[1]:
            if Mario.hitbox[0]>neprijatelj.hitbox[0] and Mario.hitbox[0]+Mario.hitbox[2]<neprijatelj.hitbox[0]+neprijatelj.hitbox[2]:
                run=False
    #crtanje objekata
    crtanje()
    #prikaz pogodaka
    text = font.render('Broj pogodaka: {}'.format(brojač_pogodaka), True, (255,255,255))
    win.blit(text,(7,7))
    #ažuriranje prozora
    pygame.display.update()
#kraj programa
pygame.quit()
