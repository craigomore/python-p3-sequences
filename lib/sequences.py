def print_fibonacci(length):
    # Handle edge cases
    if length <= 0:
        print([])  # Print an empty list if the length is 0 or negative
        return
    elif length == 1:
        print([0])  # Print only the first Fibonacci number
        return
    elif length == 2:
        print([0, 1])  # Print the first two Fibonacci numbers
        return

    # Initialize the Fibonacci sequence with the first two numbers
    fib_sequence = [0, 1]
    
    # Generate Fibonacci numbers until we reach the desired length
    for i in range(2, length):
        # The next Fibonacci number is the sum of the last two
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    # Print the Fibonacci sequence
    print(fib_sequence)
