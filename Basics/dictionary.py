days_mont={'jan':12,'feb':22,'sep':23}
print(days_mont)
print(type(days_mont))
states_USA={'CA':'CALIFORNIA','NY':'NEW YORK','NJ':'NEW JERSEY','T':'TEXAS'}
print(states_USA)
print(type(states_USA))
#iterating a dictionary using loops
for key,value in states_USA.items():
    print(key,value)
#simple method for keys
for key in states_USA.keys():
    print(key)
#simple method for values
for value in states_USA.values():
    print(value)
#replacing old with new
days_month={'jan':12,'feb':22,'sep':23,'feb':23}
print(days_month)
footballer_goals={'abds':123,'ascd':132,'cr':220,'messi':126}
print(sorted(footballer_goals,reverse=True)) #sort not on value but on alphabets of keys like m comes first and a goes last
key_list=sorted(footballer_goals)
for key in key_list:
    print(key)
sorted_footballers=sorted(footballer_goals.items(),reverse=True)
print(sorted_footballers)#sorted on alphabets
dictionary=dict(sorted_footballers)
print(dictionary)#made a dictionary by using dict
#replace value
footballer_goals['messi']=1
print(footballer_goals)
#add new key
footballer_goals['dfgh']=10
print(footballer_goals)
#maximum player goal and name
value_max=0
key_max=' '
for key,value in footballer_goals.items():
    if value>value_max:
        value_max=value
        key_max=key
print(f"the player name {key_max} has maximum goals {value_max}")
sorted_footballers=sorted(footballer_goals.items(),key=lambda item:item[1],reverse=True)
print(sorted_footballers)#sorted by values not by name
dictionary=dict(sorted_footballers)
print(dictionary)#converted into dictionary
