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

# Nome do grupo
nome_grupo = "nome do contato ou do grupo"

# Aguarda até que o campo de pesquisa esteja visível e busca pelo grupo
try:
    search_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='3']"))
    )
    search_box.click()
    search_box.send_keys(nome_grupo)
    
    # Aguarda até que o grupo apareça na lista
    group = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, f"//span[@title='{nome_grupo}']"))
    )
    group.click()
except Exception as e:
    print(f"Erro ao localizar o grupo: {e}")

# Aguarda até que o campo de mensagem esteja visível
try:
    # Use o novo XPATH baseado na sua descrição
    campo_mensagem = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='10']"))
    )
    
    # Envia mensagens em intervalos de 60 segundos
    while True:
        try:
            campo_mensagem.click()  # Clica no campo de mensagem
            campo_mensagem.clear()  # Limpa o campo de mensagem
            mensagem = "Mensagem enviada automaticamente com script python"  # Mensagem a ser enviada

            # Envia a mensagem caractere por caractere para garantir que seja enviada completa
            for caractere in mensagem:
                campo_mensagem.send_keys(caractere)
                time.sleep(0.05)  # Espera um pouco entre os caracteres

            time.sleep(0.5)  # Aguardando um pouco para garantir que o texto foi inserido
            campo_mensagem.send_keys(Keys.RETURN)  # Pressiona Enter para enviar
            print("Mensagem enviada!")
            time.sleep(15)  # Aguarda 60 segundos antes de enviar a próxima mensagem
        except Exception as send_error:
            print(f"Erro ao enviar mensagem: {send_error}")
            break  # Sai do loop se houver erro ao enviar a mensagem
except Exception as e:
    print(f"Erro ao encontrar o campo de mensagem: {e}")

# Finaliza o driver (não será alcançado no loop acima, mas é uma boa prática)
driver.quit()
