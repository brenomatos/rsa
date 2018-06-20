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
        return(0,1)
    x,y = mdc_estendido(b,r)
    return (y,x-(a//b)*y)


def fatora(n):#usado para fatorar um n-1 em potencia de dois em miller
    atual = 2
    contador = 0
    t=0
    while atual*atual <= n:
        while(n%atual == 0):
            if atual == 2:
                t+=1
            n/=atual
        atual+=1

    q = int(n) #apenas para padronizar as variaveis
    return (t,q)#retorna o o numero fatorado em base 2 x parte prima

def talvez_primo(a,n,n1,t,q):
    x=exp_rapida(a,q,n)
    if x==1 or x==-1:
        return 1 ## nao sei
    while(t>0):
        x = x*x%n
        if x==n1:
            return 1 ##nao sei
        t-=1
    return 0 ##composto


def provavelmente_primo(iter, n):
    t,q = fatora(n)
    for i in range(0,iter):
        print(talvez_primo(randint(2,n-1),n,n-1,t,q))


provavelmente_primo(20,341)






# t,q = fatora(340)
# print(talvez_primo(3,341,340,t,q))

# print(mdc_estendido(13,2))
# print(pow(5,1024))
# print(exp_rapida(5,1024,2))
