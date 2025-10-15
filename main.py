from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import csv
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--item', required=True, help="Item que vai ser pesquisado.")
parser.add_argument('-o', '--out', '--output', default='marketplace.csv', help="Arquivo csv que vai baixar.")
parser.add_argument('-s', '--store', type=str, choices=['amazon', 'mercadolivre'],  required=True, help="O marketplace a ser utilizado.")

args = parser.parse_args()

if not args.out.endswith(".csv"):
    raise Exception("Arquivo obrigatoriamente precisa ser csv")

if args.store == 'amazon':
    # Iniciando navegador Firefox.
    navegador = webdriver.Firefox()

    # Tela cheia
    navegador.maximize_window()

    # link para encurtar
    url = "https://www.amazon.com.br/"


    # Acessar a página do marketplace.
    navegador.get(url)


    # Tempo de espera para carregar a página.
    navegador.implicitly_wait(1.0)

    # Localiza a barra de pesquisa e escrever.
    el = navegador.find_element(By.ID, "twotabsearchtextbox")
    el.send_keys(args.item)

    el = navegador.find_element(By.ID, "nav-search-submit-button")
    el.click()

    # Tempo de espera de 1 segundo
    navegador.implicitly_wait(1.0)
    # Primeiro item
    navegador.find_element(By.CLASS_NAME, 'puis-card-container').click()

    # Tempo de espera de 1 segundo
    navegador.implicitly_wait(1.0)

    # Nome do produto
    nome_produto = navegador.find_element(By.ID, 'productTitle').text

    # Descrição
    descricao_produto = navegador.find_element(By.CLASS_NAME, 'a-expander-partial-collapse-content').text

    descricao_produto = descricao_produto.replace("\n", "")

    # Vendedor
    vendedor_produto = navegador.find_element(By.ID, 'sellerProfileTriggerId').text

    # Preço inteiro
    preco_inteiro = navegador.find_element(By.CLASS_NAME, 'a-price-whole').text

    # Preço fracionario
    preco_fracionario = navegador.find_element(By.CLASS_NAME, 'a-price-fraction').text

    # Imagem do produto
    image_elmento_produto_url = navegador.find_element(By.CLASS_NAME, 'a-dynamic-image')
    imagem_produto = image_elmento_produto_url.get_attribute("src")

    # Data
    data = datetime.today().strftime("%d-%m-%Y")

    with open(args.out, "a", newline="") as file:
        campos_head = ['date','url','title','description','image_url','seller', 'marketplace']
        writer = csv.DictWriter(file, fieldnames=campos_head, delimiter=';')
    
        if file.tell() == 0:
            writer.writeheader()
            writer.writerow({'date':data,'url':navegador.current_url,'title':nome_produto,'description':descricao_produto,'image_url':imagem_produto,'seller':vendedor_produto, 'marketplace':url})
        else:
            writer.writerow({'date':data,'url':navegador.current_url,'title':nome_produto,'description':descricao_produto,'image_url':imagem_produto,'seller':vendedor_produto, 'marketplace':url})
    print(args.out)
    navegador.quit()

elif args.store == 'mercadolivre':
    # Iniciando navegador Firefox.
    navegador = webdriver.Firefox()

    # Tela cheia
    navegador.maximize_window()

    # link para encurtar
    url = "https://www.mercadolivre.com.br/"

    # Acessar a página do marketplace.
    navegador.get(url)


    # Tempo de espera para carregar a página.
    navegador.implicitly_wait(1.0)

    # Localiza a barra de pesquisa e escrever.
    el = navegador.find_element(By.ID, "cb1-edit")
    el.send_keys(args.item)

    el = navegador.find_element(By.CLASS_NAME, "nav-icon-search")
    el.click()

    # Tempo de espera de 1 segundo
    navegador.implicitly_wait(1.0)
    # Primeiro item
    navegador.find_element(By.CLASS_NAME, 'ui-search-result__wrapper').click()

    # Tempo de espera de 1 segundo
    navegador.implicitly_wait(1.0)

    # Nome do produto
    nome_produto = navegador.find_element(By.CLASS_NAME, 'ui-pdp-title').text

    # Descrição
    descricao_produto = navegador.find_element(By.CLASS_NAME, 'ui-pdp-description__content').text

    descricao_produto = descricao_produto.replace("\n", "")

    # Vendedor
    vendedor_produto = navegador.find_element(By.CLASS_NAME, 'ui-seller-data-header__title').text

    # Preço inteiro
    preco_inteiro = navegador.find_element(By.CLASS_NAME, 'andes-money-amount__fraction').text

    # Preço fracionario
    preco_fracionario = navegador.find_element(By.CLASS_NAME, 'andes-money-amount__cents').text

    # Imagem do produto
    image_elmento_produto_url = navegador.find_element(By.CLASS_NAME, 'ui-pdp-image')
    imagem_produto = image_elmento_produto_url.get_attribute("src")

    # Data
    data = datetime.today().strftime("%d-%m-%Y")

    with open(args.out, "a", newline="") as file:
        campos_head = ['date','url','title','description','image_url','seller', 'marketplace']
        writer = csv.DictWriter(file, fieldnames=campos_head, delimiter=';')
    
        if file.tell() == 0:
            writer.writeheader()
            writer.writerow({'date':data,'url':navegador.current_url,'title':nome_produto,'description':descricao_produto,'image_url':imagem_produto,'seller':vendedor_produto, 'marketplace':url})
        else:
            writer.writerow({'date':data,'url':navegador.current_url,'title':nome_produto,'description':descricao_produto,'image_url':imagem_produto,'seller':vendedor_produto, 'marketplace':url})
    print(args.out)
    navegador.quit()
else:
    raise Exception("Arquivo obrigatoriamente precisa ser csv")