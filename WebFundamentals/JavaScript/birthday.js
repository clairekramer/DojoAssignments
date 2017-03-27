for (var bday = 60; bday > -1; bday--) {
  if (bday > 30) {
    console.log(bday, 'days until my birthday. :(');
  } else if (bday > 5) {
    console.log('My birthday is only', bday, 'days away!')
  } else if (bday > 0) {
    console.log(bday, 'DAYS UNTIL MY BIRTHDAY!!!!')
  } else {
    console.log('IT IS MY BIRTHDAY!!!!')
  }
}

console.log();
