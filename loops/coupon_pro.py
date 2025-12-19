#  first we create the list of usesrs

my_users= [
    {"id":1,"total":4798,"coupon":"P20"},
    {"id":2,"total":878,"coupon":"F40"},
    {"id":3,"total":3118,"coupon":"P10"}
]


my_discounts= {
    "P20":(0.2,0),
    "F40":(0.4 , 0),
    "P10":(0,450)
}
for user in my_users:
    percent,fixed = my_discounts.get(user["coupon"],(0,0))
    discounts= user["total"] * percent + fixed

    print(f"percent  is :{percent}")
    print(f"fixed is :{fixed}")
    print(f"user id {user["id"]} paid user {user["total"]}  he give discount is {discounts} ")