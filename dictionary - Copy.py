#dictionary->key,vaklues
#eg:1
#it is order
d1={"name":"edex",
    "loc":"maudrai",
    "year":2024}
print(d1)
print("------------------------------------------------")

#dublicate->will not be allowed
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
print(d1)
print("--------------------------------------------------")

#mutable->change ,add ,remove
#change
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
d1["name"]="priyaa"
print(d1)
print("--------------------------------------------------")

#add
#update->it should be dic
#eg:1
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
d1.update({"age":21,"color":"blue"})
print(d1)
print("--------------------------------------------------")
#store in another variable and update
#eg:2
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
d2={"age":21,"color":"blue"}
d1.update(d2)
print(d1)
print("--------------------------------------------------")

#pop()->need to pass the key for pop
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
d1.pop("loc")
print(d1)
print("--------------------------------------------------")

#popitem()->last value ill be deleted
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
d1.popitem()
print(d1)
print("--------------------------------------------------")
#clear()->clear the values
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
d1.clear()
print(d1)
print("--------------------------------------------------")
'''#del()->clear the entire set of values
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
del d1
print(d1)
print("--------------------------------------------------")'''

#geting a values using key
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
print(d1["loc"])
print("--------------------------------------------------")

#.get()->if there is no value it will not show error inside none will print
#eg:1
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
print(d1.get("priyaa"))
print("--------------------------------------------------")
#eg:2
#keys()
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
print(d1.get("priyaa","shanmu"))#it will take the course as key and shanmu as values
print("--------------------------------------------------")

#values
#eg:1->keys only
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
d1.keys()
print(d1)
print("--------------------------------------------------")
#eg:2->get values
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
d1.values()
print(d1)
print("--------------------------------------------------")

#items()
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
d1.items()
print(d1)
print("--------------------------------------------------")

#iteration
#eg:1
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
for i,j in d1.items():
    print(i,j)
print("--------------------------------------------------")
#eg:2
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
for i,j in d1.items():
    print(i)
    print(j)
print("--------------------------------------------------")
#eg:3
#without using in bulid func we need to take keys and values
d1={"name":"edex",
    "loc":"maudrai",
    "loc":"maudrai",
    "year":2024}
for i in d1:
    print(i,d1[i])#it will take both key and values  
print("--------------------------------------------------")




