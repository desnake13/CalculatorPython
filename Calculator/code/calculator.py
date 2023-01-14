# calculator  / calcolatrice

#functions / funzioni
# This function adds two numbers
def addizione(x,y):
    return x + y

# This function subtracts two numbers
def sottrazione(x,y):
    return x - y

# This function multiplies two numbers
def moltiplicazione(x,y):
    return x * y

# This function divides two numbers
def divisione(x,y):
    return x / y

print("--------- Calculator ---------")

print("----- Scegli l'operazione -----")
print("1-Addizione")
print("2-Sottrazione")
print("3-Moltiplicazione")
print("4-Divisione")

while True:

     scelta = input("Scegli (1/2/3/4): ")

     if scelta in ("1","2","3","4"):
         num1 = float(input("Inserisci il primo numero: "))
         num2 = float(input("Inserisci il secondo numero: "))


         if scelta == "1":
             print(num1, "+", num2, "=", addizione(num1, num2))

         if scelta == "2":
             print(num1, "-", num2, "=", sottrazione(num1, num2))

         if scelta == "3":
             print(num1, "*", num2, "=", moltiplicazione(num1, num2))

         if scelta == "4":
             print(num1, "+", num2, "=", divisione(num1, num2))

         restart = input("Vuoi fare ancora calcoli? (si/no): ")
         if restart != "si":
             break
         else:
             print("\n")

     else:
         print("input invalido")


