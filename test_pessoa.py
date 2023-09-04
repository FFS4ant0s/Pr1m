# class Pessoa:
#     __init__
#         nome : str
#         sobrenome : str
#         dados_obtidos : bool
    
#     API:
#         obter_todos_os_dados -> method
#             OK
#             404
import unittest
from unittest.mock import patch
from Pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Fernando', 'Fernandes')
    
    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Fernando')
    
    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Fernandes')

if __name__ == '__main__':
    unittest.main(verbosity=2)