# Automação

Este projeto foi desenvolvido para realizar automação de preços de protudos de marketplaces do Mercado Libre e Amazon BR.

## O que ele faz?

O projeto permite ao usuario realizar busca automatizadas de preços de produtos de marketplaces do Mercado Libre e Amazon BR. Utilizando o selenium para realizar a automação e a busca dos produtos.
## Instalação

Para fazer a instação você precisara ter o python instalado em seu dispositivo, precisa utilizar o pip ou pipx.

Comando para instalar:

```
pipx install git+https://github.com/marino-matsumoto/desafio_automacao
```
ou 
```
pip install git+https://github.com/marino-matsumoto/desafio_automacao
```

## Comandos

* `automacao -i [item] -o [arquivo.csv] -s [marketplace]` - Executar automação.
* `automacao -h` - Lista de comandos

## Parâmetros

* `-h ou --help` - Mostrar lista de comandos.
* `-i ou --item [item]` - Escolher o item para pesguisar. Obrigatorio.
* `-o, --out ou --output [arquivo.csv]` - Escolher a saída dos dados. Caso não configure este parâmetro por padrão vai ser esolhido o 'marketplace.csv'
* `'-s' ou '--store' [amazon, mercadolivre]` - Escolher o marketplace. Mercado Libre ou Amazon BR.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
```