![image](https://github.com/MarreraTech/Zabbix/assets/141791017/937ef0f2-c187-4c1f-a95d-8b2c5afabee6)

# Configuração Zabbix + WhatsApp com Imagem 🛠️📱

## Instalação do Zabbix ✅

Certifique-se de ter o Zabbix devidamente instalado em seu sistema.

## Preparando o Ambiente 🐍

Acesse a máquina onde o Zabbix está instalado e execute os seguintes passos:

- Instale o Python 3: `apt install python3-pip`
- Instale a biblioteca do Zabbix: `pip3 install pyzabbix`

## Configuração do Script 📜

1. Copie o script fornecido pela Marrera.
2. Edite as configurações de acesso para seu Zabbix.
3. Insira o token disponibilizado pela Marrera.

## Adicionando o Script 📂

- Cole o script na pasta `/usr/lib/zabbix/alertscripts`.
- Renomeie o script para incluir a extensão `.py`, por exemplo: `whatsappimages.py`.

## Permissões e Propriedade 🔒👤

- Dê as permissões adequadas ao script: `chmod +x whatsappimages.py`
- Configure a propriedade correta: `chown zabbix:zabbix whatsappimages.py`

## Testando o Script 🧪

- Realize um teste do script: `./whatsappimages.py "Item ID: 84541" TESTE IDDOGRUPO`

  > Para visualizar os IDs de grupos, você pode acessar [este link](https://app.marrera.net/tools/idgrupos.php).

## Configuração no Zabbix ⚙️

Dentro do Zabbix, configure um novo tipo de mídia.

## Configuração da Ação 📢

- Crie uma nova ação, garantindo que contenha a variável `{ITEM.VALUE1}`. Isso será responsável pelo envio da imagem.

## Testando a Ação ✅✔️

- Realize um teste para verificar se tudo está funcionando corretamente.



![image](https://github.com/MarreraTech/Zabbix/assets/141791017/a91e9672-02e3-4651-8c15-71960390bd2b)
