from services.user_services import get_user, get_my_detail, get_all_user, update_user, delete_user, update_user_password


def handle_admin_menu(user):
    while True:
        print(f"""
------Welcome Admin - {user.name}------
    1. Get User
    2. Get All User
    3. Update User Detail
    4. Delete User
    5. Update Product Stock
    6. Update Order Status
    7. Logout
""")
        choice = input("Enter here: ")
        match choice:
            case '1':
                get_user(user)
            case '2':
                get_all_user()
            case '3':
                update_user()
            case '4':
                delete_user()
            case '5':
                update_product_stock()
            case '6':
                update_order_status()
            case '7':
                exit()
            case _:
                print("❌ Invalid choice. Try Again!\n")

def handle_customer_menu(user):
    while True:
        print(f"""
------Welcome {user.name}------
    1. My Detail
    2. Update My Detail
    3. Update Password
    4. Show My Orders
    5. Show Product
    6. Place Order
    7. Logout
""")
        choice = input("Enter here: ")
        match choice:
            case '1':
                get_my_detail(user)
            case '2':
                update_user()
            case '3':
                update_user_password(user)
            case '4':
                show_orders()
            case '5':
                show_product()
            case '6':
                place_order()
            case '7':
                exit()
            case _:
                print("❌ Invalid choice. Try Again!\n")