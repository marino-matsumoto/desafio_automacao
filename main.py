from selenium import webdriver
from selenium.webdriver.common.by import By

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

# Primeiro item
navegador.find_element(By.CLASS_NAME, 'ui-search-result__wrapper').click()

# Nome do produto
nome_produto = navegador.find_element(By.CLASS_NAME, 'ui-pdp-title').text

# Descrição
descricao_produto = navegador.find_element(By.CLASS_NAME, 'ui-pdp-description__content').text

# Vendedor
vendedor_produto = navegador.find_element(By.CLASS_NAME, 'ui-seller-data-header__title').text

# Preço inteiro
preco_inteiro = navegador.find_element(By.CLASS_NAME, 'andes-money-amount__fraction').text

# Preço fracionario
preco_fracionario = navegador.find_element(By.CLASS_NAME, 'andes-money-amount__cents').text

image_elmento_produto_url = navegador.find_element(By.CLASS_NAME, 'ui-pdp-image')
imagem_produto = image_elmento_produto_url.get_attribute("src")

text_file = f"""Nome do produto: {nome_produto}
Preço do produto: R${preco_inteiro},{preco_fracionario}
Descrição do produto: {descricao_produto}
URL da imagem: {imagem_produto}
Vendedor do produto: {vendedor_produto}"""

with open("produto.txt", "w") as file:
    file.write(text_file)


navegador.quit()