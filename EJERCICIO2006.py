# EJERCICIO 6 / Buscar una palabra y reemplazarla por otra

palabra_especifica=input("Ingrese la palabra que desea buscar: ")
palabra_reemplazo=input("Ingrese la palabra con la que desea reemplazarla: ")

try:
    with open ("documento.txt","r", encoding="utf-8") as archivo:
        lineas=archivo.readlines()
    lineas_nuevas=[]
    for linea in lineas:
        palabras=linea.split()
        linea_nueva=[]
        for palabra in palabras:
            if palabra==palabra_especifica:
                linea_nueva.append(palabra_reemplazo)
            else:
                linea_nueva.append(palabra)
        
        lineas_nuevas.append(" ".join(linea_nueva))
        
    with open("modificado.txt","w",encoding="utf-8") as archivo_modificado:
        for linea in lineas_nuevas:
            archivo_modificado.write(linea+"\n")
    
    print ("Se ha creado el archivo modificado con los cambios ingresados")

except FileNotFoundError:
    print("El archivo no fue encontrado!")
