
def cuadradoMedio (z1):
    lis=[]
    for i in range (100):
        z2=z1**2
        numero=str(z2)
        long=len(numero)
        if(long == 8):
            z3 = z2[2:6]
            dev=(int(z3)/10000)
            z1=int(z3)
            lis += [dev]
        else:
            cerosASumar= (8-long)
            z0='0'*cerosASumar
            z3=z0+numero
            z4=z3[2:6]
            dev=(int(z4)/10000)
            z1=int(z4)
            lis+=[dev]
    return lis

print(cuadradoMedio(1009))
