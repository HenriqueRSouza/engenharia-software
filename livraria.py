"""Sistema de Livraria - Versão 2.0.0

BREAKING CHANGE: Reestruturação completa do sistema para Orientação a Objetos (OO).
As funções procedurais da v1.x foram substituídas pelas classes Livro e Livraria.
"""

from typing import List


class Livro:
    """Entidade que representa um livro com ISBN e metadados."""

    def __init__(self, isbn: str, titulo: str, autor: str, preco: float, categoria: str = "Geral"):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.categoria = categoria

    def __repr__(self) -> str:
        return f"Livro(isbn='{self.isbn}', titulo='{self.titulo}', autor='{self.autor}', preco={self.preco:.2f})"


class Livraria:
    """Gerenciador do catálogo da livraria."""

    def __init__(self, nome: str):
        self.nome = nome
        self._acervo: List[Livro] = []

    def cadastrar_livro(self, livro: Livro) -> None:
        """Cadastra um novo livro no acervo."""
        self._acervo.append(livro)

    def listar_todos(self) -> List[Livro]:
        """Retorna todos os livros cadastrados."""
        return list(self._acervo)

    def buscar(self, termo: str) -> List[Livro]:
        """Busca livros por título, autor ou categoria (case-insensitive)."""
        termo_normalizado = termo.strip().lower()
        return [
            livro
            for livro in self._acervo
            if termo_normalizado in livro.titulo.lower()
            or termo_normalizado in livro.autor.lower()
            or termo_normalizado in livro.categoria.lower()
        ]

    def quantidade_total(self) -> int:
        """Retorna a quantidade de livros no acervo."""
        return len(self._acervo)


if __name__ == "__main__":
    print("=== Sistema de Livraria (v2.0.0 - Orientado a Objetos) ===")
    livraria = Livraria("Livraria Central")

    livraria.cadastrar_livro(Livro("978-8575427583", "O Alquimista", "Paulo Coelho", 39.90, "Ficção"))
    livraria.cadastrar_livro(Livro("978-8535914849", "Dom Casmurro", "Machado de Assis", 29.90, "Clássico"))
    livraria.cadastrar_livro(Livro("978-8572328128", "Memórias Póstumas de Brás Cubas", "Machado de Assis", 34.90, "Clássico"))

    print(f"\nTotal no acervo: {livraria.quantidade_total()} títulos")

    print("\n--- Acervo Completo ---")
    for item in livraria.listar_todos():
        print(f"[{item.isbn}] {item.titulo} - {item.autor} (R$ {item.preco:.2f}) | {item.categoria}")

    print("\n--- Busca por 'Clássico' ---")
    for item in livraria.buscar("clássico"):
        print(f"Encontrado: {item.titulo} ({item.autor})")
