import re
from typing import Dict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from processos_destinatario import processos_destinatario

def processar_mensagens(input_text: str):
    # busca por números de processo no texto
    numeros_processo = re.findall(r'\d{7}-\d{2}\.\d{4}\.\d{1}\.\d{2}\.\d{4}', input_text)
    numeros_processo = set(numeros_processo)  # converte a lista em um set de valores únicos
    processos_destinatario = {num: "" for num in numeros_processo}  # cria o dicionário com as chaves como números de processo

    # busca por números de processo não presentes no dicionário processos_destinatario e atribui a eles a chave "não enviar"
    for num in re.findall(r'\d{7}-\d{2}\.\d{4}\.\d{1}\.\d{2}\.\d{4}', input_text):
        if num not in processos_destinatario:
            processos_destinatario[num] = "não enviar"

    # Separando as mensagens do arquivo
    mensagens = input_text.split('***\n\n')

    # Criando o dicionário de mensagens processadas
    mensagens_processadas = {}
    for mensagem in mensagens:
        # Obtendo o nome do destinatário da mensagem
        destinatario = None
        for processo, nome in processos_destinatario.items():
            if processo in mensagem:
                destinatario = nome
                break

        # Se não houver destinatário correspondente, atribui a chave "não enviar"
        if destinatario is None:
            destinatario = "não enviar"

        # Obtendo o texto da mensagem
        menssagem_start = mensagem.find('#para:') + len('#para:')
        menssagem_end = mensagem.find('***', menssagem_start)
        menssagem = mensagem[menssagem_start:menssagem_end].strip()

        # Adicionando a mensagem ao dicionário de mensagens processadas
        if destinatario in mensagens_processadas:
            mensagens_processadas[destinatario].append(menssagem)
        else:
            mensagens_processadas[destinatario] = [menssagem]

    return mensagens_processadas


def enviar_mensagem(driver, destinatario, mensagem):
    destinatario_search = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
    mensagem_form = driver.find_element(By.XPATH, '//*[@id="main"]/footer[1]/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p')
    destinatario_search.send_keys(destinatario, Keys.RETURN)
    mensagem_form.send_keys(mensagem, Keys.RETURN)


def main():
    with open('input.txt', 'r') as f:
        input_text = f.read()

    # busca por números de processo no texto
    numeros_processo = re.findall(r'\d{7}-\d{2}\.\d{4}\.\d{1}\.\d{2}\.\d{4}', input_text)
    numeros_processo = set(numeros_processo)  # converte a lista em um set de valores únicos
    processos_destinatario = {num: [] for num in numeros_processo}  # cria o dicionário com as chaves como números de processo

    # separa as mensagens do arquivo
    mensagens = input_text.split('***\n\n')

    # processa as mensagens e adiciona aos dicionários de mensagens a serem enviadas
    mensagens_processadas = {}
    for mensagem in mensagens:
        # Obtendo o número do processo da mensagem
        processo_encontrado = False
        for num_proc in numeros_processo:
            if num_proc in mensagem:
                processo_encontrado = True
                for destinatario, procs in processos_destinatario.items():
                    if num_proc in procs:
                        # Obtendo o texto da mensagem
                        mensagem_start = mensagem.find('#para:') + len('#para:')
                        mensagem_end = mensagem.find('***', mensagem_start)
                        mensagem_texto = mensagem[mensagem_start:mensagem_end].strip()

                        # Adicionando a mensagem ao dicionário de mensagens processadas
                        if destinatario in mensagens_processadas:
                            mensagens_processadas[destinatario].append(mensagem_texto)
                        else:
                            mensagens_processadas[destinatario] = [mensagem_texto]

                        break
                else:
                    processos_destinatario["não enviar"].append(num_proc)
        if not processo_encontrado:
            print(f"AVISO: Nenhum número de processo encontrado na mensagem: {mensagem}")

    # Acessa o WhatsApp Web e espera até que o usuário faça login
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )

        # Envia as mensagens para os destinatários correspondentes
        for destinatario, mensagens in mensagens_processadas.items():
            for mensagem in mensagens:
                enviar_mensagem(driver, destinatario, mensagem)
    finally:
        # Fecha o driver
        driver.quit()

