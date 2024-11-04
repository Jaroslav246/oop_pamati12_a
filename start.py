import json

organizations = []
file=open('organizations.json', 'r')
data=json.load(file)
file.close()
organizations=data['organizations']
print('DATI PIEVIENOTI')
while (True):
    response=input('(1) - Pievieno organizāciju // (2) - Izvada organizāciju // (3) Beigt: ')
    if response=='1':
        organization_name=input('Organization nosaukums: ')
        organization_adress=input('Organization adresse: ')
        organization_id=input('Organization id: ')

        organization={
            'name':organization_name,
            'adress':organization_adress,
            'id': organization_id,
             'contacts': []
         }
        while (True):
            response=input('Vai vēlies pievienot kontaktu (jā/nē)')
            if response=='jā':
                print('Darbinieka informācija:')
                contact_name = input('Ievadiet Darbinieka vārdu: ')
                contact_position = input('Darbinieka adresse: ')
                contact_id = input('Darbinieka id: ')
                contact = {
                    'name': contact_name,
                    'position': contact_position,
                    'id': contact_id
                }
                organization['contacts'].append(contact)
            elif response == 'nē':
               break
        organizations.append(organization) 
        
    elif response =='2':
        for organization in organizations:
            print('---ORGANIZATION---')
            print(f"{organization['name']} ({organization['id']})")
            print(f"Adrese:{organization['adress']}")
            print(f"Kontaktu skaits: {len(organization['contacts'])}")
    elif response=='3':
        data = {
            'organizations': organizations
        }
        print('SAGLĀBA DATUS.....')
        file = open('organizations.json', 'w')
        json.dump(data, file, indent=4)
        print('Paldies, par darbu!')
        print(organizations)
        exit()
    else:
        print('Izvele skaitļu 1,2 vai 3')
        continue