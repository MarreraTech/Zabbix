# Envio de Alertas Zabbix via API do WhatsApp 📡📲

Este script de Zabbix permite o envio de alertas, dados e imagens para grupos ou números do WhatsApp, proporcionando uma integração eficaz.

![Marrera Tech Logo](https://github.com/MarreraTech/Zabbix/assets/141791017/f79c274c-56ca-4d3b-aa1f-8ce416e21dae)

Para usar esse script é necessário que o usuário contrate uma instância API do WhatsApp com a Marrera Tech.
Para utilizar este script, é necessário contratar uma instância da API do WhatsApp por meio da Marrera Tech.

* **Contrate aqui** https://app.marrera.net (Receba 3 dias de teste)
🔗 **Contrate agora**: [https://app.marrera.net](https://app.marrera.net) (3 dias de teste gratuito)

1. Envio para Grupo ou número usando graficos e texto:

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

  > Para visualizar os IDs de grupos você deve acessar a ferramenta "id dos grupos" no painel [este link](https://app.marrera.net).

## Configuração no Zabbix ⚙️

Dentro do Zabbix, configure um novo tipo de mídia.

## Configuração da Ação 📢

- Crie uma nova ação, garantindo que contenha a variável `{ITEM.VALUE1}`. Isso será responsável pelo envio da imagem.

## Testando a Ação ✅✔️

- Realize um teste para verificar se tudo está funcionando corretamente.


![image](https://github.com/MarreraTech/Zabbix/assets/141791017/a91e9672-02e3-4651-8c15-71960390bd2b)

---
*Nota: As imagens acima são ilustrativas e podem variar de acordo com a configuração.*
