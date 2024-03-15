# Acesse a pasta alertscripts do Zabbix
cd /usr/lib/zabbix/alertscripts

# Crie e edite o arquivo de script
nano whatsapp.sh

______________________________________________________________________________
#!/bin/bash
SENDTO=$1
SUBJECT=$2
MESSAGE=$3

curl --location -g 'https://apiwt.marrera.net/send-message/id=SEU_TOKEN' \
--header 'Content-Type: application/json' \
--data-raw '{
    "number": "'"$SENDTO"'",
    "textMessage": {
        "text": "'"$SUBJECT \n$MESSAGE"'"
    }
}'
______________________________________________________________________________
# Salve o arquivo (Ctrl + O, Enter, Ctrl + X)

# Dê permissões de execução ao arquivo
chmod +x whatsapp.sh
chown zabbix:zabbix whatsapp.sh

# Teste o script
./whatsapp.sh 5581988887777 "teste" "teste"

# Para enviar para um grupo, insira o ID do grupo no lugar do número

# Configuração no Zabbix:
# 1. Crie um tipo de mídia do tipo script, acionando o nome do script criado.
# 2. Associe essa mídia a um usuário informando o número ou grupo que vai receber as notificações.
# 3. Configure uma ação no Zabbix para utilizar essa mídia.
# 4. Está pronto para ser utilizado!
