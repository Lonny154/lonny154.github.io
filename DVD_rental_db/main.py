from queries import (
    get_customer_address,
    get_customer_rental_history,
    get_unreturned_films_by_customer,
    get_all_films_with_categories,
    get_sales_by_category,
    count_unreturned_films
)


def show_menu():
    print("====================================")
    print(" DVD Rental Data Analysis Project")
    print("====================================")
    print("1. Show customer address information")
    print("2. Show all movies rented by a customer")
    print("3. Show unreturned films for a customer")
    print("4. Show film information with categories")
    print("5. Show total sales by category")
    print("6. Count all unreturned films")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            get_customer_address()
        elif choice == "2":
            get_customer_rental_history()
        elif choice == "3":
            get_unreturned_films_by_customer()
        elif choice == "4":
            get_all_films_with_categories()
        elif choice == "5":
            get_sales_by_category()
        elif choice == "6":
            count_unreturned_films()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()