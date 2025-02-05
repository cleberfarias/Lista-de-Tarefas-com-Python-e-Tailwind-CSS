# Aplicação de Lista de Tarefas com Python e Tailwind CSS

Este projeto é uma aplicação simples de lista de tarefas desenvolvida como parte de um estudo sobre Python (usando Flask) e Tailwind CSS.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal
- **Flask**: Framework web para Python
- **SQLAlchemy**: ORM (Object-Relational Mapping) para interação com o banco de dados
- **Tailwind CSS**: Framework CSS para estilização rápida e responsiva

## Aprendizados

## Tecnologias Utilizadas

- Flask: Framework web em Python para desenvolvimento do backend.

- SQLAlchemy: ORM para gerenciamento do banco de dados embarcado na aplicação.

- Tailwind CSS: Framework CSS para estilização rápida e responsiva.

- Flask-Testing: Extensão para facilitar testes em aplicações Flask.

### Python e Flask

- Criação de rotas em Flask
- Uso de decoradores para definir funções de visualização
- Integração com SQLAlchemy para operações de banco de dados
- Renderização de templates usando Jinja2

### Tailwind CSS

- Utilização de classes utilitárias para estilização rápida
- Design responsivo sem escrever CSS personalizado
- Customização de componentes como botões e inputs
- Uso de flexbox e grid para layout

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask
- `templates/lista.html`: Template HTML para a página principal
- `README.md`: Este arquivo, contendo informações sobre o projeto

## Como Executar

## Criando e Ativando o Ambiente Virtual

- python -m venv venv
# No Windows
- venv\Scripts\activate
# No macOS/Linux
- source venv/bin/activate

1. Instale as dependências:

- pip install flask flask-sqlalchemy
- python app.py
- pytest test.py

## Estrutura do Projeto 

📂 CRUD
│-- 📂 instance
│   ├── tarefas.db  # Banco de dados SQLite
│-- 📂 templates
│   ├── lista.html  # Página HTML principal
│-- 📂 venv  # Ambiente virtual
│   ├── Scripts/  # Arquivos do ambiente virtual
│-- app.py  # Código principal da aplicação
│-- test.py  # Arquivo de testes
│-- README.md  # Documentação do projeto
│-- .gitignore  # Arquivos ignorados pelo Git
