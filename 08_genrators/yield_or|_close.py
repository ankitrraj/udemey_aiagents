def local_chai():
    yield "sher ki chai "
    yield "bakri ki chai "


def improted_cahi():
    yield "russian ki chai @6000 "
    yield " japanese ki chai "

def sher_cahi():
    yield from local_chai()
    yield from improted_cahi()


for chai in sher_cahi():
    print(chai)



def chai_stall():
    try: 
        while True:
          order  = yield "the order is "

    except:
        print("mujhe nahi pata ")

hey = chai_stall()

print(next(hey))
hey.close()  # cleanup  for memory