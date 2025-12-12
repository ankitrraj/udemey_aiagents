#  1 to 10 

for t in range(1,11):
    print(t)



list_is= ["ankit","rohit","ankesh"]

print(type(list_is))

for t in list_is:
    print(f"the order of name is {t}")

for idx,item in enumerate(list_is ,start=1):
    print(f"the {idx}:{item}")

#  zip combine th elist 

hey = ["hello","ram_ram","sherrr"]
num= [1,2,3]
for u,t in zip(hey,num):
    print(f"the order print {t} and {u}")
