import random
print('Δώσε μου έναν όρο της ακολουθίας fibonacci.')
n=int(input('> '))
y=0
n1=0 
n2=1
n3=0
if n<0:
  print('Δεν υπάρχει   ')
elif n<=2:
 print('Ο',n, 'ος όρος της ακολουθίας fibonacci δεν είναι πρώτος.')
else:
  for i in range(n-1):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
  for i in range(20):
    a=random.randint(0,999999)
    if (a ** n3 ) % n3 == (a % n3 ):
      y=y+1
    else:
      print('Ο',n, 'ος όρος δεν είναι πρώτος.')
      break    
  if y==20:
    print('Ο', n, 'ος όρος είναι πρώτος.')
