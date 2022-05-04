from txns import Txn_bot
import time

token_address = '0x6b23c89196deb721e6fd9726e6c76e4810a464bc'  # BUSD bsc-mainnet

price = 0.28
qtt = 2180

print("Token: {}, Address: {}".format("XWG", token_address))
print("Order Price: {}, Quantity: {}, Total: {}".format(price, qtt, (price * qtt)))

quantity = qtt * 10 ** 18
net = 'bsc-mainnet'
slippage = 10  # %
gas_price = 8 * 10 ** 9  # Gwei, bsc-mainnet=5, eth-mainnet=https://www.gasnow.org/, eth-rinkeby=1
bot = Txn_bot(token_address, quantity, net, slippage, gas_price)

# tokens = bot.get_amounts_out_sell()
# print(tokens)
# bot.swap_token()

loop = True
count = 0

while (loop):
    time.sleep(2)
    try:
        current_price = (bot.check_price_usdt()[1] / (10 ** 18))
        print("{}".format(current_price / qtt))
        if current_price >= (qtt * price):
            count = count + 1
            if count == 2:
                bot.swap_token()
                loop = False
    except:
        print("An exception occurred")
