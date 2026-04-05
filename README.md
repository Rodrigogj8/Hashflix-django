# Hashflix

Projeto de estudo em Django: uma plataforma de streaming simples (filmes e séries) para praticar models, views, templates, admin, autenticação e formulários. O foco é aprendizado; o código e a interface vão evoluindo aos poucos.

## O que o projeto faz hoje

- **Homepage** com captura de e-mail e redirecionamento para login ou cadastro.
- **Catálogo** (`/filmes/`) com destaque, novidades, em alta, grade geral e lista do que o usuário já marcou como visto.
- **Detalhe do título** com sinopse, episódios (links externos) e sugestões semelhantes.
- **Busca** por nome do filme na barra superior (usuários autenticados).
- **Conta**: cadastro, login, logout, edição de perfil e alteração de senha.
- **Admin** do Django para gerenciar filmes, categorias e conteúdo.

Interface em **português (pt-BR)**, com Tailwind CSS (CDN), Bootstrap 5 (formulários via Crispy Forms), Ionicons e layout escuro alinhado ao tema de streaming.

## Tecnologias

| Uso | Stack |
|-----|--------|
| Backend | Python, **Django 6** |
| Banco | SQLite (desenvolvimento) |
| Templates | Django Templates, herança com `base.html` |
| Estilo | Tailwind CSS (CDN), Bootstrap 5.3 |
| Formulários | **django-crispy-forms** + **crispy-bootstrap5** |
| Mídia | `static/` e `media/` (thumbs, uploads) |

## Estrutura (resumo)

```
hashflix/
├── filme/                 # app principal
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   └── templates/
├── hashflix/              # settings, urls raiz
├── templates/             # base.html, navbar.html
├── static/
└── media/
```

## Como rodar localmente

1. Crie um ambiente virtual (recomendado) e instale as dependências:

```bash
pip install django django-crispy-forms crispy-bootstrap5 pillow
```

2. Aplique migrações e crie um superusuário:

```bash
python manage.py migrate
python manage.py createsuperuser
```

3. Suba o servidor:

```bash
python manage.py runserver
```

- Site: `http://127.0.0.1:8000`
- Admin: `http://127.0.0.1:8000/admin`

Cadastre filmes no admin (thumbnail, descrição, categoria, etc.) para popular o catálogo.

## Modelo principal (ideia)

O modelo de filme inclui título, capa, descrição, categoria, visualizações e data de criação; há suporte a episódios e relação com usuários para títulos vistos (conforme implementação no app `filme`).

## Licença e autor

Projeto pessoal de estudos. Autor: **Rodrigogj8**.
