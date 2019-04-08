print("Give me two numbers, and I'll plus them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q' or first_number == 'quit':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You should input a number!")
    else:
        print(answer)
