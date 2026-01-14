# Guia de contribuição

## Clonar o projeto
Garanta que seu ssh esteja configurado no git e no github.

Utilizar o comando:

```bash
git clone git@github.com:marino-matsumoto/desafio_automacao.git
```

## Instalar projeto

Instalar o poetry na maquina.

```bash
pipx install poetry
```

Instalar a versão correta do python.

```bash
poetry python install 3.13
```

Configurar o python do poetry.

```bash
poetry env use 3.13
```

Instalar o projeto.

```bash
poetry install
```

## Documentação

A documentação do projeto esta em docs. Para poder mostrar a documentação utilize o comando server.

```bash
poetry run mkdocs serve
```

## Contribuição

Apos a modificação do projeto fazer um fragmento(De CHANGELOG) depois o commit.

```bash
poetry run towncrier create
```

Commit:

```bash
git add <nome do arquivo que mudou>
```

```bash
git commit -m "Sua descrição"
```

```bash
git push
```

## Como gerar a release

1. Alterar a versão do pyproject.toml
2. Criar o changelog utilizando o towncrier

    `towncrier build --version <versão>`

3. Criar a tag

    `git tag <versão>`

4. Pública a tag

    `git push --tags`

