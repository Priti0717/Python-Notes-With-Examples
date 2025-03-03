#key()=return list of keys
#syntax=var.keys()
l={1:"priti",2:"sid"}
print(l.keys())#dict_keys([1, 2])
#values()=return list values
#syntax=var.values()
l={1:"priti",2:"sid"}
print(l.values())#dict_items([(1, 'priti'), (2, 'sid')])
#items()=returns list of tuple of key and values
#syntax=var.items()
l={1:"priti",2:"sid"}
print(l.items())#dict_items([(1, 'priti'), (2, 'sid')])


sanjay_leela_bhansali={"akshay_kumar":{"rowdy_rathore":{"release":"1may2015","language":"hindi"},"gabbar_is_back":{"release":"1june2012","language":"hindi"}},"ranveer_sing":{"bajirao_mastani":{"release":"8dec2015","language":"hindi"},"padmaavat":{"release":"25jan2018","language":"hindi"}}}
print(sanjay_leela_bhansali.keys())#dict_keys(['akshay_kumar', 'ranveer_sing'])
print(sanjay_leela_bhansali["akshay_kumar"].keys())#dict_keys(['rowdy_rathore', 'gabbar_is_back'])
print(sanjay_leela_bhansali["akshay_kumar"]["rowdy_rathore"].keys())#dict_keys(['release', 'language'])
print(sanjay_leela_bhansali.values())#dict_values([{'rowdy_rathore': {'release': '1may2015', 'language': 'hindi'}, 'gabbar_is_back': {'release': '1june2012', 'language': 'hindi'}}, {'bajirao_mastani': {'release': '8dec2015', 'language': 'hindi'}, 'padmaavat': {'release': '25jan2018', 'language': 'hindi'}}])
print(sanjay_leela_bhansali["ranveer_sing"].values())#dict_values([{'release': '8dec2015', 'language': 'hindi'}, {'release': '25jan2018', 'language': 'hindi'}])
print(sanjay_leela_bhansali["ranveer_sing"]["padmaavat"].values())#dict_values(['25jan2018', 'hindi'])
print(sanjay_leela_bhansali.items())#dict_items([('akshay_kumar', {'rowdy_rathore': {'release': '1may2015', 'language': 'hindi'}, 'gabbar_is_back': {'release': '1june2012', 'language': 'hindi'}}), ('ranveer_sing', {'bajirao_mastani': {'release': '8dec2015', 'language': 'hindi'}, 'padmaavat': {'release': '25jan2018', 'language': 'hindi'}})])
print(sanjay_leela_bhansali["ranveer_sing"].items())#dict_items([('bajirao_mastani', {'release': '8dec2015', 'language': 'hindi'}), ('padmaavat', {'release': '25jan2018', 'language': 'hindi'})])
print(sanjay_leela_bhansali["ranveer_sing"]["padmaavat"].items())#dict_items([('release', '25jan2018'), ('language', 'hindi')])