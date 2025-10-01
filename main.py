from selenium import webdriver
from selenium.webdriver.common.by import By

# Iniciando navegador Firefox.
navegador = webdriver.Firefox()

# Tela cheia
navegador.maximize_window()

# link para encurtar
url = "https://www.mercadolivre.com.br/memoria-ram-valueram-verde-4gb-1-kingston-kvr1333d3s94g-15v/p/MLB6065670?has_official_store=false&highlight=true&headerTopBrand=false#polycard_client=search-nordic&search_layout=grid&position=4&type=product&tracking_id=f63bb904-4df9-4074-975a-992019c2f36f&wid=MLB4020351181&sid=search"

# Acessar a página do marketplace.
navegador.get(url)

# Tempo de espera para carregar a página.
navegador.implicitly_wait(1.0)

navegador.quit()