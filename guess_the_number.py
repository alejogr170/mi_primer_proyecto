print()
print()

number_to_guess = int(input("Write one number without been seen: "))

tried_number = int(input('Try some numbers :'))

while tried_number != number_to_guess:
    print('You fail due!')
    tried_number = int(input('Try again big boy ;) :'))

print('Good work!')