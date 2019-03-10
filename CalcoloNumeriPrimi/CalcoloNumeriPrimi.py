import math # sqrt()
###################################### Numero Primo? Si/No 
def primo(x):
   if(x   == 2): return True
   if(x%2 == 0): return False
   ultimo=int(math.sqrt(x))
   for i in range(3, ultimo+1,2):
      if(x%i == 0):
         return False
   return True
###################################### 

nmax = int(input('Inserisci nmax: '))
print (' \n')
print ('Questi sono i numeri primi compresi tra 1 e ', nmax, ' \n')
for numero in range(nmax):
    if(primo(numero)):
      print(numero)
      numero+=1
TheEnd = input ("Premi invio")
 
