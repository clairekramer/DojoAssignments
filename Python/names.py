#Part 1
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def partOne(givenDict):
    for item in givenDict:
        print item['first_name'], item['last_name']

partOne(students)

#Part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def partTwo(givenList):
     num = 0
     for item in givenList:
         print item
         for person in givenList[item]:
             num = num + 1
             print num, '-', person['first_name'].upper(), person['last_name'].upper(), '-', len(person['first_name']+person['last_name'])


partTwo(users)
