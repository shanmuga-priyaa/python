#nested dis
#eg:1
sivakumar={"son1":{"name":"surya",
                "location":"chennai",
                "age":50},
          "son2":{"name":"karthi",
                "location":"madurai",
                "age":47}
          }
print(sivakumar)
print(sivakumar["son1"]["location"])
print(sivakumar["son2"]["age"])
print("-----------------------------------------")

#eg:2
sivakumar={"son1":{"name":"surya",
                "location":"chennai",
                "age":50},
          "son2":{"name":"karthi",
                "location":"madurai",
                "age":47}
          }
for i,j in sivakumar.items():
    print()
    print(i)
    for x,y in j.items():
        print(x,y)
print("-----------------------------------------")


