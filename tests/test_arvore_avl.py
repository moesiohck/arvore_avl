"""Testes básicos da implementação de Árvore AVL."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from arvore_avl import NoAVL, buscar, em_ordem, fator_balanceamento, inserir  # noqa: E402


class TesteArvoreAVL(unittest.TestCase):
    def montar_arvore(self, valores: list[int]) -> NoAVL | None:
        raiz = None
        for valor in valores:
            raiz = inserir(raiz, valor)
        return raiz

    def test_rotacao_esquerda_esquerda(self) -> None:
        raiz = self.montar_arvore([30, 20, 10])
        self.assertEqual(raiz.chave, 20)
        self.assertEqual(em_ordem(raiz), [10, 20, 30])

    def test_rotacao_direita_direita(self) -> None:
        raiz = self.montar_arvore([10, 20, 30])
        self.assertEqual(raiz.chave, 20)
        self.assertEqual(em_ordem(raiz), [10, 20, 30])

    def test_rotacao_esquerda_direita(self) -> None:
        raiz = self.montar_arvore([30, 10, 20])
        self.assertEqual(raiz.chave, 20)
        self.assertEqual(em_ordem(raiz), [10, 20, 30])

    def test_rotacao_direita_esquerda(self) -> None:
        raiz = self.montar_arvore([10, 30, 20])
        self.assertEqual(raiz.chave, 20)
        self.assertEqual(em_ordem(raiz), [10, 20, 30])

    def test_busca_encontra_e_nao_encontra(self) -> None:
        raiz = self.montar_arvore([30, 20, 10, 40])
        self.assertIsNotNone(buscar(raiz, 40))
        self.assertIsNone(buscar(raiz, 99))

    def test_valores_repetidos_sao_ignorados(self) -> None:
        raiz = self.montar_arvore([20, 10, 20, 30])
        self.assertEqual(em_ordem(raiz), [10, 20, 30])

    def test_fator_de_balanceamento_da_raiz(self) -> None:
        raiz = self.montar_arvore([30, 20, 10, 40, 50])
        self.assertLessEqual(abs(fator_balanceamento(raiz)), 1)


if __name__ == "__main__":
    unittest.main()
