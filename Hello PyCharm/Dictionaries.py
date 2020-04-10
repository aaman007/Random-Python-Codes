# Dictionaries [ Key-Value pair ]
customer = {
    "name" : "Aaman Rahman",
    "age" : 30,
    "is_verified" : True
}
print(customer["name"])
# print(customer["NAme"]) ## gives an KeyError
print(customer.get("name"))
print(customer.get("NAme"))  ## returns None
print(customer.get("NAme" , "John Doe"))  ## returns John Doe cause NAme key doesn't exists and John Does was passed as default value
customer["name"] = "Amanur Rahman"  ## Value for name key is updated
print(customer.get("name"))
customer["birthdate"] = "21 April 1997"  ## New Key value pair added to dictionary
print(customer.get("birthdate"))