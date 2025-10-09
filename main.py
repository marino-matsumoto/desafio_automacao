from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import csv
import argparse

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
el.send_keys("Livro")

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

with open("produtos.csv", "a", newline="") as file:
    campos_head = ['date','url','title','description','image_url','seller']
    writer = csv.DictWriter(file, fieldnames=campos_head, delimiter=';')
    
    if file.tell() == 0:
        writer.writeheader()
    else:
        writer.writerow({'date':data,'url':navegador.current_url,'title':nome_produto,'description':descricao_produto,'image_url':imagem_produto,'seller':vendedor_produto})
print(file)
navegador.quit()