import sys

print sys.argv

def add(number):
        new_value = int(number) + 10
        return new_value


result = add(sys.argv[1])
print "you passed in this number: %s" % sys.argv[1]
print "I calculated this new number by adding 10 to it: %s" % result

 
