def gnerate_vat_rate(amount ,vatrate):
    # return (100+vatrate)/100
    return round(amount*(100+vatrate)/100,2)

print(f"the amount is 1452 vat rate 18% as india to the final amount of bill is {gnerate_vat_rate(586,17)}")