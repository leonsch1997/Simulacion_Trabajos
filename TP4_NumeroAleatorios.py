
# def cuadrado_medios(Z): #Esta funcion tiene que converger a 0
#    zf=[]
#    z1s=[]
#    z1=Z**2                         #zf y z1s son arreglos ... z1 es variable
#    long=len(str(z1))               #acá lo casteo para sacarle la longitud al numero z1
#    for j in str(z1):
#        z1s+=[int(j)]               #lleno el arreglo z1s, cada elemento 1 digito
#    if (long<=8):
#        for i in range (8-long):    #si tiene menos de 8 digitos se ponen 0's adelante para llegar a 8
#            z1s+=[0]
#    zf=z1s[2:6]                     #al arreglo z1s le corto los 4 del medio y los pongo en zf (recordar que sigue siendo una lista)
#    s= ''.join(str(e) for e in zf)  #uno todo con un join para convertir la list en string
#    sf=int(s)  #por ultimo convierto el string nuevamente a int
#    return sf
#
# z=(cuadrado_medios(1009))
# print(z/10000)
# for i in range (200):
#    zi=cuadrado_medios(z)
#    print(i," - ",float(zi)/10000)
#    z=zi


def cuadradoMedio (z1):
  z2=z1**2

  long=len(str(z2))
  if(long == 8):
     for j in range (30):
        z3 = z2[2:6]
        print (z3/10000)
  else:
     cerosASumar= (8-long)
     print(cerosASumar)

  return (cerosASumar)

cuadradoMedio(z1=1009)
