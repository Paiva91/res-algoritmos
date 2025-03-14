def eh_palindromo(frase):
    frase = frase.replace(" ", "").lower()
    return frase == frase[::-1]

entrada = input("Digite uma frase: ")

if eh_palindromo(entrada):
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
