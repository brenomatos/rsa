from random import randint

def modular_exp(b,e,n):#Fast modular exponentiation: returns (b^e) mod n
    r = 1
    b = b%n

    while(e>0):
        if (e&1):
            r = (r*b)%n

        e = e >> 1
        b = (b*b)%n
    return r


def extended_euclidean(a,b):# finds "x" and "y" so "ax +by = mdc(a,b)"
    r=a%b
    if r==0:
        return(b,0,1)
    g,x,y = extended_euclidean(b,r)
    return (g,y,x-(a//b)*y)

def modular_inv(a,n):# finds the inverse of "a" mod n
    g,x,y = extended_euclidean(a,n)
    if g!=1:
        return 0
    else:
        return x%n


def miller_test(a,n,n1,t,q):# performs Miller test
    x=modular_exp(a,q,n)
    if x==1 or x==n1:
        return 1 ## dont know
    while((t)>0):
        x = (x*x)%n
        if x==n1:
            return 1 ## dont know
        t-=1
    return 0 ## composite


def miller_rabin_test(iter, n):# performs miller-rabin test
    t = 0
    q = n - 1
    while q & 1 == 0:
        t += 1
        q //= 2
    for i in range(0,iter):
        x = miller_test(randint(2,n-1),n,n-1,t,q)
        if x == 0: return 0 ## composite
    return 1## probably prime


def random_prime(b):## generates a random prime with "b" bits
    while(1):
        probably_prime = randint(2,2**b)
        probably_prime |= ((1 << b - 1) | 1)
        flag = miller_rabin_test(20, probably_prime)
        if flag == 1:
            return probably_prime

def find_e(p,q):# calculates the "e" key
    phi = (p-1)*(q-1)
    i = 65537
    while(1):
        g,x,y = extended_euclidean(i, phi)
        if(g==1): return i;

def find_d(e,p,q):#finds "d" key: modular inverse of "e" mod phi(n)
    return modular_inv(e,(p-1)*(q-1))


def encodes(str):
	r = 0
	for i in range(0,len(str)):
		r = r+ord(str[i])*pow(256,i)
	return r

def decodes(n):
	str = ""
	while(n!=0):
		str += chr(n%256)
		n //= 256

	return str

def encrypt(M,n,e):
	return modular_exp(M,e,n)

def decrypt(C,n,d):
	return modular_exp(C,d,n)
