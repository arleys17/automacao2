from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    driver.get("https://formulario-contato-m8p8.onrender.com/")
    wait = WebDriverWait(driver, 10)

    # Espera e preenche os campos
    wait.until(EC.presence_of_element_located((By.NAME, "nome"))).send_keys("Uarley Teste")
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("uarley@example.com")
    wait.until(EC.presence_of_element_located((By.NAME, "telefone"))).send_keys("11999998888")
    wait.until(EC.presence_of_element_located((By.NAME, "cidade"))).send_keys("ilhabela")
    wait.until(EC.presence_of_element_located((By.NAME, "bairro"))).send_keys("barrra velha")
    wait.until(EC.presence_of_element_located((By.NAME, "mensagem"))).send_keys("hello guys")
   


    # Localiza o botão e clica com JavaScript (mais seguro)
    botao = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", botao)

    time.sleep(3)



    print("✅ Formulário enviado com sucesso!")
     


except Exception as e:
    print("❌ Erro:", e)

finally:
    driver.quit()
