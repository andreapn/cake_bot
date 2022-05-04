from txns import Txn_bot

token_address = '0x6b23c89196deb721e6fd9726e6c76e4810a464bc'  # BUSD bsc-mainnet

quantity = 5 * 10 ** 18
net = 'bsc-mainnet'
slippage = 2  # %
gas_price = 5 * 10 ** 9  # Gwei, bsc-mainnet=5, eth-mainnet=https://www.gasnow.org/, eth-rinkeby=1
bot = Txn_bot(token_address, quantity, net, slippage, gas_price)

# tokens = bot.get_amounts_out_sell()
# print(tokens)
bot.swap_token()

# TODO: Add description to  README
