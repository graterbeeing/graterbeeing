shut_down=False

new_user = {}
new_user['name'] = 'Yehuda Arieli'
new_user['age'] = '25'
new_user['city'] = 'JVM'


new_user2 = {}
new_user2['name'] = 'Itay I'
new_user2['age'] = '13'
new_user2['city'] = 'Tel Aviv'

all_users = {
    'Yehuda': new_user,
    'Itay' : new_user2

}

def print_user(user: dict):
  if 'first_name' in user and 'last_name' in user:
    name = f"first name: {user['first_name']}, last name: {user['last_name']}"
  else:
    name = user['name']

  print(f"""name: {name}
age: {user['age']}
city: {user['city']}
""")
  
def add_first_and_last_name(user: dict):
  user['first_name'], user['last_name'] = user['name'].split(' ')


def insert_new_user(all_users):
  name = input('name: ')
  age = input('age: ')
  city = input('city: ')
  all_users[name] = dict(name=name, age=age, city=city)

def insert_new_info(all_users):
  subject=input('subject: ')
  idea=input('about: ')
  information=input('info: ')
  all_users[subject] = dict(name=subject, age=idea, city=information)

def show_all_users(all_users):
  print('Full list:')
  for user in all_users.values():
    print_user(user)


def delete_user(all_users):
  deleted_user=input('what user do you whant to delete? ')
  if deleted_user in all_users:
    all_users.pop(deleted_user)
    print('   user is no longer in database')
  else:
    print('   user was never in the database',
          'please check if you wrote it right'
          )

print('hello and welcom to the new information collection system \n')
print('what would you like to do?')
print(' to search a specific information, type - <show user>',
      '\n to add a first and last name for a person, type- <first and last name>',
      '\n to add new information (person or subject), type- <add info>',
      '\n to show all of the information gathered, type- <show all>',
      '\n to delete any unneeded info, type- <remove>',
      '\n to finish running the program, type- <exit>'
)

while shut_down != True:
  action=input('what now? ')
  action=action.lower()
  
  if action == ('show user'):
    print('\n   searching in users...')
    s_user=input('what info would you like to see? ')
    # s_user is what user to show
    if s_user in all_users:
      print_user(all_users[s_user])
    else:
      print('sorry make sure you wrote it right')
  
  if action == ('first and last name'):
    print('\n   searching in users...')
    n_name=input('witch name to change? ')
    #n_name is what name needs to be split
    add_first_and_last_name(all_users[n_name])
  
  if action == ('add info'):
    info_user=input('   do you want to add a info or a person?')
    info_user=info_user.lower()
    if info_user == ('info'):
      insert_new_info(all_users)
    if info_user == ('person'):
      insert_new_user(all_users)
    print('   new info added')
  
  if action == ('show all'):
    print('\n   searching he database')
    show_all_users(all_users)
  
  if action == ('remove'):
    delete_user(all_users)
  
  if action == ('exit'):
    print('shuting down systems... restarting information')
    shut_down=True