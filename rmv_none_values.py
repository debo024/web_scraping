
import json

#prompt the user for a file to import

filename = 'news.json'
list_x = []
count_y = []
u = 0


#Read JSON data into the datastore variable
if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)
        
#Use the new datastore datastructure
for n in datastore:
    list_x.append(n["important"])

#Counting number of ocuurences of "PUBG" keyword also can be changed to user
#defined requirewments to get the neutrality.

list_x[:] = (value for value in list_x if value != None)

for y in range(len(list_x)):
    list_y = list_x[y]
    u = u+ list_y.count('PUBG')   #
    

print(u)