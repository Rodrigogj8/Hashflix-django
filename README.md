# Hashflix

Projeto de estudo em Django. A ideia é simular uma plataforma de streaming (tipo Netflix) para colocar em prática conceitos do framework: models, views, templates, admin, autenticação, etc. Não é um produto final — é um repositório que vai crescendo conforme eu for implementando coisas novas.

## Por que esse projeto

Usei Django porque quero treinar desde o básico (rotas, templates, ORM) até coisas mais avançadas que pretendo adicionar depois, como usuários, sessões e relacionamentos entre modelos. O admin já ajuda demais para cadastrar conteúdo sem precisar criar formulário na mão. O plano é ir evoluindo o Hashflix aos poucos e ir documentando aqui o que foi feito e o que ainda falta.

Futuras implementações serão adicionadas conforme o estudo avança. Coisas como login, cadastro, episódios, pesquisa e lista de “já vistos” estão no planejamento e devem entrar em versões posteriores.

## O que tem hoje

- Homepage com layout inspirado em streaming (Tailwind + Bootstrap).
- App `filme` com modelo de Filme (título, thumb, descrição, categoria, visualizações, data).
- Categorias: Análises, Programação, Apresentação, Outros.
- Django Admin configurado para gerenciar filmes.
- Estrutura de templates com base.html e blocos.
- Uso de arquivos estáticos e media (imagens).

O que ainda não tem: autenticação, episódios, barra de pesquisa, contagem de visualizações de verdade, páginas de detalhe por filme. Tudo isso entra na lista de “futuras implementações”.

## Tecnologias utilizadas

- **Python** – linguagem base do projeto.
- **Django 6.0.1** – framework web (models, views, urls, admin, templates, static/media).
- **SQLite** – banco de dados usado no desenvolvimento (vem junto com o Django, zero config).
- **Tailwind CSS** – via CDN no projeto, para estilizar a interface de forma rápida.
- **Bootstrap 5.3.8** – também via CDN, para grid e componentes.
- **Ionicons** – ícones (chevron, etc.) via CDN.

Backend é 100% Django; front é HTML + Tailwind + Bootstrap + ícones, sem JS framework. Templates Django com herança (base.html) e `{% static %}` para CSS e imagens.

## Estrutura do projeto

```
hashflix/
├── filme/              # app principal (filmes/séries)
│   ├── models.py       # modelo Filme e LISTA_CATEGORIAS
│   ├── views.py        # views (ex.: homepage)
│   ├── urls.py         # rotas do app
│   ├── admin.py        # registro do Filme no admin
│   └── templates/      # templates do app
├── hashflix/           # projeto Django (settings, urls raiz)
├── templates/          # base.html, navbar, etc.
├── static/             # CSS, JS, imagens estáticas
└── media/              # uploads (ex.: thumb_filmes)
```

## Como rodar

Requisito: Python instalado (3.8+).

```bash
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abrir `http://127.0.0.1:8000` para a homepage e `http://127.0.0.1:8000/admin` para gerenciar os filmes (usar o superusuário criado).

## Modelo Filme (resumo)

- `titulo` (CharField, 100)
- `thumb` (ImageField, upload em `thumb_filmes`)
- `descricao` (TextField, 1000)
- `categoria` (choices: ANALISES, PROGRAMACAO, APRESENTACAO, OUTROS)
- `visualizacoes` (IntegerField, default 0)
- `data_criacao` (DateTimeField, timezone.now)

## Próximos passos (planejamento)

Conforme o arquivo de planejamento do repositório, a ideia é ir adicionando:

- Login e criação de conta (email, username, senha).
- Filmes já vistos por usuário.
- Episódios com vídeos e títulos.
- Barra de pesquisa.
- Página de detalhe por filme/série e uso real do campo de visualizações.

Tudo isso entra como “futuras implementações” — o projeto é de estudos e vai sendo incrementado aos poucos.
