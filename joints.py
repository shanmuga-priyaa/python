'''#union->it should be in print or we can store in a variable and print it

#eg:0
#wrong method->by using this method it only print the s1
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.union(s2)
print(s1)
print("------------------------------------------")

#eg:1
s1={1,2,3,4,5}
s2={4,5,6,7,8}
union_set=s1.union(s2)
print(union_set)
print("------------------------------------------")

#eg:2
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.union(s2))
print("------------------------------------------")

#eg:3
s1={10,12,23,"apple","mango"}
s2={"Mango","apple","orange"}
set_union=(s1.union(s2))
print(s1)
print("------------------------------------------")

#intersection->it should be in print or we can store in a variable and print it
#eg:0
s1={1,2,4,5,6}
s2={2,4,7,9,10}
new_set=s1.intersection(s2)
print(new_set)
print("------------------------------------------")

#eg:1
#difference->it should be in print or we can store in a variable and print it
#*in difference it will remove the same value and print the left set vale

#eg:0
s1={1,2,4,5,6}
s2={2,4,7,9,10}
new_set=s1.difference(s2)
print(new_set)
print("------------------------------------------")

#eg:1
s1={1,2,4,5,6}
s2={2,4,7,9,10}
new_set=s2.difference(s1)
print(new_set)
print("------------------------------------------")

#eg:using (union,intersection,difference)
s1={1,2,3,4,5}
s2={4,5,6,7,8}
u_set=s1.union(s2)
i_set=s1.intersection(s2)
d_set=s2.difference(s1)
print(u_set)
print(i_set)
print(d_set)
print("------------------------------------------")


#symmetric_difference()->it will remove the same value in the set and ring remaning
s1={1,2,3,4}
s2={4,5,6,7}
dset1=s1.difference(s2)
dset2=s2.difference(s1)
sdset1=s1.symmetric_difference(s2)
print(dset1)
print(dset2)
print(sdset1)
print("------------------------------------------")

#symmetric_difference_update()-> no need for print,are a another variable
s1={1,2,3,4}
s2={4,5,6,7}
s1.symmetric_difference_update(s2)
print(s1)
print("------------------------------------------")

#intersection_update
s1={1,2,3,4}
s2={4,5,6,7}
s1.intersection_update(s2)
print(s1)
print("------------------------------------------")'''

#join->it ah common intersection values
#disjoin->it has no intersection values

#isdisjoint->it return boolean values 
#eg:1
s1={1,2,3,4}
s2={4,5,6,7}
print(s1.isdisjoint(s2))
print("------------------------------------------")

#eg:2
s1={1,2,3}
s2={4,5,6,7}
print(s1.isdisjoint(s2))
print("------------------------------------------")


#group1(1,2,3,4,5)->so more members it is superset,group2(3,4)->less members subset
#issuperset->which have high value
#eg:0
print("------------superset--------------------------")
s1={"apple","mango","grapes","banana"}
s2={"apple","grapes"}
print(s1.issuperset(s2))
print(s2.issubset(s1))
print("------------------------------------------")

#eg:1
print("------------not a superset--------------------------")
s1={"apple","mango","grapes","banana"}
s2={"apple","grapes","orange"}
print(s1.issuperset(s2))
print(s2.issubset(s1))
print("------------------------------------------")



