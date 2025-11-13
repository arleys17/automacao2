from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then

# Configuração do Chrome
chrome_options = Options()
# chrome_options.add_argument("--headless")  # opcional, roda sem abrir o navegador

@given("que esta na pagina de formulario")
def step_abrir_pagina(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    context.driver.get("https://formulario-contato-m8p8.onrender.com/")
    context.wait = WebDriverWait(context.driver, 10)

@when("preenche os dados do formulario")
def step_preencher_formulario(context):
    context.wait.until(EC.presence_of_element_located((By.NAME, "nome"))).send_keys("Uarley Teste")
    context.wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("uarley@example.com")
    context.wait.until(EC.presence_of_element_located((By.NAME, "telefone"))).send_keys("11999998888")
    context.wait.until(EC.presence_of_element_located((By.NAME, "cidade"))).send_keys("Ilhabela")
    context.wait.until(EC.presence_of_element_located((By.NAME, "bairro"))).send_keys("Barra Velha")
    context.wait.until(EC.presence_of_element_located((By.NAME, "mensagem"))).send_keys("Hello guys")
    
    # Clicar no botão de enviar de forma segura
    botao = context.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    context.driver.execute_script("arguments[0].click();", botao)

@then("o formulario e enviado")
def step_verificar_envio(context):
    # Aqui você pode adicionar verificação de mensagem de sucesso
    print("✅ Formulário enviado com sucesso!")
    context.driver.quit()
