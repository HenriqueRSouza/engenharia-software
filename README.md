# Sistema de Livraria — Engenharia de Software

Projeto acadêmico desenvolvido para demonstrar na prática os conceitos de controle de versão de software e **Semantic Versioning (SemVer)** no contexto de um sistema de livraria.

- **Aluno:** Henrique Ribeiro — 10401770
- **Colaborador:** Eduardo Ferreira de Mattos

---

## 📌 Objetivo do Exercício

Demonstrar a evolução controlada de uma aplicação através de tags e convenções semânticas (`MAJOR.MINOR.PATCH`):

1. **MAJOR (`v2.0.0`)**: Mudança estrutural incompatível (Breaking Change).
2. **MINOR (`v1.1.0`)**: Adição de funcionalidade mantendo retrocompatibilidade.
3. **PATCH (`v1.1.1`)**: Correção de bug sem quebra de compatibilidade.

---

## 🏷️ Histórico de Versões e Tags

| Versão | Tipo SemVer | Descrição |
| :--- | :--- | :--- |
| **`v1.0.0`** | Versão Inicial | Primeira versão estável: catálogo básico procedural, cadastro e listagem. |
| **`v1.1.0`** | MINOR | Adiciona função de busca de livros (`buscar_livros`) por título ou autor. |
| **`v1.1.1`** | PATCH | Correção na busca: suporte a busca case-insensitive e remoção de espaços extras. |
| **`v2.0.0`** | MAJOR | **Breaking Change**: Reestruturação completa para Orientação a Objetos (`Livraria` e `Livro`). |

---

## ⚠️ Detalhes da Breaking Change (v1.x ➔ v2.0.0)

- **Versões v1.x (Procedural)**:
  - Utilizava funções globais (`adicionar_livro`, `listar_livros`, `buscar_livros`) e catálogo em lista de dicionários com chaves inteiras `id`.
- **Versão v2.0.0 (Orientada a Objetos)**:
  - O sistema passa a ser gerenciado pela classe `Livraria` e as entidades passam a ser instâncias da classe `Livro` identificadas por `isbn` e `categoria`.
  - As chamadas procedurais antigas não são compatíveis, exigindo adaptação do código cliente.

---

## 🚀 Como Executar

Execute o módulo principal:

```bash
python livraria.py
```