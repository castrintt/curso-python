from conhecendo_unittest import par_impar, converte_padrao as cv
import unittest

class ConhecendoUnittestTeste(unittest.TestCase): # é bom nomear as classes com o mesmo nome do modulo testado!
    # COMO CONVENÇÃO É INTERESSANTE PASSAR UMA FUNÇÃO PARA CADA ASSERT!!

    # por convenção usamos test_nomeDaFunção para declarar as funções de teste
    def test_converte_padrao_tarde(self): # recebe self, pois a classe herda de TestCase, que por usa vez tem os metodos vistos no link do arquivo conhecendo_unittest.py
        """

        """
        self.assertEqual(cv(14,25), '2:25 P.M', 'deu erro!') 
        #como vimos na tabela o assertEqual testa dois valores (nesse caso vamos testar o retorno da função convert_padrao, passando 2 parametros, para ver se ela é igual ao segundo parametro definido no assert, ('2:25 P.M') e logo o terceiro parametro é uma mensagem de erro caso não passe nos testes)
        # logo 1 e 2 ( parametros ) --> são para testar um ao outro
        # 3 -> mensagem de erro caso falhe

    def test_convert_padrao_manha(self):
        self.assertEqual(cv(8,10),'8:10 A.M')



    def test_type_return(self):
        self.assertIs(type(cv(8,10)), str )
        # nesse caso estamos testando se o tipo do retorno final da função converte_padrao é str (nesse caso sem retornar uma mensagem de erro se não for)
     
    
    def test_par(self):
        self.assertTrue(par_impar(4))

    def teste_impar(self):
        self.assertFalse(par_impar(5))



if __name__ == '__main__': # essa linha é necessaria pois podemos importar o modulo testes, reaproveitando para outros sistemas, e assim não realizar os testes toda vez que for executado o programa!
    unittest.main()  # o comando unittest.main() ele cria a interface e realiza os testes em si!, enquanto nos casos acima nós só mostramos quais testes queremos executar


# se executarmos o codigo no terminal usando --> python3 nomeDoArquivo.py , ele nos retorna o seguinte erro ( falhas )

# FF4 é par
# .F5 é impar
# F
# ======================================================================
# FAIL: test_convert_padrao_manha (__main__.ConhecendoUnittestTeste)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "testes_unittest.py", line 15, in test_convert_padrao_manha
#     self.assertEqual(cv(8,10),'8:10 A.M')
# AssertionError: None != '8:10 A.M'

# ======================================================================
# FAIL: test_converte_padrao_tarde (__main__.ConhecendoUnittestTeste)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "testes_unittest.py", line 9, in test_converte_padrao_tarde
#     self.assertEqual(cv(14,25), '2:25 P.M', 'deu erro!')
# AssertionError: None != '2:25 P.M' : deu erro!

# ======================================================================
# FAIL: test_type_return (__main__.ConhecendoUnittestTeste)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "testes_unittest.py", line 20, in test_type_return
#     self.assertIs(type(cv(8,10)), str )
# AssertionError: <class 'NoneType'> is not <class 'str'>

# ======================================================================
# FAIL: teste_impar (__main__.ConhecendoUnittestTeste)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "testes_unittest.py", line 28, in teste_impar
#     self.assertFalse(par_impar(5))
# AssertionError: 5 is not false

# ----------------------------------------------------------------------
# Ran 5 tests in 0.001s

# FAILED (failures=4)




#                       temos primeiro a implementação do codigo (onde nos guiara para os testes), segundo temos os testes de fato, e terceiro a refatoração do codigo

# apos refatorar as funções e rodar os testes de novo o retorno é esse

# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s

# OK


# após terminar os testes, temos que documentar as funções dentro do unittest.TestCase , explicando que esta dentro do codigo

# 

from conhecendo_unittest import par_impar, converte_padrao as cv
import unittest

class ConhecendoUnittestTeste(unittest.TestCase):

    # por convenção usamos test_nomeDaFunção para declarar as funções de teste
    def test_converte_padrao_tarde(self): # recebe self, pois a classe herda de TestCase, que por usa vez tem os metodos vistos no link do arquivo conhecendo_unittest.py
        """
            DOCUMENTAÇÃO --> função que testa se o horario ja passou das 12 hrs
        """
        self.assertEqual(cv(14,25), '2:25 P.M', 'deu erro!') 
        #como vimos na tabela o assertEqual testa dois valores (nesse caso vamos testar o retorno da função convert_padrao, passando 2 parametros, para ver se ela é igual ao segundo parametro definido no assert, ('2:25 P.M') e logo o terceiro parametro é uma mensagem de erro caso não passe nos testes)
        # logo 1 e 2 ( parametros ) --> são para testar um ao outro
        # 3 -> mensagem de erro caso falhe

    def test_convert_padrao_manha(self):
        """
        Função que testa se o horario é antes de 12 horas
        """
        self.assertEqual(cv(8,10),'8:10 A.M')



    def test_type_return(self):
        """
            função que testa o tipo do retorno 
        """
        self.assertIs(type(cv(8,10)), str )
        # nesse caso estamos testando se o tipo do retorno final da função converte_padrao é str (nesse caso sem retornar uma mensagem de erro se não for)
     
    
    def test_par(self):
        """
            função que retorna true caso o numero seja par
        """
        self.assertTrue(par_impar(4))

    def teste_impar(self):
        """
            função que retorna true caso o numero seja impar
        """
        self.assertFalse(par_impar(5))


# temos um modo de abertura para ver mais detalhes dos testes, que é o modo de abertura -v

# por tanto no terminal vamos digitar a seguinte linha --> python3 nomeDoArquivo.py -v

# nos retorna o seguinte::

# test_convert_padrao_manha (__main__.ConhecendoUnittestTeste) ... ok
# test_converte_padrao_tarde (__main__.ConhecendoUnittestTeste) ... ok
# test_par (__main__.ConhecendoUnittestTeste) ... ok
# test_type_return (__main__.ConhecendoUnittestTeste) ... ok
# teste_impar (__main__.ConhecendoUnittestTeste) ... ok

# ----------------------------------------------------------------------
# Ran 5 tests in 0.001s