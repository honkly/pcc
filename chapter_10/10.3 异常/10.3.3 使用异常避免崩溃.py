while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    answer = int(first_number) / int(second_number)
    print(answer)
