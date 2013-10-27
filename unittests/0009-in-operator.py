class A:
    def __init__(self):
        self.x = 1
        self.y = 2

    def __contains__(self, name):
        with javascript:
            if name in self.__dict__:
                return True

class B:
    pass

print 'testing dict'
if 1 in {1:True}: print 'in dict OK'
print 'testing tuple'
if 1 in (1,2,3): print 'in tuple OK'
print 'testing list'
if 1 in [1,2,3]: print 'in list OK'
print 'testing int32 array'
if 1 in array('int32', [1,2,3,4]): print 'in array OK'
print 'testing overloaded custom class A'
a = A()
if 'x' in a: print 'instance of overloaded A OK'

with javascript:
    print 'testing in Array'
    arr = [1,2,3]
    jsob = {1:True}
    if 1 in arr: print 'in Array ok'
    if 1 in jsob: print 'in javascript-object ok'

    if 1 in [1,2]: print 'in literal Array ok'
    if 'xx' in {xx:True}: print 'in literal jsobject ok'

b = B()
#if '__name__' in b: print 'this will throw an error because B is lacking a __contains__ method'
with javascript:
    if '__class__' in b:
        print 'this is allowed because we are within-javascript where the rules are slightly different'
        print 'class name of instance b:', b['__class__']['__name__']

print 'test complete'
