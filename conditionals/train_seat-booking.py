seat_booking = input("enter what seat you need sleeper/ac/general/luxury:: ").lower()


if seat_booking =="sleeper":
    print("you are book a sleeper class ticket enjoy your journey")
elif seat_booking =="ac":
    print("you are book a ac class ticket enjoy your journey")
elif seat_booking =="general":
    print("you are book a  general class ticket enjoy your journey")
elif seat_booking =="luxury":
    print("you are book a luxury class ticket enjoy your journey")
else :
    print("invalid seat type")

