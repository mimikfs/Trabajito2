# 2.- Contador de palabras en un archivo: Crea un programa que lea un archivo llamado “articulo.txt” y cuente cuántas veces aparece una palabra específica proporcionada por el usuario.
wSearch=input("Ingrese la palabra que desea buscar: ").lower()
try:
    # Se ejecuta el archivo en modo de lectura
    with open("articulo.txt", 'r', encoding="utf-8") as archivo: 
       
       #Se divide el texto en palabras y se contaran cuantas veces aparece la palabra buscada 
       contenido=archivo.read().lower() # Leer el texto en minuscula
       wordS=contenido.split()
       cont=wordS.count(wSearch)
       print("La palabra '(wSearch)', aparece (cont) veces el arcivo.")

except FileNotFoundError: # En caso de no encontrar el archivo, se ejecuta error
 print("El archivo 'archivo.txt' no se encontró")