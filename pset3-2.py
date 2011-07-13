# MIT 6.00 Problem Set 3 - Problem 2

from string import *

def subStringMatchExact(target, key):
    index = 0
    starts = []

    if key == '':
        for i in range(0, len(target)):
            starts.append(i)

    else:        
        while True:
            index = find(target, key, index)
            if index == -1:
                break

            starts.append(index)
            index += len(key) 

    return tuple(starts)

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'q'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca' 

print "\n----------Problem 2----------\n"

print subStringMatchExact(target1, key10)             
print subStringMatchExact(target1, key11)
print subStringMatchExact(target1, key12)
print subStringMatchExact(target1, key13)

print subStringMatchExact(target2, key10)
print subStringMatchExact(target2, key11)
print subStringMatchExact(target2, key12)                
print subStringMatchExact(target2, key13)


print "\n----------Problem 3----------\n"

target = 'atgacatgca'

key1 = 'a'
key2 = 'gc'

starts1 = subStringMatchExact(target, key1)
starts2 = subStringMatchExact(target, key2)

print "starts1: ", starts1
print "starts2: ", starts2

def constrainedMatchPair(substr1, substr2, length):
    valid = []

    for n in substr1:
        for k in substr2:
            if n + length + 1 == k:
                valid.append(n)

    return tuple(valid)
            

print constrainedMatchPair(starts1, starts2, len(key1))



### START MIT CODE ###

# Grimson, Guttag, 6.00 Introduction to Computer Science and Programming, 
# Fall 2008. (Massachusetts Institute of Technology: MIT OpenCouseWare), 
# http://ocw.mit.edu (Accessed July 13, 2011). 
# License: Creative Commons BY-NC-SA
# http://ocw.mit.edu/terms/#cc

def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print '\nbreaking key',key,'into',key1,key2

        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)

        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers

### END MIT CODE ###

subStringMatchOneSub('atgc','atgaatgcatggatgtaaatgcag')
print "\nTrial 2\n" 
print subStringMatchExact('atgctttgtgctttacgctttatactttatga', 'atgc')

subStringMatchOneSub('atgc','atgctttgtgctttacgctttatactttatga')

print "\n----------Problem 4----------\n"

def subStringMatchExactlyOneSub(target, key):
    matches = []
    exact = subStringMatchExact(target, key)
    oneSub = subStringMatchOneSub(key, target)
    for i in oneSub:
        for j in exact:
            if j == i:
                break
            else:                
                matches.append(i)

    return tuple(matches)


print subStringMatchExactlyOneSub('atgctttgtgctttacgctttatactttatga', 'atgc')
