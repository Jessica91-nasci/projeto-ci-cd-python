import unittest
from main import criptografar, descriptografar


class TestCriptografia(unittest.TestCase):

    # Teste 1: Verifica se a criptografia básica funciona
    def test_criptografia_simples(self):
        self.assertEqual(criptografar("abc", 1), "bcd")

    # Teste 2: Verifica se a descriptografia básica reverte o texto
    def test_descriptografia_simples(self):
        self.assertEqual(descriptografar("bcd", 1), "abc")

    # Teste 3: Verifica se espaços e caracteres especiais são ignorados (não embaralhados)
    def test_espacos_e_simbolos(self):
        self.assertEqual(criptografar("a b!", 1), "b c!")

    # Teste 4: Verifica o comportamento com letras maiúsculas e minúsculas misturadas
    def test_maiusculas_minusculas(self):
        self.assertEqual(criptografar("DevOps", 3), "GhyRsv")

    # Teste 5: Verifica se um deslocamento de zero mantém o texto idêntico
    def test_deslocamento_zero(self):
        self.assertEqual(criptografar("teste", 0), "teste")


if __name__ == '__main__':
    unittest.main()
