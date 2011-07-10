#Problem Set 2 - Problems 1 & 2

# if small consecutive n are solutions then all larger n are also
# also true for medium and large_ since:
#   large contains medium which contains small. The labels don't
#   matter. [small, medium, large] = [20, 9, 6] works as well

# Let [50, 55] be values of n with solutions, then small can be 
# added to any value on the interval m times to create arbitrary 
# n > 55 with solutions

# 50 + (1)6 = 56    Once there is a run of at least small correct
# 51 + (1)6 = 57    solutions then there will be a solution for 
# 52 + (1)6 = 58    all n > x where x is the last unsolvable n 
# 53 + (1)6 = 59    before the run of small correct solutions
# 54 + (1)6 = 60
# 55 + (1)6 = 61    Arbitrary solution using [50, 55] 
#                   i + (m)6 = n 
# 50 + (2)6 = 62    i = 50 + ((n - 50) % 6)
# 51 + (2)6 = 63    solve for m
# 52 + (2)6 = 64
# 53 + (2)6 = 65
# 54 + (2)6 = 66
# 55 + (2)6 = 67

# 50 + (3)6 = 68   # 50 + (4)6 = 74
# 51 + (3)6 = 69   # 51 + (4)6 = 75
# 52 + (3)6 = 70   # 52 + (4)6 = 76
# 53 + (3)6 = 71   # 53 + (4)6 = 77
# 54 + (3)6 = 72   # 54 + (4)6 = 78
# 55 + (3)6 = 73   # 55 + (4)6 = 79

result = {}
min = 0
max = 66
greatest_zero = 0
consecutive_solutions = 0
small = 6
medium = 9
large = 20

for n in range(min, max):
    a_bound = (n / small) + 1
    b_bound = (n / medium) + 1
    c_bound = (n / large) + 1

    result[n] = 0
    for a in range(a_bound):
        for b in range(b_bound):
            for c in range(c_bound):
                if (small*a + medium*b + large*c) == n:
                    print "\tWinner! %d(%d) + %d(%d) + %d(%d) = %d" % (
                        small, a, medium, b, large, c, n)
                    result[n] += 1

for i in range(min, max):
    if result[i] == 0:
        greatest_zero = i
    #print "result[%d]: %d" % (i, result[i])

    if result[i] > 0:
        consecutive_solutions += 1
    else:
        consecutive_solutions = 0;

    if consecutive_solutions == small:
        print "greatest_no_solution: %d" % (i - small)
    
print "greatest_zero: %d" % (greatest_zero)

