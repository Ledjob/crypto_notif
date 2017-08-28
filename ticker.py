import requests

r = requests.get("https://api.liqui.io/api/3/ticker/stx_btc")
r.json()
tick = r.json()
sell_stx = tick["stx_btc"]["sell"]

buy_stx = 0.00039000
total_stx = 0.00390000
quantity_stx = 9.99000000


profit_unit_stx = sell_stx - buy_stx
profit_stx = profit_unit_stx * quantity_stx
quantity_act_stx = quantity_stx * sell_stx

CONST = 100
pourcent_stx = ((quantity_act_stx - total_stx)/total_stx)*CONST

print '              Liqui Exchange'
print "\n\n     STX indication"
print "Buy at:                 ", buy_stx
print "STX sell price at:      ", sell_stx
print "for BTC:                ", total_stx
print "Variance price/share:   ", profit_unit_stx
print "You have made:          ", profit_stx
print "Actual profit:           %f %%          " % pourcent_stx
print "Actual BTC quantity:    ", quantity_act_stx


r = requests.get("https://api.liqui.io/api/3/ticker/dnt_btc")
r.json()
tick = r.json()
sell_dnt = tick["dnt_btc"]["sell"]

buy_dnt = 0.00004055
total_dnt = 0.00202750
quantity_dnt = 49.9500000

profit_unit_dnt = sell_dnt - buy_dnt
profit_dnt = profit_unit_dnt * quantity_dnt
quantity_act_dnt = quantity_dnt * sell_dnt

pourcent_dnt = ((quantity_act_dnt - total_dnt)/total_dnt)*CONST

print "\n    DNT indication"
print "Buy at:                 ", buy_dnt
print "STX sell price at:      ", sell_dnt
print "for BTC:                ", total_dnt
print "Variance price/share:  ", profit_unit_dnt
print "You have made:         ", profit_dnt
print "Actual profit:          %f %%          " % pourcent_dnt
print "Actual BTC quantity:    ", quantity_act_dnt



quantity_liqui_start = 0.00586182
quantity_liqui_total = quantity_act_dnt + quantity_act_stx
pourcent_liqui = ((quantity_liqui_total - quantity_liqui_start)/quantity_liqui_start)*CONST

print "\n\n                On Liqui Exchangge "
print "\nQuantity start;         ", quantity_liqui_start
print "Quantity total:         ", quantity_liqui_total
print "\nYou have made:            %f %% of profit" % pourcent_liqui
