# Solicita al usuario la palabra a buscar
palabra_clave = input("Ingresa la palabra que deseas filtrar: ") #ocupar una palabra clave para el programa

# Abre el archivo original para lectura y el nuevo archivo para escritura
with open("libro.txt", "r", encoding="utf-8") as archivo_entrada, \
     open("filtrado.txt", "w", encoding="utf-8") as archivo_salida:
      for linea in archivo_entrada:
        if palabra_clave in linea:
            archivo_salida.write(linea)

print("Filtrado completado. Revisa el archivo 'filtrado.txt'.")
    
  