def serve_cahi():
    yield "cup 1: masala chai"
    yield "cup 2: elaichi chai"
    yield "cup 3: another chai"

stall = serve_cahi()

for i in stall:
    print(i)

print(stall)


def sher_cahi():
    yield "ram ram "
    yield "jai shree krishna "
    yield "sherrrrrrrrrrrrrrr"

a = sher_cahi()

print(next(a))
print(next(a))
print(list(a))