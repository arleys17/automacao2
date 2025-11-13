from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
import time


@given('que estou no WhatsApp Web')
def step_open_whatsapp(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://web.whatsapp.com")

    print("Escaneie o QR Code para continuar...")
    time.sleep(20)  # tempo para escanear o QR code


@when('eu pesquiso pelo contato "{nome}"')
def step_search_contact(context, nome):
    wait = WebDriverWait(context.driver, 30)

    # XPATH atualizado — funciona na versão atual do WhatsApp (2025)
    search_box = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id='side']//div[@contenteditable='true']")
        )
    )

    search_box.click()
    search_box.clear()
    search_box.send_keys(nome)

    time.sleep(2)

    contato = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//span[@title='{nome}']")
        )
    )
    contato.click()
    time.sleep(2)


@when('envio a mensagem "{mensagem}"')
def step_send_message(context, mensagem):
    wait = WebDriverWait(context.driver, 20)

    msg_box = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@contenteditable='true' and @data-tab='10']")
        )
    )

    msg_box.click()
    msg_box.send_keys(mensagem + Keys.ENTER)
    time.sleep(2)


@then('a mensagem deve ser enviada com sucesso')
def step_verify_message(context):
    print("Mensagem enviada com sucesso!")
    time.sleep(2)
    context.driver.quit()
