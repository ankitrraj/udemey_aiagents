def chai(masala="medium"):
    """hey how are you chai"""
    return masala

print(chai.__doc__)
print(chai.__name__)

def create_bill(band=0,fevikvick=0):
    """

    there  is a bill calculator 
    :the band price is 56 per quantity
    :and thw fevikvick is 5 rupees per qty
    """
    total_amount = band*56 + fevikvick*5
    return f"here is your bill {total_amount}"

print(create_bill(879747,257))