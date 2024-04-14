import unittest


def contar_vocales(palabra):
    palabra = palabra.lower().replace(" ", "") #Elimina los espacios y las mayusculas
    vocales = ("a","e","i","o","u")
    resultado = {} #Diccionario vacio
    #Entra la palabra
    for letra in palabra:
        #Recorre las letras de la palabra hasta que termine
        if letra in vocales:
            #Si una de las letras es una vocal entra
            if not resultado.get(letra, 0):    #El get sirve para que si no tiene vocal me debuelva none y si queres cambiar el none por 0 haces(letra,0)
                #Si la vocal esta todavia en el resultado se inicializa en 0 y salta al siguiente resultado[letra]+=1
                resultado[letra]= 0
            #Si ya se repitio solo se le suma 1
            resultado[letra]+=1
         
    return resultado
#"""""
#Otra forma de hacer para que no te salte el error NoneType
#"""""
"""""
def contar_vocales_des(palabra: str):  
    resultado = contar_vocales(palabra)
    return resultado.get('a',0), resultado.get('e',0), resultado.get('i',0), resultado.get('o',0), resultado.get('u',0)
"""""

class TestContarVocales(unittest.TestCase):
    def test_sin_vocales(self):
        palabra = "tryhgf"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {})

    def test_con_vocal_o(self):
        palabra = "sol"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 1})

    def test_con_vocal_doble_o(self):
        palabra = "solo"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 2})

    def test_con_dos_vocales(self):
        palabra = "sola"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 1, "a": 1})

    def test_con_todas_las_vocales(self):
        palabra = "solamente quiero que gane Boca"
        resultado = contar_vocales(palabra)
        self.assertEqual(
            resultado,
            {"a": 3, "e": 5, "i": 1, "o": 3, "u": 2},
        )

    def test_con_vocales_en_mayuscula(self):
        palabra = "SOlAmente quIerO"
        resultado = contar_vocales(palabra)
        self.assertEqual(
            resultado,
            {"a": 1, "e": 3, "i": 1, "o": 2, "u": 1},
        )

unittest.main()