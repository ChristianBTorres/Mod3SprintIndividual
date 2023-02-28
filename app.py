import random
import string
usuarios=[]
def password():
    length
    length= 10
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char) for _ in range(length))
    while not (any(x.islower() for x in password) and any(x.isupper() for x in password) and any(x.isdigit() for x in password)):
        password = ''.join(random.choice(char) for _ in range(length))
    return password
    
for i in range(10):
    usuario = f"Usuario N° {i+1}"
    usuarios.append({"user":usuario, "password":password(), "phone":""}) 

print(usuarios)

for x in usuarios:
    
    while True:
        numero = input(f"Ingrese el número para el usuario {x['user']}\n")
        if not numero.isdigit():
            print("Solo debe ingresar números")
        if len(numero)!=8:
            print("El número debe tener un largo de 8 dígitos")
        if numero.isdigit() and len(numero)==8:
            x['phone']=numero
            break
        
for x in usuarios:
    print(x['user'], '\nN° de Teléfono:', x['phone'])
