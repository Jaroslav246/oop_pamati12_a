from prettytable import PrettyTable
table=PrettyTable()
table.field_names= ['Name', 'Age', 'City']
table.add_now (['Emily','15','Daugavpils'])
print(table)