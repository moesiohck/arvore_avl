# Árvore AVL: tecnologias, caso de uso e exemplo prático

Este projeto apresenta uma implementação simples de uma **Árvore AVL** usando Python. O conteúdo foi organizado para estudar os três pontos da atividade de Estrutura de Dados Avançada:

1. Tecnologias utilizadas;
2. Proposta de caso de uso;
3. Construção de um exemplo simples e detalhado.

## 1. Tecnologias

A Árvore AVL é uma árvore binária de busca que mantém seu próprio balanceamento durante as inserções. Isso evita que a estrutura fique muito inclinada para um dos lados e tenha o desempenho de uma lista encadeada.

As tecnologias e os conceitos utilizados neste projeto são:

- **Python 3:** linguagem usada para implementar a estrutura;
- **Árvore binária de busca:** cada nó pode ter um filho à esquerda e outro à direita. Os valores menores ficam à esquerda e os maiores à direita;
- **Fator de balanceamento:** diferença entre a altura da subárvore esquerda e a altura da subárvore direita;
- **Rotações:** operações que reorganizam os nós quando a árvore fica desbalanceada.

A implementação utiliza apenas recursos nativos do Python, portanto não é necessário instalar bibliotecas externas.

### Como funciona o balanceamento?

Em uma Árvore AVL, o fator de balanceamento de cada nó deve ficar entre `-1` e `1`.

O cálculo é:

```text
Fator de balanceamento = altura da subárvore esquerda - altura da subárvore direita
```

Quando uma inserção faz esse fator sair do intervalo permitido, a árvore realiza uma rotação para recuperar o equilíbrio. Existem quatro situações principais:

- **Esquerda-esquerda (LL):** rotação simples para a direita;
- **Direita-direita (RR):** rotação simples para a esquerda;
- **Esquerda-direita (LR):** rotação para a esquerda no filho e depois para a direita no nó;
- **Direita-esquerda (RL):** rotação para a direita no filho e depois para a esquerda no nó.

## 2. Proposta de caso de uso

Um possível uso da Árvore AVL é em um **sistema de cadastro de alunos** de uma instituição de ensino.

Imagine uma escola que possui milhares de alunos. Cada aluno tem uma matrícula única, que pode ser usada como chave para localizar seu cadastro. Como o sistema precisa consultar essas matrículas com frequência, é interessante manter os registros organizados para facilitar as buscas.

A Árvore AVL pode armazenar as matrículas em ordem. Ao inserir uma nova matrícula, ela é posicionada de acordo com seu valor e a estrutura verifica automaticamente se precisa realizar alguma rotação.

Por exemplo, ao inserir as matrículas `30`, `20` e `10`, a árvore inicialmente fica inclinada para a esquerda. A AVL identifica o desequilíbrio e realiza uma rotação para a direita. O resultado passa a ser:

```text
       20
      /  \
    10    30
```

Nesse cenário, a matrícula `20` fica na raiz, `10` fica à esquerda e `30` fica à direita. A organização permite encontrar uma matrícula sem precisar percorrer todos os registros.

Esse exemplo é uma demonstração didática. Em um sistema real, os dados completos dos alunos poderiam ser armazenados em cada nó, enquanto a matrícula seria usada como chave de busca.

## 3. Exemplo prático em Python

O arquivo [`src/arvore_avl.py`](src/arvore_avl.py) contém a implementação. Ele cria os nós, calcula alturas, identifica desequilíbrios, executa rotações, insere matrículas e realiza buscas.

### Requisitos

- Python 3.9 ou superior;
- Nenhuma biblioteca externa.

### Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python src/arvore_avl.py
```

### Código utilizado

O código está separado do README para facilitar a leitura e a execução. O programa principal insere as matrículas `30`, `20` e `10`, mostra os valores em ordem crescente e procura a matrícula `30`.

### Resultado esperado

```text
Matriculas cadastradas em ordem crescente:
10 20 30

Estrutura da arvore apos o balanceamento:
       20
      /  \
    10    30

Buscando a matricula 30...
Matricula 30 encontrada!
```

### Entendendo o exemplo passo a passo

1. **Primeira inserção — 30:** como a árvore está vazia, o número `30` se torna a raiz.
2. **Segunda inserção — 20:** como `20` é menor que `30`, ele é colocado à esquerda.
3. **Terceira inserção — 10:** como `10` é menor que `30` e menor que `20`, ele é colocado à esquerda de `20`.
4. **Verificação do equilíbrio:** o nó `30` fica com fator de balanceamento igual a `2`, ultrapassando o limite permitido.
5. **Rotação:** a árvore executa uma rotação simples para a direita. O nó `20` passa a ser a raiz, mantendo `10` à esquerda e `30` à direita.
6. **Busca:** para procurar `30`, o programa compara o valor com a raiz `20`. Como `30` é maior, segue para a direita e encontra o nó.

### Complexidade

| Operação | Complexidade média e no pior caso em uma AVL |
|---|---:|
| Busca | `O(log n)` |
| Inserção | `O(log n)` |
| Percurso em ordem | `O(n)` |

A busca e a inserção permanecem em `O(log n)` porque a árvore se mantém balanceada. Já o percurso em ordem visita todos os nós, por isso tem custo `O(n)`.

## Como executar os testes

O projeto também contém testes automatizados para verificar os quatro casos de rotação, a busca e o comportamento com valores repetidos.

Na pasta principal, execute:

```bash
python -m unittest discover -s tests -v
```

## Conclusão

A Árvore AVL é útil quando uma aplicação precisa inserir e procurar informações mantendo os dados organizados. Seu principal diferencial é o balanceamento automático, que evita que a árvore fique muito alta e prejudique o desempenho das operações. O exemplo de matrículas demonstra como esse processo acontece na prática.

---

**Disciplina:** Estrutura de Dados Avançada  
**Tema:** Árvore AVL  
**Linguagem:** Python
