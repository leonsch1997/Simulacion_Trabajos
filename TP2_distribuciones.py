import random
import matplotlib.pyplot as plt
import  math
import numpy as np
def uniforme (a,b):
 x=[]
 for i in range (1000):
     r=round(random.random(),2)
     x+=[a+(b-a)*r]
 return x

uni=(uniforme(1,3))

def gamma(k,a):
 x=[]
 r=0
 for j in range(1,100):
     tr=1.0
     for i in range(1,k):
         r = random.random()
         tr=tr*r
     x+=[(-(math.log10(tr)))/a]
 return x

gam=(gamma(5,20))

def exponencial(ex):
 x=[]
 for i in range(1000):
     r=random.random()
     x+=[-ex*(math.log10(r))]
 return x

expo=(exponencial(5))

def normal(u,stdx):
 x=[]
 for j in range (1000):
     sum = 0.0
     for i in range (12):
         sum+=random.random()
     x+=[stdx*(sum-6.0)+u]
 return x
nor=normal(2.35,85.5)

def poison (lamb):
  x = []
  for j in range(1000):
      cont=0
      tr=1
      b=0
      while(tr-b >= 0):
          b = math.exp(-lamb)
          r=random.random()
          tr=tr*r
          if(tr-b >= 0):
              cont+=1
      x+=[cont]
  return x
poi=poison(50)

def binomial (k,q):
  nx=[]
  for j in range (1000):
      tr=1
      qr=math.log10(q)
      for i in range (k):
          r=random.random()
          tr*=r
      x=math.log10(tr)/qr
      nx+=[x]
  return nx
bino=binomial(5,200)

def empirica():
    x=[]
    p=[0.273,0.037,0.195,0.009,0.124,0.058,0.062,0.151,0.047,0.044]
    for j in range (1000):
        r=random.random()
        a=0
        for i in p:
          a+=i
          if (r<=a):
            break
        x+=[a]
    return x

empi=empirica()


def graficar(u,g,e,n,p,b,em):
 plt.title("uniforme")
 plt.hist(u)
 plt.show()
 plt.title("gamma")
 plt.hist(g,25,histtype="stepfilled", alpha=.7,linewidth=5, color='r')
 plt.show()
 plt.title("exponencial")
 plt.hist(e, 25, histtype="stepfilled", alpha=.7, linewidth=5, color='g')
 plt.show()
 plt.title("normal")
 plt.hist(n, 25, histtype="stepfilled", alpha=.7, linewidth=5, color='y')
 plt.show()
 plt.title("poisson")
 plt.hist(p, 25, histtype="stepfilled", alpha=.7, linewidth=5, color='orange')
 plt.show()
 plt.title("binomial")
 plt.hist(b, 25, histtype="stepfilled", alpha=.7, linewidth=5, color='black')
 plt.show()
 plt.title("empirica")
 plt.plot(em, color='violet')
 plt.show()



graficar(uni,gam,expo,nor,poi,bino,empi)



