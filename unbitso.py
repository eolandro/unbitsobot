"""
Este bot es para checar la cotizacion de un crytomoneda en bitso
iniciamente ser perfilara para eth

"""
from telegram.ext import Updater, CommandHandler
from urllib import request
import json

def Saludo(bot, update):
	MSG = 'Hello {}'.format(update.message.from_user.first_name) + "."
	MSG += 'Este bot te permite consultar el precio del eth en bitso, ejecuta /eth'
	update.message.reply_text(MSG)

# realizar un get a curl "https://api.bitso.com/v3/ticker/?book=eth_mxn"
def eth(bot, update):
	url = "https://api.bitso.com/v3/ticker/?book=eth_mxn"
	req = request.Request(url, data=None, headers={'User-Agent': 'curl/7.57.0'})
	R = request.urlopen(req)
	#De vuelve una lista
	lineas = R.readlines()
	# En la primera posicion esta la respuesta en json
	jdata = json.loads(lineas[0])
	update.message.reply_text(jdata['payload']['last'])

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

#					Token del botfather
updater = Updater('')
# 									º		NombreComando, Funcion
updater.dispatcher.add_handler(CommandHandler('start', Saludo))
updater.dispatcher.add_handler(CommandHandler('eth', eth))

updater.start_polling()
updater.idle()
