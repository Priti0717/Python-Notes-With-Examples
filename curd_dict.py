# # #curd operation:
# #c=create
# #u=update
# #r=read
# #d=delete

# #how to access dict:  "var_name[key]"

# mobile={"onepluse":{"ce2":{"storage":"64gb","price":29000,"ram":"164gb"},"ce3":{"storage":"64gb","price":29000,"ram":"164gb"}},"oppo":{"a57":{"storage":"64gb","price":16000,"ram":"64gb"},"f12":{"storage":"123gb","price":10000,"ram":"4gb"}}}
# print(mobile["oppo"])
# print(mobile["onepluse"]["ce2"])
# print(mobile["oppo"]["a57"]["ram"])

# cars={"skoda":{"superb":{"price":"7.65lakhs","milage":"3458000km","seter":5},"kodiaq":{"price":"7.65lakhs","milage":"3458000km","seter":5}},"renault":{"kiger":{"price":"7.65lakhs","milage":"3458000km","seter":5},"duster":{"price":"7.65lakhs","milage":"3458000km","seter":5}}}
# print(cars["renault"])
# print(cars["skoda"]["kodiaq"])
# print(cars["renault"]["duster"]["milage"])

# #by using get() method:
# #var.get(key)

# cars={"skoda":{"superb":{"price":"7.65lakhs","milage":"3458000km","seter":5},"kodiaq":{"price":"7.65lakhs","milage":"3458000km","seter":5}},"renault":{"kiger":{"price":"7.65lakhs","milage":"3458000km","seter":5},"duster":{"price":"7.65lakhs","milage":"3458000km","seter":5}}}
# print(cars.get("skoda"))

# students={1:{"name":"priti","city":"pune","per":88,"marks":{"science":90,"maths":88,"history":98,"geography":87}},2:{"name":"sid","city":"kolhapur","per":84,"marks":{"science":65,"maths":76,"history":87,"geography":63}},3:{"name":"sonal","city":"amravati","per":79,"marks":{"science":78,"maths":87,"history":69,"geography":80}}}
# print(students.get(2))
# print(students[1].get("city"))
# print(students[2].get("marks"))

# #how to update a data from dict:
# #var[key]=updated_value

# students={1:{"name":"priti","city":"pune","per":88,"marks":{"science":90,"maths":88,"history":98,"geography":87}},2:{"name":"sid","city":"kolhapur","per":84,"marks":{"science":65,"maths":76,"history":87,"geography":63}},3:{"name":"sonal","city":"amravati","per":79,"marks":{"science":78,"maths":87,"history":69,"geography":80}}}
# students[1]["city"]="nashik"
# students[2]["marks"]["science"]=88
# print(students)

# #add():var[key]=value
# mobile={"onepluse":{"ce2":{"storage":"64gb","price":29000,"ram":"164gb"},"ce3":{"storage":"64gb","price":29000,"ram":"164gb"}},"oppo":{"a57":{"storage":"64gb","price":16000,"ram":"64gb"},"a14":{"storage":"123gb","price":10000,"ram":"4gb"}}}
# mobile["onepluse"]["ce2"]["camera"]="64mp"
# print(mobile)

#how to delete data from dict:
#pop():
#syntax:var.pop(key)

# ce2={"storage":"64gb","price":29000,"ram":"164gb"}
# print(ce2.pop("ram"))

# mobile={"onepluse":{"ce2":{"storage":"64gb","price":29000,"ram":"164gb"},"ce3":{"storage":"64gb","price":29000,"ram":"164gb"}},"oppo":{"a57":{"storage":"64gb","price":16000,"ram":"64gb"},"a14":{"storage":"123gb","price":10000,"ram":"4gb"}}}
# mobile["onepluse"]["ce3"].pop("storage")
# print (mobile)

sanjay_leela_bhansali={"akshay_kumar":{"rowdy_rathore":{"release":"1may2015","language":"hindi"},"gabbar_is_back":{"release":"1june2012","language":"hindi"}},"ranveer_sing":{"bajirao_mastani":{"release":"8dec2015","language":"hindi"},"padmaavat":{"release":"25jan2018","language":"hindi"}}}
sanjay_leela_bhansali["akshay_kumar"]["rowdy_rathore"]["edited"]=("rajesh_pandey")
sanjay_leela_bhansali["akshay_kumar"]["gabbar_is_back"]["edited"]=("aarti_bajaj")
sanjay_leela_bhansali["ranveer_sing"]["bajirao_mastani"]["edited"]=("rajesh_pandey")
sanjay_leela_bhansali["ranveer_sing"]["padmaavat"]["edited"]=("rajesh_pandey")
print(sanjay_leela_bhansali)
sanjay_leela_bhansali["akshay_kumar"]["rowdy_rathore"]["release"]=(2015)
sanjay_leela_bhansali["akshay_kumar"]["gabbar_is_back"]["release"]=(2012)
sanjay_leela_bhansali["ranveer_sing"]["bajirao_mastani"]["release"]=(2015)
sanjay_leela_bhansali["ranveer_sing"]["padmaavat"]["release"]=(2018)
print(sanjay_leela_bhansali)
sanjay_leela_bhansali["akshay_kumar"]["rowdy_rathore"].pop("language")
sanjay_leela_bhansali["akshay_kumar"]["gabbar_is_back"].pop("language")
sanjay_leela_bhansali["ranveer_sing"]["bajirao_mastani"].pop("language")
sanjay_leela_bhansali["ranveer_sing"]["padmaavat"].pop("language")
print(sanjay_leela_bhansali)