print("Iniciando o sistema de Criptografia Simples")

print("Iniciando o sistema de Criptografia Simples")

def criptografar(texto, deslocamento):
    resultado = ""
    for caractere in texto:
        if caractere.isalpha():
            codigo = ord(caractere) + deslocamento
            resultado += chr(codigo)
        else:
            resultado += caractere
    return resultado
