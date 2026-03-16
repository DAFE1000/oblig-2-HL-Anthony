import numpy as np
import matplotlib.pyplot as plt

#--------------------------------------------For ploten-----------------------------------------------------#


## Setter begrensninger for x og y range for ploten som lages
upperLim = 5
lowerLim = -0.5

plt.xlim(lowerLim,upperLim)
plt.ylim(lowerLim,upperLim)


#--------------------------------------------For utregning-------------------------------------------------#


## definerer x verdi range og antall punkter mellom -15 -> 15 
x = np.linspace(-15 , 15 , 1000)


# funksjonen f(x)
def f(x) :
  y = np.power(np.e, -x/4) * np.arctan(x)
  return y


# den deriverte av f(x)
def df(g):
   y = np.arctan(g) - (4/(np.pow(g,2) + 1))
   return y



# variabler for maksimal verdien og tolleransen for loopen
max = 0
tol = 0.0001

# range for g verdier, der det er 2000 like steg mellom 1.5 -> 2. (skal brukes for å finne maksimal punktet)
g = np.linspace(1.5, 2, 3000)


#loop for å sjekke g verdier i den deriverte
for i in g : 

   if -tol <= df(i) <= tol:
      
      max = i
      print("maksimal punkt x verdi =",max)
      print("f(maksimal x) =",f(max))

      break



## ploting av punktet og grafen

plt.plot(x,f(x))
plt.plot(max,f(max), marker = 'o')
plt.show()