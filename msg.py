from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
import time
from selenium.webdriver.common.keys import Keys

# Inicializa o serviço com o caminho do geckodriver
service = Service('geckodriver.exe')  # Substitua pelo caminho correto se necessário
driver = webdriver.Firefox(service=service)

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com/")
print("Pressione Enter depois de escanear o QR code e carregar o WhatsApp Web completamente...")
input()  # Aguarda o usuário pressionar Enter

while True:
    # Pergunta ao usuário qual grupo enviar a mensagem
    nome_grupo = input("Digite o nome do grupo ou contato: ")
    
    # Aguarda até que o campo de pesquisa esteja visível e busca pelo grupo
    try:
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='3']"))
        )
        search_box.click()
        search_box.clear()  # Limpa o campo de pesquisa antes de inserir o novo grupo
        search_box.send_keys(nome_grupo)

        # Aguarda até que o grupo apareça na lista
        group = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f"//span[@title='{nome_grupo}']"))
        )
        group.click()
    except Exception as e:
        print(f"Erro ao localizar o grupo: {e}")
        continue  # Se não encontrar o grupo, volta para o início do loop para tentar novamente

    # Aguarda até que o campo de mensagem esteja visível
    try:
        campo_mensagem = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='10']"))
        )

        # Pergunta qual mensagem enviar
        mensagem = input("Digite a mensagem a ser enviada: ")
        
        # Envia a mensagem
        campo_mensagem.click()  # Clica no campo de mensagem
        campo_mensagem.clear()  # Limpa o campo de mensagem

        # Envia a mensagem caractere por caractere para garantir que seja enviada completa
        for caractere in mensagem:
            campo_mensagem.send_keys(caractere)
            time.sleep(0.05)  # Espera um pouco entre os caracteres

        time.sleep(0.5)  # Aguardando um pouco para garantir que o texto foi inserido
        campo_mensagem.send_keys(Keys.RETURN)  # Pressiona Enter para enviar
        print("Mensagem enviada!")
        
    except Exception as send_error:
        print(f"Erro ao enviar mensagem: {send_error}")

    # Limpa o campo de pesquisa antes da próxima iteração
    search_box.clear()

# Finaliza o driver (não será alcançado no loop acima, mas é uma boa prática)
driver.quit()
