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

def descriptografar(texto_criptografado, deslocamento):
    # A descriptografia é o inverso, então aplicamos o deslocamento negativo
    return criptografar(texto_criptografado, -deslocamento)

texto_recuperado = descriptografar(texto_criptografado, 3)
print(f"Texto Recuperado: {texto_recuperado}")

if texto_original == texto_recuperado:
    print("Sucesso: A lógica de segurança está funcionando perfeitamente!")
