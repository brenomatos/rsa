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

# GERANDO PRIMOS ALEATORIOS
p = primo_aleatorio(2048)
q = primo_aleatorio(2048)
n = p*q
#CALCULADO e E d
e = acha_e(p,q)
d = acha_d(e,p,q)
#Aqui adicionei codigo caso queir inserir os seus proprios primos
#Entao basta comentar as linhas anteriores
# p = int(input("\n\nDigite um primo p: "))
# q = int(input("\n\nDigite um primo q: "))
# n = p*q
# e = acha_e(p,q)
# d = acha_d(e,p,q)

#Caso queirsa salvar informacoes em um arquivo
# f = open("saida_primos.txt","w")
# f.write("primo p: "+str(p)+"\n\n\n")
# f.write("primo q: "+str(q)+"\n\n\n")
# f.write("numero n = p*q: "+str(p*q)+"\n\n\n")
# f.write("numero e: "+str(e)+"\n\n\n")
# f.write("numero d: "+str(d)+"\n\n\n")

print("Numero p:" + str(p)+"\n\n")
print("Numero q:" + str(q)+"\n\n")
print("Numero n:"+str(n)+"\n\n")
print("Chave e: "+str(e)+"\n\n")
print("Chave d: "+str(d)+"\n\n")

mensagem = str(input('Digite a mensagem a ser criptografada: \n'))

print("Mensagem Pre codificacao: "+str(mensagem)+"\n\n")

M = codifica(mensagem)
print('Mensagem Codificada: ' + str(M)+"\n\n")

msg_cript = criptografa(M,n,e)
print("Mensagem Criptografada: " + str(msg_cript)+"\n\n")

msg_descrip = descriptografa(msg_cript,n,d)
print("Mensagem Descriptografada: "+ str(msg_descrip)+"\n\n")

msg_descod = decodifica(msg_descrip)
print("Mensagem Decodificada: "+str(msg_descod)+"\n\n")

#adicionei uma mensagem de exatos 500 char para eventuais testes
mensagem = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu"
