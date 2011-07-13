from string import *

def countSubStringMatch(target, key):
    index = 0
    count = 0

    while True:
        index = find(target, key, index)
        if index == -1:
            break
        index += len(key) 
        print "index %d" % (index)
        count += 1

    return count


def countSubStringMatchRecursive(target, key):
    index = 0
    count = 0

    index = find(target, key, index)

    if index != -1:
        count += 1
        index += len(key)
        print "index %d" % (index) 
        print "target[index:]: %s" % (target[index:])
        count += countSubStringMatchRecursive(target[index:], key)

    return count
    


print countSubStringMatch("XXXXXbeepXXXXbeepXXXbeepXXbeepXbeepbeep", "beep")
print "---------------------------------------------"
print countSubStringMatch("beepbeepbeepbeepbeepbeep", "beep")
print "---------------------------------------------"
print countSubStringMatch("beepeepbeepbeebeepeepbeepbeebeepbeep", "beep")
print "---------------------------------------------"
print countSubStringMatch("beep", "beep")
print "---------------------------------------------"
print countSubStringMatch("", "beep")
print "---------------------------------------------"

print countSubStringMatchRecursive("XXXXXbeepXXXXbeepXXXbeepXXbeepXbeepbeep", "beep")
print "---------------------------------------------"
print countSubStringMatchRecursive("beepbeepbeepbeepbeepbeep", "beep")
print "---------------------------------------------"
print countSubStringMatchRecursive("beepeepbeepbeebeepeepbeepbeebeepbeep", "beep")
print "---------------------------------------------"
print countSubStringMatchRecursive("beep", "beep")
print "---------------------------------------------"
print countSubStringMatchRecursive("", "beep")
print "---------------------------------------------"


