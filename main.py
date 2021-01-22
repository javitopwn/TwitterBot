#!/usr/bin/env python3

"""Requisitos:

Crear un bot en Telegram con @BotFather.
Crear un canal publico y meter al bot como administrador.


"""
import requests
import json
import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream

bot_token="xxxxx:xxxxxxxx"   #Token del bot que da @BotFather
bot_chatID="@XXXXXX"         #ID del usuario al que quieras enviar mensajes o del canal


def telegram_bot_sendtext(bot_token, bot_chatID, bot_message,bot_message2):
# send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' "Usuario: "+ bot_message + "\nTweet: "+bot_message2


#PETICION A LA API
    r = requests.post('https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' "Usuario: "+ bot_message + "\nTweet:"+bot_message2)
"""
   response = requests.get(send_text)
    data=json.loads(r.text)
    print(data['ok'])
    print(send_text)
"""
class StdOutListener(StreamListener):


    def on_status(self, status):
        if status.user.id_str != '1224795286155014145':   #ID OBTENIDA DE https://tweeterid.com/
            return
        print(status.text)
        telegram_bot_sendtext(bot_token,bot_chatID,status.user.screen_name,status.text)

    def on_error(self, status_code):
        print(status_code)

palabras_track = ['pito','subnormal']    #Palabras a trackear, se pueden trackear mas cosas aparte de palabras

if __name__=="__main__":
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)


#LANZAR EL STREAM LISTENER Y FILTRAR

    stream= Stream(auth,listener)
    stream.filter(track=palabras_track)



