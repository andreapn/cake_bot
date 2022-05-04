from txns import Txn_bot

# token_address = '0x6b23c89196deb721e6fd9726e6c76e4810a464bc'  # XWG
# token_address = '0xfb62ae373aca027177d1c18ee0862817f9080d08'  # DPET
token_address = '0xf4ed363144981d3a65f42e7d0dc54ff9eef559a1'  # FARA
# token_address = '0x14c358b573a4ce45364a3dbd84bbb4dae87af034'  # DND
# token_address = '0x154a9f9cbd3449ad22fdae23044319d6ef2a1fab'  # SKILL
# token_address = '0xbcf39f0edda668c58371e519af37ca705f2bfcbd'  # CWS
print("Address: {}".format(token_address))

net = 'bsc-mainnet'
slippage = 4  # %
qtt = 1
quantity = qtt * 10 ** 18
gas_price = 7 * 10 ** 9  # Gwei, bsc-mainnet=5, eth-mainnet=https://www.gasnow.org/, eth-rinkeby=1
bot = Txn_bot(token_address, quantity, net, slippage, gas_price)
bnb_price = (bot.check_price_bnb_busd()[1] / (10 ** 18))
token_bnb_price = (bot.check_price_bnb_token()[1] / (10 ** 18))
print("BNB price: {}".format(bnb_price))
print("Token-BNB price: {}".format(token_bnb_price))
print("Token price: {}".format(bnb_price * token_bnb_price))

# token_address = '0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82' #Example CAKE bsc-mainnet
# net = 'bsc-mainnet'
#
# bot = Txn_bot(token_address, net)
# print(bot.check_price_busd_usdc())
