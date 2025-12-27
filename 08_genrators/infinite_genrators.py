def infinite_sher():
    count = 1
    while True:
        yield f"the sher is {count}"
        count+=1

sher = infinite_sher()

for i in range(7):
    print(next(sher))
