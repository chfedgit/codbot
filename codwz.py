# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:38:57 2020

@author: CHFED
"""

#import sqlite3
import locale
import time
import telepot
from telepot.loop import MessageLoop



def handle(msg):
    global chat_id
    content_type,chat_type,chat_id=telepot.glance(msg)
    #print(msg)
    
 #   conn = sqlite3.connect('C:/Users/CHFED/TG.db')
 #   cursor = conn.cursor()
    
    if 'video' in msg:
        print(msg)
        #{'message_id': 1526, 'from': {'id': 450446774, 'is_bot': False, 'first_name': 'Churin', 'last_name': 'Fed', 'username': 'chfed', 'language_code': 'ru'}, 'chat': {'id': 450446774, 'first_name': 'Churin', 'last_name': 'Fed', 'username': 'chfed', 'type': 'private'}, 'date': 1605792059, 'text': 'ss'}
        #print(msg['video']['file_name'])
        from_chat_id=msg['chat']['id']
        name=msg['chat']['first_name']
        
        # sql="SELECT * FROM COD_vid_stat WHERE chat_id=?"
        # cursor.execute(sql,[from_chat_id])
        # res = cursor.fetchone()
        # if res != None:
        #     count = res[2] 
        #     count = count+1
        #     sql="UPDATE COD_vid_stat SET stat=? WHERE chat_id = ?"
        #     cursor.execute(sql,[count,from_chat_id])
        #     conn.commit()
        # else:
        #     sql="INSERT INTO COD_vid_stat (chat_id,name,stat) VALUES(?,?,1)"
        #     cursor.execute(sql,[from_chat_id,name])
        #     conn.commit()
        
        sendings=bot.sendMessage('-478385715',msg['video']['file_name'])
        sendings=bot.forwardMessage('-478385715', from_chat_id, msg['message_id'],disable_notification=None)
        sendings=bot.sendMessage(chat_id,u'Спасибо, еще давай')
        # if ((count % 5) == 0):
        #     sendings=bot.sendMessage(chat_id,u'Ранг повышен!')
            
    else:
        # if msg['text'] == "/stats":
        #       # sql="SELECT * FROM COD_vid_stat"
        #       # cursor.execute(sql)
        #       # res = cursor.fetchall()
        #       strings=""
        #       for lines in res:
        #           strings+=str(lines[1])+" - "+str(lines[2]) +"\n"
        #       sendings=bot.sendMessage(chat_id,strings)
        # else:
        sendings=bot.sendMessage(chat_id,u'это не видос!')
    # conn.close()

#def on_callback_query(msg):
#    query_id,from_id,query_data, = telepot.glance(msg,flavor='callback_query')



TOKEN='1397913104:AAF_ntUecVbE8KZjneyaUQ4HMv3cJ-Yjpx0'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('я в деле!')

while 1:
    time.sleep(10)