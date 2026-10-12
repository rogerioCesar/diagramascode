"""Calcula reposicoes necessarias para produtos abaixo do estoque minimo."""

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True)
class ProdutoEstoque:
    nome: str
    quantidade_disponivel: int
    estoque_minimo: int

    def __post_init__(self) -> None:
        if not isinstance(self.nome, str):
            raise TypeError("nome deve ser um texto")
        if not self.nome.strip():
            raise ValueError("nome deve ser um texto nao vazio")

        for campo, quantidade in (
            ("quantidade_disponivel", self.quantidade_disponivel),
            ("estoque_minimo", self.estoque_minimo),
        ):
            if isinstance(quantidade, bool) or not isinstance(quantidade, int):
                raise TypeError(f"{campo} deve ser um numero inteiro")
            if quantidade < 0:
                raise ValueError(f"{campo} nao pode ser negativo")


@dataclass(frozen=True)
class ItemReposicao:
    nome_produto: str
    quantidade_repor: int


def calcular_reposicao(
    produtos: Iterable[ProdutoEstoque],
) -> list[ItemReposicao]:
    """Retorna, na ordem de entrada, apenas produtos abaixo do minimo."""
    if not isinstance(produtos, Iterable):
        raise TypeError("produtos deve ser uma colecao iteravel")

    itens_reposicao = []
    for produto in produtos:
        if not isinstance(produto, ProdutoEstoque):
            raise TypeError("cada item deve ser um ProdutoEstoque")

        quantidade_faltante = produto.estoque_minimo - produto.quantidade_disponivel
        if quantidade_faltante > 0:
            itens_reposicao.append(
                ItemReposicao(produto.nome, quantidade_faltante)
            )

    return itens_reposicao