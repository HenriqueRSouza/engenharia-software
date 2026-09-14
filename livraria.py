"""Sistema de Livraria - Versão 1.0.0

Módulo simples para gerenciamento e catálogo de livros.
"""

catalogo = []


def adicionar_livro(id_livro: int, titulo: str, autor: str, preco: float) -> dict:
    """Adiciona um novo livro ao catálogo da livraria."""
    livro = {
        "id": id_livro,
        "titulo": titulo,
        "autor": autor,
        "preco": preco,
    }
    catalogo.append(livro)
    return livro


def listar_livros() -> list:
    """Retorna todos os livros cadastrados no catálogo."""
    return catalogo


if __name__ == "__main__":
    print("=== Sistema de Livraria (v1.0.0) ===")
    adicionar_livro(1, "O Alquimista", "Paulo Coelho", 39.90)
    adicionar_livro(2, "Dom Casmurro", "Machado de Assis", 29.90)

    for item in listar_livros():
        print(f"[{item['id']}] {item['titulo']} - {item['autor']} (R$ {item['preco']:.2f})")
