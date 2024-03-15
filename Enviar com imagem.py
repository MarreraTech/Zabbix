# Esse script lhe permite integrar o zabbix com o whatsapp
# Na configuração do zabbix você vai usar tanto o número quanto o id do grupo pois não muda nada. 


#!/usr/bin/python3
import requests
import json
import base64
from datetime import datetime
import urllib3
from pyzabbix import ZabbixAPI
import sys
import re

urllib3.disable_warnings()
TOKEN = "SEUTOKEN"
URL_ZABBIX = "http://SEUIP/zabbix"
USER = "Admin"
PASS = "zabbix"
WIDTH = "800"
HEIGTH = "250"
DRAWTYPE = "5"
period = "from=now-00d-6h-20m&to=now"
NOW = datetime.now()
mensagem = sys.argv[1]
titulo = sys.argv[2]
chat_id = sys.argv[3]
CAPTION_TEMPLATE = "Tit: {TITULO}\nDat: {NOW}"

mensagem = sys.argv[1]
titulo = sys.argv[2]
chat_id = sys.argv[3]

def getCookie():
    s = requests.session().get(
        f"{URL_ZABBIX}/index.php?login=1&name={USER}&password={PASS}&enter=Enter"
    )
    return s.cookies

def extract_item_id(mensagem):
    match = re.search(r'Item ID:\s*(\d+)', mensagem)
    if match:
        item_id = match.group(1)
        return item_id
    else:
        return None
item_id = extract_item_id(mensagem)

print('\n\n\nItem ID:', item_id)


def getImage(itemid, item_name):
    r = requests.get(
        f"{URL_ZABBIX}/chart3.php?name={item_name}&{period}&items[0][itemid]={item_id}&items[0][drawtype]=5&items[0][color]=C71585&width={WIDTH}&height={HEIGTH}",
        cookies=getCookie()
    )
    return r.content

if item_id:
    zapi = ZabbixAPI(URL_ZABBIX)
    zapi.login(USER, PASS)
    item = zapi.item.get(filter={"itemid": item_id})
    if item:
        item_name = item[0]["name"]
        caption = CAPTION_TEMPLATE.format(TITULO=item_name, NOW=NOW)

        image_data = getImage(item_id, item_name)
        base64_image = base64.b64encode(image_data).decode('utf-8')

        api_url = f"https://apiwt.marrera.net/send-media/id={TOKEN}"

        payload = {
            "number": chat_id,
            "mediaMessage": {
                "mediatype": "image",
                "caption": f"{titulo}\n{mensagem}",
                "media": base64_image
            }
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(api_url, json=payload, headers=headers)

        print(f"Item '{item_name}' enviado para o WhatsApp. Resposta: {response.text}")
    else:
        print(f"Item ID '{item_id}' não encontrado no Zabbix.")
else:
    print("Item ID não encontrado na mensagem.")
