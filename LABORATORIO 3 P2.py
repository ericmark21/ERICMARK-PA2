
print("Bienvenido al programa\n")
print("REGISTRO DE VEHICULOS DE TRES EJES \n")
cont=0 
promedio=0
suma=0
lista=[]
while (True):
    try:
        #peso= float(input("Registre el peso de su vehiculo en toneladas: "))
        while (True):
            peso= float(input("Registre el peso de su vehiculo en toneladas: "))
            if (peso ==0): 
                break
            else:
                lista.append(peso)
                suma+= peso
                if(peso>=22):
                    cont+= 1
        promedio=sum(lista)/len(lista)
                       
    except:
        print("Ha ocurrido un error, digite solo numeros, no palabras")
    else:
        print("Lista de los pesos ingresados: ")
        print(lista)
        print(f"el promedio es: {promedio}")
        print(f"Vehiculos quesobrepasan las 22 toneladas: {int(cont)}")
        
