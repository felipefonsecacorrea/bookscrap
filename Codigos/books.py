import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "http://books.toscrape.com/"

driver.get(url)
time.sleep(1)

links = driver.find_elements(By.TAG_NAME, 'a')
print(links)
print(len(links))

x = driver.find_elements(By.TAG_NAME, 'a')[0].text
print(x)
print(f'Total de Letras no Nome: {len(x)}')

y = driver.find_elements(By.TAG_NAME, 'a')[0].get_attribute('title')
print(y)

# print(driver.find_elements(By.TAG_NAME, 'a')[54:92:1])

elementostitulo = driver.find_elements(By.TAG_NAME, 'a')[54:92:2]

listatitulo = [title.get_attribute('title') for title in elementostitulo]
#print(listatitulo)

#elementostitulo[0].click()
#time.sleep(1)
#stok = driver.find_element(By.CLASS_NAME, 'instock').text
#print(stok)
#time.sleep(1)

#estoque = int(stok.replace("In stock (", "").replace("available)", ""))
#print(estoque)

#driver.back()

listaestoque = []

for titulo in elementostitulo:
    titulo.click()
    time.sleep(0.2)
    quantidade = int(driver.find_element(By.CLASS_NAME, 'instock').text.replace("In stock (", "").replace("available)", ""))
    listaestoque.append(quantidade)
    driver.back()
    time.sleep(0.2)

data = {'Titulo': listatitulo, 'Estoque': listaestoque}

print(pd.DataFrame(data))

dados = pd.DataFrame(data)
dados.to_excel("dados.xlsx")

