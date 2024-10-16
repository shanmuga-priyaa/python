#exception handling

'''a=int(input("enter a value:"))
b=int(input("enter a value:"))
print(a/b)
print("the end")
print("___________________________________________________")'''

#try,exception-->(like if else)
'''try:
    a=int(input("enter a value:"))
    b=int(input("enter a value:"))
    print(a/b)
except Exception:
    print("some thing went wrong")
print("the end")
print("___________________________________________________")'''

#to mention the error
'''try:
    a=int(input("enter a value:"))
    b=int(input("enter a value:"))
    print(a/b)
except Exception as e:
    print("some thing went wrong:",e)
print("the end")
print("___________________________________________________")'''

#TYPE ERROR
'''#eg:1
a=10
b="priyaa"
print(a+b)
#eg:2
a="shanmu"
b="aruna"
print(a/b)'''

#exception handling --->condition like(if,elif,else)
'''try:
    a="edex"
    b=int(input("enter a value:"))
    print(a+b)
except ValueError as e:
    print("Value Error :",e)
except IndexError as e:
    print("Index Error :",e)
except TupeError as e:
    print("Type Error:",e)
except Exception as e:
    print("some thing went wrong:",e)
print("the end")
print("___________________________________________________")'''

#else-->if try true it will call else
'''try:
    a="edex"
    b=int(input("enter a value:"))
    print(a+b)
except Exception as e:
    print("something went wrong:",e)
else:
    print("else block")
print("___________________________________________________")'''

#finally-->if try true,or false it will call finally
'''try:
    a="edex"
    b=int(input("enter a value:"))
    print(a+b)
except Exception as e:
    print("something went wrong:",e)
else:
    print("else block")
finally:
    print("the end")'''


#python errors finding syntax
'''print(dir(locals()['__builtins__']))'''
#python length of the error
'''print(len(dir(locals()['__builtins__'])))'''


#task-1
'''class treasure():
    def box1(self):
        key1=int(input("key1:"))
        print("gold")
    def box2(self):
        key2=int(input("key2:"))
        print("gold")
    def box3(self):
        key3=int(input("key3:"))
        print("gold")+
Dora=treasure()
Dora.box1()
Dora.box2()
Dora.box3()
print("the end")'''

class Treasure:
    def __init__(self):
        self.gold_count = 0
    def box1(self):
        try:
            key1 = int(input("key1: "))
            print("gold")
            self.gold_count += 1
        except ValueError:
            print("something went wrong")
    def box2(self):
        try:
            key2 = int(input("key2: "))
            print("gold")
            self.gold_count += 1
        except ValueError:
            print("something went wrong")
    def box3(self):
        try:
            key3 = int(input("key3: "))
            print("gold")
            self.gold_count += 1
        except ValueError:
            print("something went wrong")
Dora=Treasure()
Dora.box1()
Dora.box2()
Dora.box3()
print("Total gold:" + str(Dora.gold_count))
print("The end")

        

