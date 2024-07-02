
def splitlist(numbers):
    minval = numbers[0] # Assume that first element is the minimum
    minindex = 0
    for i in range(1, len(numbers)):
        if numbers[i] < minval:
            # Update minval and minindex
            minval = numbers[i]
            minindex = i



def main():

    numbers = [5, 4, 3, 2, 1]

    first, others = splitlist(numbers)
    print(first)  # Expected output     1
    print(others)  # Expected output     4 3 2 5


if __name__ == '__main__':
    main()
