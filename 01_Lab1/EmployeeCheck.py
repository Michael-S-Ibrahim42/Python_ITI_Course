def isEmployee(name):
  for emp in companyEmps:
    if name == emp:
      return True
    else:
      return False
      
      
if __name__ == '__main__':
  isEmployee('Michael')