from user import getUser
import calculator
def main():
    x = getUser()
    print(f"Hello, {x["name"]}")
    p = input("Application: ")
    if p == "calculator":
        calculator.add()

if __name__ == "__main__":
    main()