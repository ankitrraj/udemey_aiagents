#  two ways to delcare a dict 

# use dict()

sher = dict(type="sheru",qty="kuta",color="white",cat=3)
print(f"hey kuta is {sher}")

print(type(sher))

another_sher = {}
another_sher["sheru"] ="tiger"
another_sher["patanahi"] ="mujhenahipata"
print(another_sher)

print(type(sher))
del another_sher["sheru"]
print(another_sher)

print(f"kya sher ke pass sheru hai {"type"in sher}")
print(f"kya sher ke pass sheru hai {"tiger"in another_sher}")  # only the key  is to identify

nikal = sher.popitem()
print(f"piche se nikal{nikal}")

extra =  {"a":"apple","b":"baal"}
another_sher.update(extra)
print(another_sher)

bata_kitne_hai = sher.get("kuta","kuch to hai ")
print(f"cat kitne hai : {bata_kitne_hai}")

