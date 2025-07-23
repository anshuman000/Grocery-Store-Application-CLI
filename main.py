from cli.cli import user_login, user_registration
   
def run():
    print("""
===========GROCERY STORE CLI===========

        1.Login
        2.Register
""")
    choice = input("Enter here: ")
    # print(type(choice))
    if choice == '1':
        user_login()
    elif choice == '2':
        user_registration()  
    else:
        print("❌ Invalid choice.\n")
        exit()


if __name__ == "__main__":
    run()