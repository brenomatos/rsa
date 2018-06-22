from random import randint

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

def fatora(n):#usado para fatorar um n-1 em potencia de dois em miller
    atual = 2
    t=0
    while atual*atual <= n:
        while(n%atual == 0):
            if atual == 2:
                t+=1
            n/=atual
        break

    q = int(n) #apenas para padronizar as variaveis
    return (t,q)#retorna o o numero fatorado em base 2 x parte prima


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
    t,q = fatora(n-1)
    for i in range(0,iter):
        x = talvez_primo(randint(2,n-1),n,n-1,t,q)
        if x == 0: return "composto"
    return "prov primo"


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
print(provavelmente_primo(20,1023142342342342342340000345435543535345345345345345408))
