# Define un array con los nombres de los ficheros
nombres_ficheros = [
    "imports.py", 
    "layername.py", 
    "combinationcounter.py", 
    "main.py"
]

# Define el nombre del fichero de salida
nombre_fichero_salida = "ratascript.py"

# Abre el fichero de salida en modo de escritura
with open(nombre_fichero_salida, "w") as fichero_salida:
    # Itera sobre cada nombre de fichero en el array
    for nombre_fichero in nombres_ficheros:
        # Abre cada fichero en modo de lectura
        with open(nombre_fichero, "r") as fichero_entrada:
            # Lee el contenido del fichero y escribe en el fichero de salida
            fichero_salida.write(fichero_entrada.read())
            fichero_salida.write("\n")