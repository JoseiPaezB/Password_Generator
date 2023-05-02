from random import randint
archivo=open('Claves.txt',"a")

s=""
#print("Hola tu clave del dia de hoy es: ")
print("Menu")
w=int(input("1.Para generar una clave \n2.Para crear una clave \n "))
if w==1:
    print
    n=input("Para que deseas esta clave: ")
    password=[]
    i=randint(0,8)
    caracteres=["!","#","$","%","^","&","*","(",")","-","~","+","=","?"]
    letras=["a","e","i","u","x","y","z"]
    #letras=["aeiouxyz"]
    for i in range(1,8):
        z=randint(0,10)
        a=randint(0,13)
        j=randint(0,6)
        password.append(str(z))
        caracter=caracteres[a]
        password.append(caracter)
        letra=letras[j]
        password.append(letra)
    s=''.join(password)
    s=s+"\n"
    n=n+":"+"\t"
    #print(s)
    archivo.write("\nGenerated Password\n")
    archivo.write(n)
    archivo.write(s)
    archivo.close()
    
if w==2:
    clave=input("Digita la clave: ")
    s=input("De que es la clave: ")
    clave=clave+"\n"
    s=s+":"+"\t"
    archivo.write("\nPersonal Password\n")
    archivo.write(s)
    archivo.write(clave)
    archivo.close()

