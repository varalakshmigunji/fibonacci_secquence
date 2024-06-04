def fibonacci_sequence(num_terms):
    # Initialize first two terms of the sequence
    fib_sequence = [0, 1]

    for _ in range(2, num_terms):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

def main():
    print("Fibonacci Sequence Generator")
    print("============================")
    num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

    # Generate and display the Fibonacci sequence
    sequence = fibonacci_sequence(num_terms)
    print("Fibonacci Sequence:", sequence)

if __name__ == "__main__":
    main()