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

# Testando a função
texto_original = "Projeto DevOps"
texto_criptografado = criptografar(texto_original, 3)

print(f"Texto Original: {texto_original}")
print(f"Texto Criptografado: {texto_criptografado}")
