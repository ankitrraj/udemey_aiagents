#  first we have to input email or password
def get_user_info():

    for i in range(0,2):
        user_name = input("enter your user name::")
        user_email = input("enter your email id example@gmail.com ::")
        if ".com" in user_email:
            print(f"user name is {user_name} and user email is here {user_email}")
        else:
            print("please enter a valid email")

the_user_data = get_user_info()

def get_validate_data():
    print(f"the user input validated {the_user_data}")

def user_saved_db():
    database = the_user_data
    print(f"the user data is {database}")

def the_register_user_info():
    print(the_user_data)
    get_validate_data()
    user_saved_db()
    print("wecome to the my ai agent ")

the_register_user_info()


    



    
