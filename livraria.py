"""Sistema de Livraria - Versão 1.1.0

Módulo simples para gerenciamento, catálogo e busca de livros.
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


def buscar_livros(termo: str) -> list:
    """Busca livros no catálogo por título ou autor (adicionado na v1.1.0)."""
    resultado = []
    for livro in catalogo:
        if termo in livro["titulo"] or termo in livro["autor"]:
            resultado.append(livro)
    return resultado


if __name__ == "__main__":
    print("=== Sistema de Livraria (v1.1.0) ===")
    adicionar_livro(1, "O Alquimista", "Paulo Coelho", 39.90)
    adicionar_livro(2, "Dom Casmurro", "Machado de Assis", 29.90)
    adicionar_livro(3, "Memórias Póstumas de Brás Cubas", "Machado de Assis", 34.90)

    print("\n--- Todos os Livros ---")
    for item in listar_livros():
        print(f"[{item['id']}] {item['titulo']} - {item['autor']} (R$ {item['preco']:.2f})")

    print("\n--- Busca por 'Machado' ---")
    resultados = buscar_livros("Machado")
    for item in resultados:
        print(f"Encontrado: {item['titulo']} ({item['autor']})")
