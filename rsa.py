from random import randint

#https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
def exp_rapida(b,e,n):
    r = 1
    b = b%n

    while(e>0):
        if (e&1):
            r = (r*b)%n

        e = e >> 1
        b = (b*b)%n
    return r


def mdc_estendido(a,b):
    r=a%b
    if r==0:
        return(b,0,1)
    g,x,y = mdc_estendido(b,r)
    return (g,y,x-(a//b)*y)

def inv_modular(a,n):
    g,x,y = mdc_estendido(a,n)
    if g!=1:
        return 0
    else:
        return x%n


def talvez_primo(a,n,n1,t,q):
    x=exp_rapida(a,q,n)
    if x==1 or x==n1:
        return 1 ## nao sei
    while((t)>0):
        x = (x*x)%n
        if x==n1:
            return 1 ##nao sei
        t-=1
    return 0 ##composto


def provavelmente_primo(iter, n):
    t = 0
    q = n - 1
    while q & 1 == 0:
        t += 1
        q //= 2
    for i in range(0,iter):
        x = talvez_primo(randint(2,n-1),n,n-1,t,q)
        if x == 0: return 0 ## composto
    return 1##prov primo


def primo_aleatorio(b):
    while(1):
        prov_primo = randint(2,2**b)
        prov_primo |= ((1 << b - 1) | 1)
        flag = provavelmente_primo(1, prov_primo)
        if flag == 1:
            return prov_primo

def acha_e(p,q):
    phi = (p-1)*(q-1)
    i = 65537
    while(1):
        g,x,y = mdc_estendido(i, phi)
        if(g==1): return i;


p = primo_aleatorio(2048)
print("Numero p:" + str(p))
q = primo_aleatorio(2048)
print("Numero q:" + str(q))
n = p*q
print("Numer n:"+str(n))



print(acha_e(p,q))
# t,q = fatora(17330748)
# print(talvez_primo(3,17330749,17330748,t,q))
# print(provavelmente_primo(10,17330749))
# print(mdc_estendido(13,2))
# print(pow(5,1024))
# print(exp_rapida(5,1024,2))
# for j in range(0,25):
# 	a = input().split(" ")
# 	for i in range(0,4):
# 		print(provavelmente_primo(20,int(a[i])))
