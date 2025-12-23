hotel_menu = [
    "panner tikkar",
    "matar panner",
    "chapati",
    "sahi panner",
    "salad"
]

filter_panner = {paneer for paneer in hotel_menu if "panner" in paneer}
print(type(filter_panner))
print(filter_panner)
