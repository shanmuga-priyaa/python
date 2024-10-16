#eg:0
'''shop_name= input("Enter the shop name:")
print(shop_name)
print("-"*70)
print("product list:")
type=("Mobiles"+"\t\t\t"+"TV"+"\t\t\t"+"Laptop"+"\t\t\t")
print(type)
print("\n")
item=input("choose your items:")
if item =="mobile":
        print("mobile list:")
print("readmi"+"\t\t\t"+"oppo"+"\t\t\t"+"vivo"+"\t\t\t")
print("-"*70)
if item =="tv":
        print("tv list:")
        print("LG"+"\t\t\t"+"Samsung"+"\t\t\t"+"Soni"+"\t\t\t")
print("-"*70)
if item =="laptop":
        print("laptop list:")
        print("DELL"+"\t\t\t"+"HP"+"\t\t\t"+"Lenova"+"\t\t\t")'''

#eg:1
'''shop_name = input("Enter the shop name: ")
print(shop_name)
print("-" * 70)
products = {
    "mobile": ["Redmi","Vivo", "Oppo"],
    "tv": ["LG", "Samsung", "Sony"],
    "laptops": ["Dell", "HP", "Lenovo"]
}
print("Product List:")
print("Mobile","TV","Laptops",sep="\t\t")
item = input("\nChoose your item: ").lower()
print("-" * 70)

if item in products:
    print(item + " list:")
    for product in products[item]:
        print(product, end="\t\t")
    print("\n" + "-" * 70)
else:
    print("\nInvalid choice. Please choose from mobile, tv, or laptops.")'''


#eg:3   
print("-----*10","DMART","-----*10")
print("Product List")

product = {
    "Mobiles": ["Redmi", "Vivo", "Oppo"],
    "Tv": ["LG", "Samsung", "Sony"],
    "Laptops": ["Dell", "HP", "Lenova"]
}
for i,j in product.items():
    print(i,end="\t\t\t")
print("-------------------------------------------")
pick1=input("Pick any one :")
print("-------------------------------------------")

for i,j in product.items():
    if i == pick1:
        print(pick1)
        for x in j:
            print(x,end="\t\t\t")

      #Module2      
Brands={"Redmi":{"Brand Name": "Redmi",
                 "Model Name": "Note 10 pro",
                 "Ram": "6gb",
                 "price": 20000,
                 "Gst":10,
                 "Final Price":22000
                 },
        "Vivo":{"Brand Name": "Vivo",
                 "Model Name": "Note y50",
                 "Ram": "5gb",
                 "price": 30000,
                 "Gst":10,
                 "Final Price":33000
                 },
        "Oppo":{"Brand Name": "Oppo",
                 "Model Name": "Oppo f7",
                 "Ram": "6gb",
                 "price": 20000,
                 "Gst":10,
                 "Final Price":22000
                 },
        "Lg":{"Brand Name": "LG",
                 "Model Name": "lg smart TVs ",
                 "Ram": "6gb",
                 "price": 30000,
                 "Gst":10,
                 "Final Price":33000
                 },
        "Samsung":{"Brand Name": "Samsung",
                 "Model Name": "samsung 4K UHD",
                 "Ram": "6gb",
                 "price": 40000,
                 "Gst":10,
                 "Final Price":44000
                 },
        "Sony":{"Brand Name": "Sony",
                 "Model Name": "sony 4K Ultra HD",
                 "Ram": "6gb",
                 "price": 30000,
                 "Gst":10,
                 "Final Price":33000
                 },
        "Dell":{"Brand Name": "Dell",
                 "Model Name": "Dell Latitude E5430",
                 "Ram": "6gb",
                 "price": 50000,
                 "Gst":10,
                 "Final Price":55000
                 },
        "Hp":{"Brand Name": "HP",
                 "Model Name": "HP 15s-eq2144au",
                 "Ram": "8gb",
                 "price": 55000,
                 "Gst":8000,
                 "Final Price":63000
                 },
        "Lenova":{"Brand Name": "Lenova",
                 "Model Name": "lenova 3WIN",
                 "Ram": "6gb",
                 "price": 32000,
                 "Gst":8000,
                 "Final Price":40000
                 }, 
       }
print()
pick2=input("Enter the name:").lower()
print("----------------------------------------------------")
for i,j in Brands.items():
    if i == pick2.capitalize():
        print(pick2)
        for x,y in j.items():
            print(x,y,sep="\t\t")
            #module3
print("Buy now","close",sep="\t"*4)
print("-------------------------------------------------------")
pick3=input("Enter the name:").lower()
if pick3=="buy now":
    name=input("Name:")
    mobile_number=input("Mobile Namber:")
    address=input("Address:")
    quantity=int(input("Quantity :"))
    product_details = Brands[pick2.capitalize()]["Brand Name"] + Brands[pick2.capitalize()]["Model Name"]
    final_price = quantity * Brands[pick2.capitalize()]["Final Price"]
    print("Name","Mobile Namber","Address","Product Details","Quantity","Total Price",sep="\t"*2)
    print(name,mobile_number,address,quantity,product_details,final_price,sep="\t\t\t")

else:
    print("Thank You")
