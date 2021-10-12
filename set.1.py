party_goers={'andrew','barbara','carole','david'}
print('no of partygoers:',len(party_goers))
print('type of partygoers:',type(party_goers))
print('name of party goers:',party_goers)
print('did barbara go to party?:','barbara' in party_goers)
students={'karthick','karnan','david','andrew'}
party_students= party_goers.intersection(students)
print(party_students)
typelist=list(party_students)
print(typelist)
print(type(typelist))
print(typelist[1])
diff= party_goers.difference(students)
print(diff)
