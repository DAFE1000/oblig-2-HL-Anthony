import numpy as np
import matplotlib.pyplot as plt

#--------------------------------------------For ploten-----------------------------------------------------#


## Setter begrensninger for x og y range for ploten som lages
upperLim = 5
lowerLim = -0.5

plt.xlim(lowerLim,upperLim)
plt.ylim(lowerLim,upperLim)


#--------------------------------------------For utregning-------------------------------------------------#
# funksjonen f(x)
def f(x) :
  y = np.power(np.e, -x/4) * np.arctan(x)
  return y

# den deriverte av f(x)
def df(x):
   y = np.power(np.e, -x/4) * (1/(1+np.power(x,2)) - (1/4 * np.arctan(x)))
   return y

# den andre deriverte av f(x)
def ddf(x):

   e = np.power(np.e, -x/4)

   y = ((e/16) * np.arctan(x) ) - ( e / (2*(1+np.power(x,2))) ) - ((2 * x * e ) / (np.power((1 + np.power(x,2)) , 2)))
   return y


#-----------------------------------------------Utregning-----------------------------------------------------#


# start gjett , og maksimal x verdi variabel 
xn = 1.5

# indeks variabel 
i = 0 

# newtons metode implementasjon 
while i < 5 :

   xn = xn - ( df(xn) / ddf(xn) )
   i += 1

#printe variabler 
print ("xn =", '%.8f'%xn)
print ("f(xn) = ",'%.8f'%f(xn))
print ("df(xn) = ",'%.8f'%df(xn))


##--------------------------------------ploting av punktet og grafen-----------------------------------------#

## definerer x verdi range og antall punkter mellom -15 -> 15 
x = np.linspace(-15 , 15 , 2000)

plt.plot(x,f(x))
plt.plot(xn,f(xn), marker = 'o')
plt.show()