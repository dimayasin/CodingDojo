class call(object):
    def __init__(self, uid, name,phone,time,reason):
        self.uid=uid
        self.name=name
        self.phone=phone
        self.time=time
        self.reason=reason
    
    def display(self):
        print "Caller ID: {}".format(self.uid)
        print "Caller Name: {}".format(self.name)
        print "Caller Phone: {}".format(self.phone)
        print "Call Time: {}".format(self.time)
        print "Call Reason: {}".format(self.reason)
        return self

class CallCenter(object):
    def __init__(self):
        self.calls=[]
        self.queue_size=len(self.calls)
    
    def add(self,uid,name,phone,time,reason):
        self.calls.append(call(uid,name,phone,time,reason))
        self.queue_size +=1
        return self

    def Remove(self):
        self.calls.remove(self.calls[0])
        self.queue_size -=1
        return self


    def info(self):
        print "Queue size: {}".format(str(self.queue_size))
        if len(self.calls)>=1:
            for item in self.calls:
                item.display()
        else:
            print "Call Center List is Empty."
        print "=================="
        return self



firstcall=CallCenter()
firstcall.add(10,"Johnson","2232233443","2:20pm","To Chat")
firstcall.info()

firstcall.Remove()
firstcall.info()



# second_call=CallCenter()
# second_call.add(10,"Peterson","223223399","8:30pm","To Order Something")

# second_call.info()





