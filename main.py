
def splitlist(*args):
    numbers = list(args)
    minval = numbers[0] # Assume that first element is the minimum
    minindex = 0
    for i in range(1, len(numbers)):
        if numbers[i] < minval:
            # Update minval and minindex
            minval = numbers[i]
            minindex = i
    # Swap minval with the first element
    numbers[0], numbers[minindex] = numbers[minindex], numbers[0]
    # Return minval and the rest of the elements
    return minval, numbers[1:]


def main():

    numbers = [5, 4, 3, 2, 1]

    first, others = splitlist(*numbers)
    print(first)  # Expected output     1
    print(others)  # Expected output     4 3 2 5


if __name__ == '__main__':
    main()
