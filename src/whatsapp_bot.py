from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_destinatario_mensagem(input_text):
    enviar_para_start = input_text.find('#para:') + len('#para:')
    enviar_para_end = input_text.find('\n', enviar_para_start)
    enviar_para = input_text[enviar_para_start:enviar_para_end].strip()
    menssagem_start = input_text.find('# mensagem:') + len('# mensagem:')
    menssagem_end = input_text.find('***', menssagem_start)
    menssagem = input_text[menssagem_start:menssagem_end].strip()
    return enviar_para, menssagem


def enviar_mensagem(driver, destinatario, mensagem):
    destinatario_search = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
    mensagem_form = driver.find_element(By.XPATH, '//*[@id="main"]/footer[1]/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p')
    destinatario_search.send_keys(destinatario, Keys.RETURN)
    mensagem_form.send_keys(mensagem, Keys.RETURN)


def main():
 
    with open('data/input.txt', 'r', encoding='utf-8') as f:
        input_text = f.read()

    # Obtém o destinatário e a mensagem do arquivo de entrada
    destinatario, mensagem = get_destinatario_mensagem(input_text)

    # Acessa o WhatsApp Web e espera até que o usuário faça login
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div')
            break
        except NoSuchElementException:
            # tratamento para a exceção de elemento não encontrado
            pass

    # Envia a mensagem para o destinatário
    enviar_mensagem(driver, destinatario, mensagem)

    # Fecha o driver
    driver.quit()


if __name__ == '__main__':
    main()
