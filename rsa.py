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

    return (t,int(n))#retorna o o numero fatorado em base 2 x parte prima

def miller(a,n):
    x=exp_rapida(a,q,n)
    if x==1 or x==-1:
        return "Nao sei"
    while(t>0):
        x = x*x%n
        if x==n-1:
            return "Nao sei"
        t-=1
    return "composto"


print(fatora(320))





# print(mdc_estendido(13,2))
# print(pow(5,1024))
# print(exp_rapida(5,1024,2))
