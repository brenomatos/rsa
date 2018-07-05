from random import randint

def exp_rapida(b,e,n):#exponenciacao modular rapida: retorna (b^e) mod n
    r = 1
    b = b%n

    while(e>0):
        if (e&1):
            r = (r*b)%n

        e = e >> 1
        b = (b*b)%n
    return r


def mdc_estendido(a,b):#acha as constantes x e y tal que ax +by = mdc(a,b)
    r=a%b
    if r==0:
        return(b,0,1)
    g,x,y = mdc_estendido(b,r)
    return (g,y,x-(a//b)*y)

def inv_modular(a,n):#acha inverso de "a" mod n
    g,x,y = mdc_estendido(a,n)
    if g!=1:
        return 0
    else:
        return x%n


def talvez_primo(a,n,n1,t,q):#teste de miller
    x=exp_rapida(a,q,n)
    if x==1 or x==n1:
        return 1 ## nao sei
    while((t)>0):
        x = (x*x)%n
        if x==n1:
            return 1 ##nao sei
        t-=1
    return 0 ##composto


def provavelmente_primo(iter, n):#teste de miller-rabin
    t = 0
    q = n - 1
    while q & 1 == 0:
        t += 1
        q //= 2
    for i in range(0,iter):
        x = talvez_primo(randint(2,n-1),n,n-1,t,q)
        if x == 0: return 0 ## composto
    return 1##prov primo


def primo_aleatorio(b):##gera e retorna um primo aleatorio de b bits
    while(1):
        prov_primo = randint(2,2**b)
        prov_primo |= ((1 << b - 1) | 1)
        flag = provavelmente_primo(20, prov_primo)
        if flag == 1:
            return prov_primo

def acha_e(p,q):#acha a chave "e"
    phi = (p-1)*(q-1)
    i = 65537
    while(1):
        g,x,y = mdc_estendido(i, phi)
        if(g==1): return i;

def acha_d(e,p,q):#acha a chave d: inverso de "e" mod phi(n)
    return inv_modular(e,(p-1)*(q-1))


def codifica(str):
	r = 0
	for i in range(0,len(str)):
		r = r+ord(str[i])*pow(256,i)
	return r

def decodifica(n):
	str = ""
	while(n!=0):
		str += chr(n%256)
		n //= 256

	return str

def criptografa(M,n,e):
	return exp_rapida(M,e,n)

def descriptografa(C,n,d):
	return exp_rapida(C,d,n)


p = primo_aleatorio(2048)
# print("Numero p:" + str(p))
q = primo_aleatorio(2048)
# print("Numero q:" + str(q))
n = p*q
# print("Numero n:"+str(n))

e = acha_e(p,q)
d = acha_d(e,p,q)
f = open("salva_dados.txt","w")
f.write("Numero p:" + str(p))
f.write("\n\nNumero q:" + str(q))
f.write("\n\nNumero n:"+str(n))
f.write("\n\nChave e: "+str(e))
f.write("\n\nChave d: "+str(d))
mensagem = "casasbaasasasasassa"
print(mensagem)
M = codifica(mensagem)
print('M ' + str(M))
msg_cript = criptografa(M,n,e)
print("msg criptografada: " + str(msg_cript))
msg_descrip = descriptografa(msg_cript,n,d)
print(msg_descrip)
descod = decodifica(msg_descrip)
print(descod)
