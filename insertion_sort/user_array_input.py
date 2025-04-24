def get_integer_input():
    while True:
        try:
            user_input = input("Enter numbers seperated by spaces: ")
            array = list(map(int, user_input.split()))
            return array
        except ValueError:
            print("Invalid input. Please enter only integers, separated by spaces.\n")


if __name__ == "__main__":
    get_integer_input()



