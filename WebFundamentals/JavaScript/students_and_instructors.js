var users = {
 'Students': [
     {
       first_name:  'Michael',
       last_name : 'Jordan',
       number : 13
     },
     {
       first_name : 'John',
       last_name : 'Rosales',
       number : 11
     },
     {
       first_name : 'Mark',
       last_name : 'Guillen',
       number : 11
     },
     {
       first_name : 'KB',
       last_name : 'Tonel',
       number : 7
     }
  ],

 'Instructors': [
     {
       first_name : 'Michael',
       last_name : 'Choi'
     },
     {
       first_name : 'Martin',
       last_name : 'Puryear'
     }
  ]
 }

function call(myList) {
  console.log('Students');
  for (var x = 0; x < myList.Students.length; x++) {
      console.log((x+1)+" - "+myList.Students[x].first_name.toUpperCase()+" "+ myList.Students[x].last_name.toUpperCase()+" - "+(myList.Students[x].first_name.length+myList.Students[x].last_name.length));
  }
  console.log('Instructors');
  for(var y = 0; y < myList.Instructors.length; y++) {
      console.log((y+1)+" - "+myList.Instructors[y].first_name.toUpperCase()+" "+ myList.Instructors[y].last_name.toUpperCase()+" - "+(myList.Instructors[y].first_name.length+myList.Instructors[y].last_name.length));
  }
}

call(users);
