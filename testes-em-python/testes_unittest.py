from conhecendo_unittest import par_impar, converte_padrao as cv
import unittest

class ConhecendoUnittestTeste(unittest.TestCase): # é bom nomear as classes com o mesmo nome do modulo testado!

    def teste_converte_padrao(self): # recebe self, pois a classe herda de TestCase, que por usa vez tem os metodos vistos no link do arquivo conhecendo_unittest.py
        self.assertEqual(cv(14,25), '2:25 P.M', 'deu erro!') 
        #como vimos na tabela o assertEqual testa dois valores (nesse caso vamos testar o retorno da função convert_padrao, passando 2 parametros, para ver se ela é igual ao segundo parametro definido no assert, ('2:25 P.M') e logo o terceiro parametro é uma mensagem de erro caso não passe nos testes)
        # logo 1 e 2 ( parametros ) --> são para testar um ao outro
        # 3 -> mensagem de erro caso falhe
        self.assertEqual(cv(8,10),'8:10 A.M')
        self.assertIs(type(cv(8,10)), str )
        # nesse caso estamos testando se o tipo do retorno final da função converte_padrao é str (nesse caso sem retornar uma mensagem de erro se não for)
     
# parei em 20 min