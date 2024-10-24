🐍 WhatsApp Automation Script

Este projeto consiste em um script Python que automatiza o envio de mensagens para um grupo ou contato específico no WhatsApp Web utilizando a biblioteca Selenium.
📋 Requisitos

Antes de executar o script, você precisará configurar o ambiente conforme as instruções abaixo:
1. Instalação do Selenium

Você pode instalar a biblioteca Selenium usando o pip. Execute o seguinte comando no terminal:

bash

pip install selenium

2. Download do GeckoDriver

O GeckoDriver é necessário para interagir com o navegador Firefox. Siga as instruções abaixo para baixar e configurar o GeckoDriver:
🖥️ Windows

    Baixe o GeckoDriver:
        Acesse a página de lançamentos do GeckoDriver no GitHub.
        Baixe o arquivo ZIP correspondente à sua versão do Windows (ex: geckodriver-vX.XX-win64.zip).

    Extraia o arquivo ZIP:
        Extraia o conteúdo do ZIP para uma pasta de sua escolha.

    Adicione o caminho ao GeckoDriver ao seu PATH:
        Copie o caminho onde o geckodriver.exe foi extraído.
        Pesquise por "Variáveis de Ambiente" no menu Iniciar e abra as Configurações de Variáveis de Ambiente.
        No campo "Variáveis do sistema", encontre e selecione a variável Path, clique em "Editar" e adicione o caminho copiado.

🍏 macOS

    Baixe o GeckoDriver:
        Acesse a página de lançamentos do GeckoDriver no GitHub.
        Baixe o arquivo correspondente ao macOS (ex: geckodriver-vX.XX-macos.tar.gz).

    Extraia o arquivo:

    bash

tar -xvzf geckodriver-vX.XX-macos.tar.gz

Mova o GeckoDriver para uma pasta no seu PATH:

bash

    sudo mv geckodriver /usr/local/bin/

🐧 Linux

    Baixe o GeckoDriver:
        Acesse a página de lançamentos do GeckoDriver no GitHub.
        Baixe o arquivo correspondente ao Linux (ex: geckodriver-vX.XX-linux64.tar.gz).

    Extraia o arquivo:

    bash

tar -xvzf geckodriver-vX.XX-linux64.tar.gz

Mova o GeckoDriver para uma pasta no seu PATH:

bash

    sudo mv geckodriver /usr/local/bin/

3. Executando o Script

    Abra o terminal ou o prompt de comando.

    Navegue até o diretório onde o seu script está salvo.

    Execute o script:

    bash

    python msg.py

    Aguarde a abertura do WhatsApp Web:
        O script solicitará que você escaneie o QR code do WhatsApp Web. Após escanear, pressione Enter no terminal.

    O script começará a enviar mensagens automaticamente.

⚙️ Configurações do Script

    Nome do grupo ou contato: Altere a variável nome_grupo para o nome do grupo ou contato que deseja enviar mensagens.

python

nome_grupo = "nome do contato ou do grupo"

    Mensagem a ser enviada: Modifique a variável mensagem para personalizar a mensagem que será enviada.

python

mensagem = "Mensagem enviada automaticamente com script python"

🤝 Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções no script. Você pode abrir um issue ou enviar um pull request.
📜 Licença

Este projeto é licenciado sob a MIT License.
