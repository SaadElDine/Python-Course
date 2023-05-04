from prettytable import PrettyTable

table = PrettyTable()
table.add_column("ID",[1,2,3,4,5])
table.add_column("Name",["Saad","KOKO","Domza","Deiboz","Doula"])

table.align = "l"
print(table)