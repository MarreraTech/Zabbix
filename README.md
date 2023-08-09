# Envio de alertas zabbix com APi do WhatsApp 
Script de zabbix para enviar dados e alertas com ou sem imagem para grupos ou números do WhatsApp


![2 Logo fundo transparente](https://github.com/MarreraTech/Zabbix/assets/141791017/f79c274c-56ca-4d3b-aa1f-8ce416e21dae)

Para usar esse script é necessário que o usuário contrate uma instância API do WhatsApp com a Marrera Tech.

Contrate aqui: https://app.marrera.net (Receba 3 dias de teste)

Envio para Grupo ou número usando graficos e texto:

![image](https://github.com/MarreraTech/Zabbix/assets/141791017/9d4ccb58-5989-40e7-8669-fdc6ae29b48a)


Envio para Grupo ou número usando texto:

![image](https://github.com/MarreraTech/Zabbix/assets/141791017/8ef211e1-b058-4c6f-8d47-6334dc34239b)



Para usar com o zabbix é necessário que exista o ITEM ID como no exemplo abaixo:

Faça as seguintes configurações:

Importante: na mensagem deve conter no corpo Item ID: {ITEM.ID1}
Exemplo.
⏰ Inicio do problema às {EVENT.TIME} em {EVENT.DATE}
Host: {HOST.NAME}
Serveridade: {EVENT.SEVERITY}
Último valor: {ITEM.VALUE1}
Item ID: {ITEM.ID1}

Exemplo em imagem:


![Configurações Zabbix](https://github.com/MarreraTech/Zabbix/assets/141791017/8cb79c6e-446f-4176-ac1f-c29c6d905667)



