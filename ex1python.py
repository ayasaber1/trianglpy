# Fonction pour convertir décimal en binaire

def DecimalToBinary(num):

if num >= 1:
DecimalToBinary(num // 2)
print(num % 2, end = '')


if __name__ == '__main__':

# valeur en décima
dec_val = 24

# appelé la fonction
DecimalToBinary(dec_val)

def binaryToDecimal(n):
   return int(n,2)


Var1= float(input("Donner la 1er longueur du triangle \n"))
Var2= float(input("Donner la 2er longueur du triangle \n"))
Var3= float(input("Donner la 3er longueur du triangle \n"))

if Var1 == Var2 and Var2== Var3:
   print("triangle est equilatéral \n")
elif Var1 == Var2 and Var3!= Var2 or Var2== Var3 and Var1!= Var2 or Var1 == Var3 and Var2!= Var1:
   print("triangle est isocèle \n")
else:
   print("triangle est scalène \n")
