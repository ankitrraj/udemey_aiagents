ice_cream_price={
    "butter_scotch":70,
    "mango_ice":50,
    "nut_creack":478
}

icecream_in_usd = {ice:price/88 for ice, price in ice_cream_price.items()}
print(icecream_in_usd)