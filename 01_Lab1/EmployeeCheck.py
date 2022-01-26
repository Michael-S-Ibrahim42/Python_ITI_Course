#checking employees list
company_emps = ['Michael', 'Samir', 'Barsoum']
def isEmployee(name):
  for emp in company_emps:
    if name == emp:
      print(True)
    else:
      print(False)

if __name__ == '__main__':
  isEmployee('Michael')