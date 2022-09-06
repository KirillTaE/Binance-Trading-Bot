from binance.client import Client
import win32gui, time
api_key = "***"
api_secret = "***"


green, red, bycicle = False, False, False
quant = 0

def pixel_color_at(x, y):
    hdc = win32gui.GetWindowDC(win32gui.GetDesktopWindow())
    c = int(win32gui.GetPixel(hdc, x, y))
    return (c & 0xff), ((c >> 8) & 0xff), ((c >> 16) & 0xff)# (r, g, b)

def check_decimals(symbol):
    info = client.get_symbol_info(symbol)
    val = info['filters'][2]['stepSize']
    decimal = 0
    is_dec = False
    for c in val:
        if is_dec is True:
            decimal += 1
        if c == '1':
            break
        if c == '.':
            is_dec = True
    return decimal


def buy_crypto(CryptoPair, money, decimal):
    quant = round(money * 0.999 / float(client.get_symbol_ticker(symbol=CryptoPair)["price"]), decimal)
    client.order_market_buy(
        symbol=CryptoPair,
        quantity=quant)
    return quant


def sell_crypto(CryptoPair, quant):
    client.order_market_sell(
        symbol=CryptoPair,
        quantity=quant)

def balanse():
    for i in client.get_account()["balances"]:
        print(i)
    print()

def green_red():
    for i in range(234, 238):
        if pixel_color_at(1635, i) == (0, 230, 118):
            #green = True
            return True, False
        elif pixel_color_at(1635, i) == (255, 82, 82):
            #red = True
            return False, True
    return False, False


client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'

#balanse()
print(client.get_asset_balance(asset='USDT'))
print(client.get_asset_balance(asset='BNB'))
while True:

    green, red = green_red()

    #print(green, red)

    if green and not bycicle:
        quant = buy_crypto("BNBUSDT", 100, check_decimals("BNBUSDT"))
        green, red, bycicle = False, False, True
        print(client.get_asset_balance(asset='USDT'))
        print(client.get_asset_balance(asset='BNB'))
    elif red and bycicle:
        green, red, bycicle = False, False, False
        sell_crypto("BNBUSDT", quant)
        #balanse()
        print(client.get_asset_balance(asset='USDT'))
        print(client.get_asset_balance(asset='BNB'))

    time.sleep(300)




'''
while True:
    print(round(100 / float(client.get_symbol_ticker(symbol='ETHUSDT')["price"]), 6))
'''