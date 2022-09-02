from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from numpy import random

import time
import urllib
import pandas as pd


contatos = pd.read_excel("Enviar.xlsx")
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements(By.ID, value='side')) < 1:
    time.sleep(1)

mensagems = contatos.loc[0, "Mensagem"]

for i, mensagem in enumerate(contatos["Mensagem"]):
    pessoa = contatos.loc[i, "Pessoa"]
    numero = contatos.loc[i, "Numero"]
    
    texto = urllib.parse.quote(f"{mensagems}")
    link = f"https://web.whatsapp.com/send?phone=55{numero}&text={texto}"

    navegador.get(link)
    time.sleep(5)

    if not (navegador.find_elements(By.CLASS_NAME, '_3J6wB')):
        while len(navegador.find_elements(By.ID, value='side')) < 1:
            time.sleep(1)

        while not (navegador.find_elements(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')):
            time.sleep(1)

        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()

        numeroRand = random.randint(5,30)
        time.sleep(numeroRand)
    else:
        time.sleep(5)
