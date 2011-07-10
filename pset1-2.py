#Problem Set 1 - Problem 2

#(sum of logs of all primes < nth prime) < nth prime
#(sum of logs of all primes < nth prime) / nth prime --> 1 as n inc

from math import log

candidate = 1
prime_count = 1
sum_log_prime = 2 

nth_prime = raw_input('find result for nth prime: ')
nth_prime = int(nth_prime)

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

        sum_log_prime += log(candidate)

        if prime_count == nth_prime:
            print "results"
            print "nth prime: %i" % (candidate)
            print "sum of logs: %f" % (sum_log_prime)
            print "ratio: %f" % (sum_log_prime / candidate)


