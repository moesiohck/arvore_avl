"""Exemplo didático de uma Árvore AVL usando matrículas de alunos."""

from __future__ import annotations


class NoAVL:
    """Representa um nó da Árvore AVL."""

    def __init__(self, chave: int) -> None:
        self.chave = chave
        self.esquerda: NoAVL | None = None
        self.direita: NoAVL | None = None
        self.altura = 1


def altura(no: NoAVL | None) -> int:
    """Retorna a altura do nó. Uma referência vazia tem altura zero."""
    return no.altura if no is not None else 0


def fator_balanceamento(no: NoAVL | None) -> int:
    """Calcula a diferença entre as alturas esquerda e direita."""
    if no is None:
        return 0

    return altura(no.esquerda) - altura(no.direita)


def atualizar_altura(no: NoAVL) -> None:
    """Atualiza a altura considerando os filhos do nó."""
    no.altura = 1 + max(altura(no.esquerda), altura(no.direita))


def rotacao_direita(raiz: NoAVL) -> NoAVL:
    """Executa uma rotação simples para a direita."""
    nova_raiz = raiz.esquerda
    subarvore_transferida = nova_raiz.direita

    nova_raiz.direita = raiz
    raiz.esquerda = subarvore_transferida

    # Atualiza primeiro o nó que desceu e depois a nova raiz.
    atualizar_altura(raiz)
    atualizar_altura(nova_raiz)

    return nova_raiz


def rotacao_esquerda(raiz: NoAVL) -> NoAVL:
    """Executa uma rotação simples para a esquerda."""
    nova_raiz = raiz.direita
    subarvore_transferida = nova_raiz.esquerda

    nova_raiz.esquerda = raiz
    raiz.direita = subarvore_transferida

    # Atualiza primeiro o nó que desceu e depois a nova raiz.
    atualizar_altura(raiz)
    atualizar_altura(nova_raiz)

    return nova_raiz


def inserir(no: NoAVL | None, chave: int) -> NoAVL:
    """Insere uma chave e retorna a raiz da subárvore balanceada.

    Valores repetidos são ignorados neste exemplo.
    """
    if no is None:
        return NoAVL(chave)

    if chave < no.chave:
        no.esquerda = inserir(no.esquerda, chave)
    elif chave > no.chave:
        no.direita = inserir(no.direita, chave)
    else:
        return no

    atualizar_altura(no)
    balanceamento = fator_balanceamento(no)

    # Caso LL: inserção na esquerda do filho esquerdo.
    if balanceamento > 1 and chave < no.esquerda.chave:
        return rotacao_direita(no)

    # Caso RR: inserção na direita do filho direito.
    if balanceamento < -1 and chave > no.direita.chave:
        return rotacao_esquerda(no)

    # Caso LR: inserção na direita do filho esquerdo.
    if balanceamento > 1 and chave > no.esquerda.chave:
        no.esquerda = rotacao_esquerda(no.esquerda)
        return rotacao_direita(no)

    # Caso RL: inserção na esquerda do filho direito.
    if balanceamento < -1 and chave < no.direita.chave:
        no.direita = rotacao_direita(no.direita)
        return rotacao_esquerda(no)

    return no


def buscar(no: NoAVL | None, chave: int) -> NoAVL | None:
    """Procura uma chave e retorna o nó encontrado ou None."""
    if no is None or no.chave == chave:
        return no

    if chave < no.chave:
        return buscar(no.esquerda, chave)

    return buscar(no.direita, chave)


def em_ordem(no: NoAVL | None) -> list[int]:
    """Retorna as chaves em ordem crescente."""
    if no is None:
        return []

    return em_ordem(no.esquerda) + [no.chave] + em_ordem(no.direita)


def exibir_arvore(no: NoAVL | None, nivel: int = 0, lado: str = "raiz") -> None:
    """Exibe a árvore de forma simples, começando pelos nós mais altos."""
    if no is None:
        return

    exibir_arvore(no.direita, nivel + 1, "direita")
    print("    " * nivel + f"{lado}: {no.chave}")
    exibir_arvore(no.esquerda, nivel + 1, "esquerda")


def main() -> None:
    """Executa o exemplo de cadastro e busca de matrículas."""
    raiz: NoAVL | None = None
    matriculas = [30, 20, 10]

    for matricula in matriculas:
        raiz = inserir(raiz, matricula)

    print("Matriculas cadastradas em ordem crescente:")
    print(*em_ordem(raiz))

    print("\nEstrutura da arvore apos o balanceamento:")
    exibir_arvore(raiz)

    matricula_procurada = 30
    print(f"\nBuscando a matricula {matricula_procurada}...")

    if buscar(raiz, matricula_procurada) is not None:
        print(f"Matricula {matricula_procurada} encontrada!")
    else:
        print(f"Matricula {matricula_procurada} nao encontrada.")


if __name__ == "__main__":
    main()
