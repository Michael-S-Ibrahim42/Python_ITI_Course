import sys

def helpFn():
  print('--help     :     To show help')
  print('--add      :     To add a new contact')
  print("--modify   :     To modify a contact's phone, mail, or address")
  print("--show     :     To show contact's info")
  print("--del      :     To delete a contact from the phonebook")

def add():
  with open('ContactsPhoneBook.txt', 'a') as file:
    None
  with open('ContactsPhoneBook.txt', 'r') as file:
    lines = [line for line in file]
    if len(lines) == 0:
      index = 0
    else:
      dic = eval(lines[len(lines)-1])
      index = dic['Index'] + 1
  contactDic = {}
  contactDic['Index']   = index
  contactDic['Name']    = input('Enter name: ').strip()
  contactDic['Phone']   = input('Enter phone: ')
  contactDic['E-mail']  = input('Enter e-mail: ')
  contactDic['Address'] = input('Enter address: ')
  with open('ContactsPhoneBook.txt', 'a') as file:
    file.write(str(contactDic)+'\n')
    
def modify():
  with open('ContactsPhoneBook.txt', 'a') as file:
    None
  with open('ContactsPhoneBook.txt', 'r') as file:
    pBook = [eval(line) for line in file]
  matchedContacts = []
  name = input('Enter contact name to modify: ')
  matchedContacts = [dic for dic in pBook if dic['Name'].lower() == name.lower()]
  if len(matchedContacts) == 0:
    print('The entered name is not found')
  else:
    print('Modification Fields:\n1-Phone\n2-E-mail\n3-Address\n', end = "")
    selection = input('Enter number of your selection: ')
    while (not selection.isnumeric()) or (int(selection) > 3) or (int(selection) < 1) :
      selection = input('Enter valid number of your selection: ')
    switcher = {
      '1': 'Phone',
      '2': 'E-mail',
      '3': 'Address'
    }
    modifyItem = switcher.get(selection)
    for dic in matchedContacts:
      print('-----------------------------------')
      for k, v in dic.items():
        print(str(k) + '\t:' + str(v))
      print('-----------------------------------')
    selectedIndex = input('Enter the index of the contact you want to modify: ')
    newValue = input('Enter new value: ')
    for dic in pBook:
      if dic['Index'] == int(selectedIndex):
        dic[modifyItem] = newValue
    with open('ContactsPhoneBook.txt', 'w') as file:
      for dic in pBook:
        file.write(str(dic)+'\n')
        
def show():
  selection = input('Enter the number of your selection:\n1-Show all the PhoneBook.\n2-Show selected contact.\n')
  if selection == '1':
    with open('ContactsPhoneBook.txt', 'a') as file:
      None
    with open('ContactsPhoneBook.txt', 'r') as file:
      pBook = [eval(line) for line in file]
    for dic in pBook:
      print('-----------------------------------')
      for k, v in dic.items():
        print(str(k) + '\t:' + str(v))
      print('-----------------------------------')      
  else:
    name = input('Enter contact name: ')
    with open('ContactsPhoneBook.txt', 'a') as file:
      None
    with open('ContactsPhoneBook.txt', 'r') as file:
      pBook = [eval(line) for line in file]
    matchedContacts = [dic for dic in pBook if dic['Name'].lower() == name.lower()]      
    if len(matchedContacts) == 0:
      print('Contact is not exist')
    for dic in matchedContacts:
      print('-----------------------------------')
      for k, v in dic.items():
        print(str(k) + '\t:' + str(v))
      print('-----------------------------------')      
      
def delete():
  pBook = []
  index = 0
  selection = input('Enter the number of your selection:\n1-Delete all the PhoneBook.\n2-Delete selected contact.\n')
  if selection == '1':
    with open('ContactsPhoneBook.txt', 'w') as file:
      None
  else:
    name = input('Enter contact name to delete: ')
    with open('ContactsPhoneBook.txt', 'r') as file:
      for line in file:
        dic = eval(line)
        if dic['Name'].lower() != name.lower():
          dic['Index'] = index
          index += 1
          pBook.append(dic)
    with open('ContactsPhoneBook.txt', 'w') as file:
      for dic in pBook:
        file.write(str(dic)+'\n')

def err():
  print('Error in entering command line argument')
  
def main():
  if len(sys.argv) == 1:
    helpFn()
  else:
    switcher = {
      "--help"     :     helpFn,
      "--add"      :     add,
      "--modify"   :     modify,
      "--show"     :     show,
      "--showAll"  :     show,
      "--del"      :     delete,
      "--delAll"   :     delete
    }
    switcher.get(sys.argv[1], err)()

if __name__ == '__main__':
  main()