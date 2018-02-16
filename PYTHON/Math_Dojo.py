print "======================================="
print "PART I"
print "======================================="
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *args):
        
        for i in range(len(args)):
            self.result += args[i]
        return self
    def subtract(self, *args):

        for i in range (len(args)):
            self.result -= args[i]
        return self
  

md = MathDojo()
myresult=md.add(2,7,3).add(2,3,6).subtract(3,2).result
print "(2+7+3)+(2+3+6)-(3+2) = {}".format(str (myresult))
#print "{}".format(str(md.result))

print "======================================="
print "PART II"
print "======================================="

class MathDojo1(object):
    def __init__(self):
        self.result = 0

    def add(self, *args):
        
        for i in range(len(args)):
            if len(str(args[i])) ==1:
                self.result += args[i]
            elif len(str(args[i])) > 1:
                for j in args[i]:
                    self.result += j

        return self
    def subtract(self, *args):
       for i in range(len(args)):
            if len(str(args[i])) ==1:
                self.result -= args[i]
            elif len(str(args[i])) > 1:
                for j in args[i]:
                    self.result -= j
        return self

md = MathDojo1()
myresult2=md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
print "{}".format(str (myresult2))
