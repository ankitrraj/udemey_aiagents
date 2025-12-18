# temp  = 40

# while temp <100:
#     print(f"here the is the temp {temp}")

#     temp+=15

# // continue and break



user_input = input("give me the what flavour ice cream you want")

for i in user_input:

    if user_input == "vanila":
        continue
    elif user_input=="sher":
        break
    else:
        print("ok")

    print(f"this is you flavoure ice cream {user_input}")
