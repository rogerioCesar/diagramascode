import unittest

from reposicao_estoque import (
    ItemReposicao,
    ProdutoEstoque,
    calcular_reposicao,
)


class CalcularReposicaoTests(unittest.TestCase):
    def test_repor_diferenca_para_produto_abaixo_do_minimo(self):
        produtos = [ProdutoEstoque("Cafe", 3, 10)]

        self.assertEqual(
            calcular_reposicao(produtos),
            [ItemReposicao("Cafe", 7)],
        )

    def test_nao_repor_produtos_no_minimo_ou_acima(self):
        produtos = [
            ProdutoEstoque("Cha", 10, 10),
            ProdutoEstoque("Acucar", 12, 10),
        ]

        self.assertEqual(calcular_reposicao(produtos), [])

    def test_preservar_ordem_de_entrada(self):
        produtos = [
            ProdutoEstoque("Cafe", 3, 10),
            ProdutoEstoque("Cha", 1, 4),
        ]

        self.assertEqual(
            calcular_reposicao(produtos),
            [ItemReposicao("Cafe", 7), ItemReposicao("Cha", 3)],
        )

    def test_colecao_vazia_retorna_lista_vazia(self):
        self.assertEqual(calcular_reposicao([]), [])

    def test_rejeitar_quantidade_negativa(self):
        with self.assertRaisesRegex(ValueError, "nao pode ser negativo"):
            ProdutoEstoque("Cafe", -1, 10)

    def test_rejeitar_estoque_minimo_negativo(self):
        with self.assertRaisesRegex(ValueError, "nao pode ser negativo"):
            ProdutoEstoque("Cafe", 1, -1)

    def test_rejeitar_valor_que_nao_seja_inteiro(self):
        with self.assertRaisesRegex(TypeError, "numero inteiro"):
            ProdutoEstoque("Cafe", 2.5, 10)

    def test_rejeitar_booleano_como_quantidade(self):
        with self.assertRaisesRegex(TypeError, "numero inteiro"):
            ProdutoEstoque("Cafe", True, 10)

    def test_rejeitar_nome_vazio(self):
        with self.assertRaisesRegex(ValueError, "texto nao vazio"):
            ProdutoEstoque("  ", 1, 10)

    def test_rejeitar_nome_com_tipo_incorreto(self):
        with self.assertRaisesRegex(TypeError, "nome deve ser um texto"):
            ProdutoEstoque(None, 1, 10)

    def test_rejeitar_item_de_tipo_incorreto(self):
        with self.assertRaisesRegex(TypeError, "ProdutoEstoque"):
            calcular_reposicao(["Cafe"])

    def test_rejeitar_entrada_que_nao_seja_iteravel(self):
        with self.assertRaisesRegex(TypeError, "colecao iteravel"):
            calcular_reposicao(None)


if __name__ == "__main__":
    unittest.main()