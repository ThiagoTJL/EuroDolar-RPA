#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[4]:


from selenium import webdriver

abrir_navegador = webdriver.Chrome()
abrir_navegador.get("https://www.google.com/")


# In[9]:


# importando o selenium para trabalhar com as páginas da web
from selenium import webdriver as opcoes_selenium
from selenium.webdriver.common.keys import Keys

# importando a biblioteca pyautogui para trabalhar com pausa
import pyautogui as tempoPausa

# usando By para trabalhar com as atualizações mais recentes
from selenium.webdriver.common.by import By

# passamos autorização ao acesso as configurações do Chrome
meuNavegador = opcoes_selenium.Chrome()
meuNavegador.get("https://www.google.com/")
tempoPausa.sleep(4)
meuNavegador.find_element(By.NAME, "q").send_keys("Dolar hoje")
tempoPausa.sleep(4)

# retorna para o campo q
meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)
tempoPausa.sleep(4)

# procura o elemento do valor do dólar
valorDolar = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
print(valorDolar)

#-----------------------------------------------------------------------------------------------------

meuNavegador.find_element(By.NAME, "q").send_keys("")
tempoPausa.sleep(4)
tempoPausa.press("tab")
tempoPausa.sleep(2)
tempoPausa.press("enter")
tempoPausa.sleep(2)
meuNavegador.find_element(By.NAME, "q").send_keys("Euro hoje")
tempoPausa.sleep(2)
meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)
tempoPausa.sleep(2)
valorEuro = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
print(valorEuro)



# In[11]:


get_ipython().system('pip install xlsxwriter')


# In[21]:


import xlsxwriter
import os
from selenium import webdriver as opcoes_selenium
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoPausa
from selenium.webdriver.common.by import By
import datetime

# passamos autorização ao acesso as configurações do Chrome
meuNavegador = opcoes_selenium.Chrome()
meuNavegador.get("https://www.google.com/")
tempoPausa.sleep(4)
meuNavegador.find_element(By.NAME, "q").send_keys("Dolar hoje")
tempoPausa.sleep(4)

# retorna para o campo q
meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)
tempoPausa.sleep(4)

# procura o elemento do valor do dólar
valorDolar = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
print(valorDolar)

#-----------------------------------------------------------------------------------------------------

meuNavegador.find_element(By.NAME, "q").send_keys("")
tempoPausa.sleep(4)
tempoPausa.press("tab")
tempoPausa.sleep(2)
tempoPausa.press("enter")
tempoPausa.sleep(2)
meuNavegador.find_element(By.NAME, "q").send_keys("Euro hoje")
tempoPausa.sleep(2)
meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)
tempoPausa.sleep(2)
valorEuro = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
print(valorEuro)


#--------------------------------------------------------------------------------------------------
nomeCaminhoArquivo = "C:\\Users\\lemes\\OneDrive\\Área de Trabalho\\Projeto\\Dolar e Euro Google.xlsx"
planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo)
planilha1 = planilhaCriada.add_worksheet()
planilha1.write("A1", "Moeda")
planilha1.write("A2", "Dolar")
planilha1.write("A3", "Euro")
planilha1.write("B1", "Valor")
planilha1.write("B2", valorDolar)
planilha1.write("B3", valorEuro)
planilhaCriada.close()
os.startfile(nomeCaminhoArquivo)


# In[ ]:





# In[ ]:




