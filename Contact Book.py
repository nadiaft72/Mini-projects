def sazande():
    contact_list = list()
    Person = dict()
    Person['name'] = 'ali1'
    Person['phone_number'] = 'ali1'
    Person['address'] = 'ali1'
    Person['email'] = 'ali1'
    contact_list.append(Person)
    
    Person = dict()
    Person['name'] = 'ali2'
    Person['phone_number'] = 'ali2'
    Person['address'] = 'ali2'
    Person['email'] = 'ali2'
    contact_list.append(Person)
    
    Person = dict()
    Person['name'] = 'ali3'
    Person['phone_number'] = 'ali3'
    Person['address'] = 'ali3'
    Person['email'] = 'ali3'
    
    contact_list.append(Person)
    Person = dict()
    Person['name'] = 'ali4'
    Person['phone_number'] = 'ali4'
    Person['address'] = 'ali4'
    Person['email'] = 'ali4'
    contact_list.append(Person)
    
    Person = dict()
    Person['name'] = 'ali5'
    Person['phone_number'] = 'ali5'
    Person['address'] = 'ali5'
    Person['email'] = 'ali5'
    contact_list.append(Person)

    return contact_list

def create():
    Person = dict()
    Person['name'] = input("name = ")
    Person['phone_number'] = input("phone_number = ")
    Person['address'] = input("address = ")
    Person['email'] = input("email = ")
    return Person

def find(contact_list , name):
    person = next ((item for item in contact_list if item["name"] == name ), None)
    return person


def delete(contact_list , name):
    for i, contact in enumerate(contact_list):
        if contact['name'] == name:
            person = contact_list.pop(i)
            return person
    return -1

def update(contact_list , name):
    person = delete(contact_list , name)
    if person != -1 :
        newPerson = dict()
        
        name = input("name is %s, wanna change it? if not press -1 :" %person["name"])
        if name != -1 :
            newPerson['name'] = name
        else :
            newPerson['name'] = person['name']
        
        phone_number = input("phone_number is %s, wanna change it? if not press -1 :" %person["phone_number"])
        if phone_number != -1 :
            newPerson['phone_number'] = phone_number
        else :
            newPerson['phone_number'] = person['phone_number']
        
        address = input("address is %s, wanna change it? if not press -1 :" %person["address"])
        if address != -1 :
            newPerson['address'] = address
        else :
            newPerson['address'] = person['address']
        
        email = input("email is %s, wanna change it? if not press -1 :" %person["email"])
        if phone_number != -1 :
            newPerson['email'] = email
        else :
            newPerson['email'] = person['email']
        
        return newPerson
    else :
        return -1


contact_list = list()
contact_list = sazande()
again = 1
while again == 1:
    if len(contact_list) == 0:
        contact_list.append(create())
    else:
        x = input("do you want to save(s) or find(f) or update(u) or delete(d) or listed save contact(l) and for exit(e) press the word : ")
        
        if x == 's' : 
            contact_list.append(create())
        elif x== 'f' :
            name = input("name = ")
            person = find(contact_list , name)
            if person != None :
                print (person)
            else:
                print("NONE")

        elif x== 'u' :
            name = input("name of who you want to update : ")
            person = update(contact_list , name)
            if person != -1 :
                contact_list.append(person)
                print("update Done!")
            else:
                print("Not found")



        elif x== 'd' :
            name = input("name = ")
            person = delete(contact_list , name)
            if person != -1 :
                print("deleted !")
            else:
                print("not found")
            

        elif x== 'l' :
            for i, contact in enumerate(contact_list):
                print (contact)


print(contact_list)
