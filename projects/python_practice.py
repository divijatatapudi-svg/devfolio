
# Python Practice Collection

def even_or_odd():
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def palindrome():
    word = input("Enter a word: ")

    if word == word[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


def count_vowels():
    text = input("Enter a sentence: ")
    vowels = "aeiouAEIOU"
    count = 0

    for character in text:
        if character in vowels:
            count += 1

    print("Number of vowels:", count)


def main():
    while True:
        print("\n--- Python Practice Collection ---")
        print("1. Even or Odd")
        print("2. Palindrome Checker")
        print("3. Count Vowels")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            even_or_odd()

        elif choice == "2":
            palindrome()

        elif choice == "3":
            count_vowels()

        elif choice == "4":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Try again.")


main()
