import random, pygame, math

run = True
pygame.init()
WWidht = 1500
HHeight = 900
win = pygame.display.set_mode((WWidht, HHeight))
pygame.display.set_caption("Life")
fon  = pygame.font.SysFont('arial', 24)
win.fill((255, 255, 255))
f = open('text1.txt', 'r')
m = 0
k =[]
k = f.readlines()
b = len(k)
bb =0
nk =''
snk = ''
snk2 = ''



class Words:
    stroka = 0
    bukva = 0
    MassStrok = []


def GetText (inn:Words):
    il  = len(inn.MassStrok)-1
    a = inn.stroka
    al = len(inn.MassStrok[a])-1
    b = inn.bukva
    if a < il and b < al:
        d = inn.MassStrok[a][b]
        if d == '—':
            inn.bukva += 1
            d = GetText(inn)
            return d
        if d == '\n':
            inn.bukva += 1
            d = ' '
            return d
        #if d == ' ':
        #    return u'\u02FD'# u'\u0420\u043e\u0441\u0441\u0438\u044f'
    elif b == al:
        inn.stroka += 1
        inn.bukva = 0
        d = ' '
        return d
    elif a == il:
        return None
    inn.bukva += 1
    return d

def compbukv(bu, vv):
    if bu == vv:
        pygame.mixer.music.load('Sound_ok.mp3')
        pygame.mixer.music.play()
        return True
    if bu != vv and vv != '':
        pygame.mixer.music.load('Sound_no.mp3')
        pygame.mixer.music.play()
    return False

ww = Words
ww.MassStrok = k
chto = GetText(ww)
snk2 =  chto
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            nk = event.unicode
            if compbukv(chto, nk):
                snk += nk
                chto = GetText(ww)
                snk2 += chto if chto != ' ' else u'\u007E'
    keys = pygame.key.get_pressed()
    text1 = fon.render(snk2,0 , (100, 80, 50))
    text = fon.render(snk, 0, (10, 80, 50))
    win.blit(text1, (10, 10))
    win.blit(text, (100, 100))

    pass
    pygame.display.update()
    if (keys[pygame.K_UP]):
        l = True
pygame.quit()
f.close()