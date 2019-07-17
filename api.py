import requests

KEY = "4e9fcd9d"
URL = "http://www.omdbapi.com/?apikey="
#titulo = "The Matrix"

# busqueda = URL + KEY + "&t=" + titulo
# resultado = requests.get(busqueda)
# print(resultado.json())

# Crear un función que reciba como parámetro el nombre de una película
# y que retorne el nombre del director de la pelicula usando el 
# API de OMDB

KEY = "4e9fcd9d"
URL = "http://www.omdbapi.com/?apikey="

def director_name():
    title = input("Nombre de la película: ")
    busqueda = URL + KEY + "&t=" + title
    resultado = requests.get(busqueda)
    return resultado.json()["Director"]

print(director_name())