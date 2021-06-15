from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("C:\\Bibs\\chromedriver.exe")

def enviarMensagem(contato, msg, count):
    driver.get("https://web.whatsapp.com")
    print("Scaneie o QR Code.")
    wait = WebDriverWait(driver, 20)

    el_contato = wait.until(EC.presence_of_element_located((By.XPATH, f'//span[@title="{contato}"]')))
    if el_contato is None:
        print("Contato não encontrado")
        driver.quit()
        quit()
    else:
        el_contato.click()
        print("Usuário encontrado")

    time.sleep(2)

    for i in range(count):
        try:
            el_click_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]'))) 
            el_click_input.click()
            el_click_input.send_keys(msg)
            print("Mensagem digitada")
        except:
            print("Falha ao encontrar o campo de input")
            driver.quit()
            quit()

        # time.sleep(1)

        try:
            el_send = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[3]/button/span')))
            el_send.click()
            print("Mensagem enviada")            
        except:
            print("Falha ao encontrar o campo de input")
            driver.quit()
            quit()

        # time.sleep(1)

    driver.quit()
    quit()

if __name__ == "__main__":
    f = open("travazap", "r", encoding="utf8")

    nome_contato = "Gustavo Voz"
    # mensagem = "Spam"
    mensagem = f.read()
    
    enviarMensagem(nome_contato, mensagem, 20)

