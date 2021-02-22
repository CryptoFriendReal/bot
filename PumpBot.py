from binance.client import Client
from binance.client import *
import time
import ccxt
import keyboard
import sys

text_file = open('API KEY.txt','r')
apikey=str(text_file.read(64))


text_file = open('API SECRET.txt','r')
apisecret=str(text_file.read(64))


text_file = open('TRADING PAIR.txt','r')
tradingpair=str(text_file.read(4))
print('Trading pair:',tradingpair)


text_file = open('PROFIT CONFIG.txt','r')
HowBigProfitYouWantBro=float(text_file.read(5))
print('Profit take:',HowBigProfitYouWantBro,'%')


text_file = open('STOP LOSS.txt','r')
stoploss=float(text_file.read(5))
print('Stop loss:',stoploss,'%')


#
binance=ccxt.binance({
    'apiKey': apikey,
    'secret': apisecret,
})
client=Client(apikey,apisecret)

print('---Succesfully logged in---')
#
account_balance=binance.fetch_balance()
roo=account_balance['free'][tradingpair]#it's integer :D
print('Your balance:',roo,tradingpair)

inputtrade=input('Input the coin name:')

symbolTicker=str(inputtrade+tradingpair)

list_of_tickers=client.get_all_tickers()
for tick_2 in list_of_tickers:
    if tick_2["symbol"] == symbolTicker:
        prev_symbolPrice = float(tick_2["price"])
print('Price for',inputtrade,'=',prev_symbolPrice,tradingpair)

ILoveYou=round(roo/prev_symbolPrice*0.60,3)
WhatT=ILoveYou*prev_symbolPrice
order=client.order_market_buy(
    symbol=symbolTicker,
    quantity=ILoveYou
    )
stopIT=stoploss*-1
print('Bought succesfully',ILoveYou,inputtrade,'for',WhatT,'',tradingpair)
def stop():
    sys.exit()
    

def PUMPING():
    list_of_tickers=client.get_all_tickers()
    for tick_2 in list_of_tickers:
        if tick_2["symbol"] == symbolTicker:
            current_symbolPrice = float(tick_2["price"])
    profiT=(current_symbolPrice/prev_symbolPrice-1)*100
    time.sleep(0.002)
    print('price',current_symbolPrice,tradingpair,'profit:',round(profiT,3),'%','want',HowBigProfitYouWantBro,'%','stoploss:',stoploss,'%')
    if profiT>=HowBigProfitYouWantBro:
        
        order=client.order_market_sell(
            symbol=symbolTicker,
            quantity=ILoveYou
            )
        print('Succesfully sold with profit of:',profiT,'%')
        time.sleep(5)
        stop()
    if profiT<=stopIT:
        order=client.order_market_sell(
            symbol=symbolTicker,
            quantity=ILoveYou
            )
        print('Succesfully sold with profit of:',profiT,'%')
        time.sleep(5)
        stop()
    if keyboard.is_pressed('s'):
        order=client.order_market_sell(
            symbol=symbolTicker,
            quantity=ILoveYou
            )
        print('Succesfully sold with profit of:',round(profiT,3),'%')
        time.sleep(5)
        stop()
    else:
        PUMPING()
PUMPING()


    
    
    
    








