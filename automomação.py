from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def enviar_mensagem_whatsapp(contato, mensagem):
    # Iniciar o driver do Chrome
    driver = webdriver.Chrome()

    # Acessar o WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    print("Aguarde a leitura do código QR pelo WhatsApp Web...")
    time.sleep(20)

    # Localizar o campo de pesquisa
    campo_pesquisa = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')

    # Digitar o nome do contato na caixa de pesquisa
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(2)  # Esperar alguns segundos para carregar a conversa

    # Localizar o campo de digitação de mensagem
    campo_mensagem = driver.find_element(By.XPATH,
                                         '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')

    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)

    # Esperar alguns segundos para enviar a mensagem
    time.sleep(2)

    driver.quit()


# Exemplo de uso da função
contato = 'Luanzin'  # Substitua pelo nome exato do contato na sua lista do WhatsApp
mensagem = f'Bom Dia!,{contato}'
enviar_mensagem_whatsapp(contato, mensagem)