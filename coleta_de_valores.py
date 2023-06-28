import pandas as pd
from selenium import webdriver as driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

option = driver.ChromeOptions()
option.add_argument('--headless=new')

driver = driver.Chrome(options=option)
driver.get('https://www.mercadolivre.com.br/')

#aceitando cookies
driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div[3]/button[1]').click()


search = str(input("Digite o produto para buscar: "))
tag = driver.find_element(By.TAG_NAME,'input')
tag.clear()
tag.send_keys(search)
tag.send_keys(Keys.ENTER)



produtos = driver.find_elements(By.CLASS_NAME,'ui-search-result__content')

print(f'foi encontrado {len(produtos)}: produtos\nAguarde, estamos coletando os dados!')

lista_nome = []
lista_value = []
lista_link = []

for inf in produtos:
    nome_produto = inf.find_element(By.TAG_NAME,'h2').text
    valor = inf.find_element(By.CLASS_NAME,'price-tag-fraction').text
    link = inf.find_element(By.TAG_NAME,'a').get_attribute('href')

    lista_nome.append(nome_produto)
    lista_value.append(valor)
    lista_link.append(link)  

driver.quit()


dados = {'nome_produto': lista_nome,'valor':lista_value,'link':lista_link}

df = pd.DataFrame(dados)

df.to_csv('pesquisa_de_valores_mercadoLivre.csv',encoding='utf8',index=None, sep='*')

print('Finalizado!')

print(df)