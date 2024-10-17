plansza = 36*[0]
import random as rn
import time
koncowe_p = [0, 2, 4, 35, 33, 31]
pionkii = [1, -1]
nielegalne = []
xc = 0
for x in range(6):
    for z in range(3):
        nielegalne.append(2*z+6*x+xc)
    if xc == 0:
        xc = 1
    else:
        xc = 0
        
tura = 1    # 0       2        4        7     9    11  12      14      16          19      21     23
pozycje_b = [0.5, 0, 0.5, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0.5, 0, 0.75, 0, 0, 0.75, 0, 1, 0, 1.5, 2.5, 0, 1.75, 0, 1.5, 0, 0, 0, 0, 0, 0, 0]
pozycje_q = [-3, 0, -2, 0, -1, 0, 0, 0, 0, 0, 0, -1, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, -1, 0, 0, 0, 0, 0, 0, -1, 0, -2, 0, -2]
def dekoding(move):
    k1 = ''
    k2 = ''
    bicie = 0
    for x in range(2):
        k1 += move[x]
        if move[x+1] == '-':
            break
        if move[x+1] == 'x':
            bicie = 1
            break
    for z in range(len(move)-x-2):
        k2 += move[z+x+2]
    k1 = int(k1)
    k2 = int(k2)
    return k1, k2, bicie
def init():
    global plansza
    global tura
    tura = 1
    lista = []
    lista1 = []
    for x in range(3):
        lista.append(2*x)
        lista.append(2*x+7)
        lista1.append(31+2*x)
        lista1.append(24+2*x)
    for x in range(6):
        plansza[lista[x]] = 1
        plansza[lista1[x]] = -1
def argmax(lista, maxi):
    if maxi == 1:
        numer = max(lista)
    else:
        numer = min(lista)
    lista1 = []
    for x in range(len(lista)):
            if lista[x] == numer:
                lista1.append(x)
    return rn.choice(lista1)
            
def rp(p):
    print(19*'=')
    for x in range(6):
        line = '| '
        for y in range(6):
            idx = (5-x)*6 + y
            if p[idx] == 1:
                line += 'b'
            elif p[idx] == -1:
                line += 'q'
            elif p[idx] == -3:
                line += 'Q'
            elif p[idx] == 3:
                line += 'B'
            else:
                line += ' '
            line += '| '
        print(line)
    print(19*'=')
def gene_r(t, p):
    ruchy = []
    for x in range(36):
        if p[x] == t or p[x] == t*3:
            move = ruch_p(x, p)
            if not move == []:
                ruchy += move
    ruchy = move_ordering(ruchy, p)
    return ruchy
def ruch_p(numer, p):
    ruchy = []
    typ = p[numer]
    if not typ  == 0:
        if typ == 1 or typ == -1:
            if numer+5*typ in nielegalne and numer+5*typ > -1:
                if p[numer+5*typ] == 0 :
                    ruchy.append(f'{numer}-{numer+5*typ}')
            if numer+7*typ in nielegalne and numer+7*typ > -1:
                if p[numer+7*typ] == 0:
                    ruchy.append(f'{numer}-{numer+7*typ}')
            if numer+10*typ in nielegalne:
                if p[numer+10*typ] == 0:
                    if p[numer+5*typ] == typ*-1 or p[numer+5*typ] == typ*-3:
                        ruchy.append(f'{numer}x{numer+10*typ}')
            if numer+14*typ in nielegalne:
                if p[numer+14*typ] == 0:
                    if p[numer+7*typ] == typ*-1 or p[numer+7*typ] == typ*-3:
                        ruchy.append(f'{numer}x{numer+14*typ}')
        else:
            if numer+5 in nielegalne:
                if p[numer+5] == 0:
                    ruchy.append(f'{numer}-{numer+5}')
            if numer-5 in nielegalne:
                if p[numer-5] == 0 and  numer-5 in nielegalne:
                    ruchy.append(f'{numer}-{numer-5}')
            if numer+7 in nielegalne:
                if p[numer+7] == 0:
                    ruchy.append(f'{numer}-{numer+7}')
            if numer-7 in nielegalne:
                if p[numer-7] == 0:
                    ruchy.append(f'{numer}-{numer-7}')
            if numer+10 in nielegalne:
                if p[numer+10] == 0:
                    if p[numer+5] == typ*-1 or p[numer+5] == typ/-3:
                        ruchy.append(f'{numer}x{numer+10}')
            if numer+14 in nielegalne:
                if p[numer+14] == 0:
                    if p[numer+7] == typ*-1 or p[numer+7] == typ/-3:
                        ruchy.append(f'{numer}x{numer+14}')                    
            if numer-10 in nielegalne:
                if p[numer-10] == 0:
                    if p[numer-5] == typ*-1 or p[numer-5] == typ/-3:
                        ruchy.append(f'{numer}x{numer-10}')
            if numer-14 in nielegalne:
                if p[numer-14] == 0:
                    if p[numer-7] == typ*-1 or p[numer-7] == typ/-3:
                        ruchy.append(f'{numer}x{numer-14}')                    
                         
    return ruchy
def eval_(p, t):
    punkty = 0
    wyn ,m1 ,m2 = check_win(p, t)
    if not wyn == 3:
        return wyn
    else:
        for x in range(36):
            punkty += p[x]
            if p[x] == 1:
                punkty += pozycje_b[x]/2
            if p[x] == -1:
                punkty -= pozycje_b[35-x]/2
            if p[x] == 3:
                punkty += pozycje_q[x]
            if p[x] == -3:
                punkty -= pozycje_q[35-x]
        punkty += m1/4 - m2/4
        return punkty
def liczenie(p):
    licz = 0
    for x in range(36):
        if p[x] != 0:
            licz += 1
    return licz
def check_win(p, t):
    move1 = gene_r(1, p)
    move2 = gene_r(-1, p)
    n1 = len(move1)
    n2 = len(move2)
    if t == 1:
        if n1 == 0:
            if n2 == 0 :
                return 0, n1, n2
            else:
                return -1000, n1, n2
        else:
            return 3, n1, n2
    elif t == -1:
        if n2 == 0:
            if n1 == 0 :
                return 0, n1, n2
            else:
                return 1000, n1, n2
        else:
            return 3, n1, n2
def sorting(ruchy, wartosci):
    n = len(ruchy)  
    for i in range(n):
        for j in range(0, n-i-1):
            if wartosci[j] < wartosci[j+1]:
                wartosci[j], wartosci[j+1] = wartosci[j+1], wartosci[j]
                ruchy[j], ruchy[j+1] = ruchy[j+1], ruchy[j]    
    return ruchy

def make_ruch(p, numer, ruch, zbicie):
    pionek = p[numer]
    p[numer] = 0
    p[ruch] = pionek
    if zbicie == 1:
        d = int((numer+ruch)/2)
        p[d] = 0
    for x in range(3):
        if p[31+2*x] == 1:
            p[31+2*x] = 3
    for x in range(3):
        if p[2*x] == -1:
            p[2*x] = -3
    return p
def move_ordering(ruchy, p):
    lista = [0]*len(ruchy)
    for x in range(len(ruchy)):
        ru1, ru2, bicie = dekoding(ruchy[x])
        if bicie == 1:
            lista[x] += 3
        if p[ru1] in pionkii:
            if ru2 in koncowe_p:
                lista[x] += 2
            else:
                if p[ru1] == 1:
                    lista[x] += pozycje_b[ru2]
                else:
                    lista[x] += pozycje_b[35-ru2]
        else:
            if p[ru1] == 3:
                lista[x] += pozycje_q[ru2]/2
            else:
                lista[x] += pozycje_q[35-ru2]/2
    lista = sorting(ruchy, lista)        
    return lista
def minimax(stan, tura, depht, maxi, głębokość, alpha, beta, transposition):
    local_tans = transposition.copy()
    global mn
    if not tuple(stan+[tura]) in mn:
        ruchy = gene_r(tura, stan)
        if depht == 0 or ruchy == []:
            vela = eval_(stan, tura)
#            if vela == 1000:
 #               vela = 1000 + depht
 #           elif vela == -1000:
 #               vela = vela - depht
            mn[tuple(stan+[tura])] = vela, None, None, 1, głębokość - depht, f'{vela}'
            return vela, None, None, 1, głębokość - depht, f'{vela}'
        else:
            if not tuple(stan) in local_tans:
                local_tans[tuple(stan)] = 1
            else:
                local_tans[tuple(stan)] += 1
            if local_tans[tuple(stan)] == 3:
                return 0, None, None, 1, głębokość - depht, f'{0}'
        
            else:
                listeval = []
                maxdepht = 0
                licznik = 0
                #bestmove = 0
                if maxi == True:    
                    best = -float('inf')
                    for x in range(len(ruchy)):
                        p = stan.copy()
                        move_mini = ruchy[x]
                        ru1, ru2, bicie = dekoding(move_mini)
                        p = make_ruch(p, ru1, ru2, bicie)
                        score, cv, cz, d, depht1, skrot1 = minimax(p, tura*-1, depht-1, False, głębokość, alpha, beta, local_tans)
                        if depht == głębokość or depht == głębokość - 1 or depht == głębokość - 2 or depht == głębokość - 3 or depht == głębokość - 4:
#                            print(f'node:{głębokość-depht}/ruch:{ruchy[x]}/{x+1}z{len(ruchy)}/konćówki:{d}/eval:{score}/alpha:{alpha}/beta:{beta}')

                            print(f"{4*(głębokość-depht)*'-'} node:{głębokość-depht} |{(x+1)*'#'}{(len(ruchy)-(x+1))*'-'}|{100*(x+1)/len(ruchy)}%")
#                                print(skrot1)

                        maxdepht = max(maxdepht, depht1)
                        listeval.append(score)
                        licznik += d
                        if score > best:
                            skrot2 = skrot1
                            best = score
                            bestmove = x
                        alpha = max(score, alpha)
                        if alpha >= beta:
                           break
                else:
                    best = float('inf')
                    for x in range(len(ruchy)):
                        p = stan.copy()
                        move_mini = ruchy[x]
                        ru1, ru2, bicie = dekoding(move_mini)
                        p = make_ruch(p, ru1, ru2, bicie)
                        score, cv, cz, d, depht1, skrot1 = minimax(p, tura*-1, depht-1, True, głębokość, alpha, beta, local_tans)
                        if depht == głębokość or depht == głębokość - 1 or depht == głębokość - 2 or depht == głębokość - 3 or depht == głębokość - 4:
 #                           print(f'node:{głębokość-depht}/ruch:{ruchy[x]}/{x+1}z{len(ruchy)}/konćówki:{d}/eval:{score}/alpha:{alpha}/beta:{beta}')
                            print(f"{4*(głębokość-depht)*'-'} node:{głębokość-depht} |{(x+1)*'#'}{(len(ruchy)-(x+1))*'-'}|{100*(x+1)/len(ruchy)}%")
#                               print(skrot1)
                        maxdepht = max(maxdepht, depht1)
                        licznik += d
                        listeval.append(score)
                        if score < best:
                            skrot2 = skrot1
                            best = score
                            bestmove = x
                        beta = min(score, beta)
                        if alpha >= beta:
                            break
                skrot2 += f' {ruchy[bestmove]}'
                mn[tuple(stan+[tura])] = (best, bestmove, listeval, 1, maxdepht, skrot2)
                return best, bestmove, listeval, licznik, maxdepht, skrot2
            
    else:
        return mn[tuple(stan+[tura])]

#plansza = [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, -1, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, -1]
#plansza = [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 1, 0, 0, 1, 0, -1, 0, 0, -1, 0, -1, 0, 0]
#plansza = [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tura = 1
AI = [1]
AI2 = []
man = [-1]
init()
#plansza = [0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0]
#plansza[0] = 3
#plansza[35] = -3
#rp(plansza)
t_tra = {}
for iteration in range(150):
    print(plansza)
    #time.sleep(1)
    rp(plansza)
    ruchy = (gene_r(tura, plansza))
    print(iteration+1)
    print(ruchy)
    wynik = check_win(plansza, tura)[0]
    if wynik == 3:
        if tura in man:
            move = int(input('ruch:'))
        elif tura in AI2:
            move = 0
        elif tura in AI:
            mn = {}
            depht = 20 + (12 - liczenie(plansza))
            #depht = 6
            print(f"depht:{depht}")
            print(f"|{len(ruchy)*'-'}|0.0%")
            transp = t_tra.copy()
            linu = minimax(plansza, tura, depht, (tura == 1), depht, -float('inf'), float('inf'), transp)
            #move = argmax(linu[2], tura)
            move = linu[1]
            if move == None:
                print('problem')
                break
            print(f'eval:{linu[0]}|move evaluation:{linu[2]}|searche:{linu[3]}')
            print(f'eval : {linu[0]}')
            kuzano = linu[5]
#            kuzano = kuzano[::-1]
            print(kuzano)
        print(ruchy[move])
        ru1, ru2, bicie = dekoding(ruchy[move])
        plansza = make_ruch(plansza, ru1, ru2, bicie)
        if tuple(plansza) in t_tra:
            t_tra[tuple(plansza)] += 1
            if t_tra[tuple(plansza)] == 3:
                print('GAME OVER')
                print('Draw by repetition')
                break
        else:
            if bicie == 1:
                t_tra = {}
            t_tra[tuple(plansza)] = 1
        tura *= -1
    else:
        print('GAME OVER')
        if wynik == 0:
            print('Draw')
        elif wynik == 1000:
            print('Player B won')
        else:
            print('Player Q won')
        break

