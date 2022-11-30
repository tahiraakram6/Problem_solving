########  LUH'N ALGORITHM #########

def main():
    # Check given card number is valid or invalid
    numbers = int(input("Enter Number: "))
    if len(str(numbers)) > 16 or len(str(numbers)) < 12:
        print("INVALID")
    else:
        card_type(card_luhn(numbers), numbers)

### Apply Luhn's Algorithm
def card_luhn(digit):

    t_no = str(digit)
    digit_sum = 0
        
    #Multiply Every second number by 2
    for i in range(2, len(t_no) + 1, 2):
        digits = 2 * int(t_no[-i])

        # Convert resulting 2 digit number into single digit
        if_sum = 0
        if len(str(digits)) == 2:
            for digit in str(digits):
                if_sum += int(digit)
                digits = 0

        if_sum += digits
        digit_sum += if_sum

    # those digits that does not need to be multiplied by 2
    for i in range(1, len(t_no) + 1, 2):
        digits = int(t_no[-i])
        digit_sum += digits

    if digit_sum % 10 == 0:
        return 0
    else:
        return 1


# Assign the card whether AMEX, VISA, or MASTERCARD
def card_type(check, nums):

    num = int(str(nums)[:2])

    if check != 0:
        print("INVALID")

    # AMEX condition (first two digits from left are either 37 or 34)
    elif num == 37 or num == 34:
        print("AMEX")

    # VISA condition (first digit from left is 4)
    elif str(num)[:1] == "4":
        print("VISA")

    # MASTERCARD condition (first two digits from left are between 50 and 56)
    elif num > 50 and num < 56:
        print("MASTERCARD")

    else:
        print("INVALID")
while(True):
    if __name__ == "__main__":
        main()