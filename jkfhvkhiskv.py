organizations=[]
organizations_a={
    'name':'Tesla Motors',
    'adress':'Tesla ave 1, USA',
    'id':'8646678'
}
organizations_b={
    'name':'Eesti posti',
    'adress':'Super street 1, Tartu',
    'id':'1435677'
}










for organization in organizations:
  print('---ORGANIZATION---')
  print(f"{organization['name']} ({organization['id']})")
  print(f"Adrese:{organization['adress']}")
  print(f"Kontaktu skaits: {len(organization['contacts'])}")