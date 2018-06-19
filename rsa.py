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
    return (y,x-r*y)


print(mdc_estendido(4,5))
# print(pow(5,1024))
# print(exp_rapida(5,1024,2))
