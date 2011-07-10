#Problem Set 1 - Problem 1

#prime_count = 1 since first prime number 2 is known
#candidate = 1 inc by 2 gives odd numbers
#stop checking once nonprime found with break
#trial division method, divisors on interval (1, sqrt(candidate)]

candidate = 1
prime_count = 1
column = 1
nth_prime = 1000
max_column = 10
column_pad = 6

print str(2).center(column_pad),

while prime_count < nth_prime:
    divisor = 2
    prime = 1
    candidate += 2

    while divisor <= candidate**0.5:
        if candidate % divisor == 0:
            prime = 0
            break

        divisor += 1
                
    if prime:
        prime_count += 1

        print str(candidate).center(column_pad),
        column += 1

        if column == max_column:
            print
            column = 0

        if prime_count == 1000:
            print ("The 1000th prime is: ", candidate)
