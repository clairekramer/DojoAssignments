function lottery(numTokens) {
    while (numTokens > 0) {
      var randomNumber = Math.floor(Math.random() * 100) + 1;
      if (randomNumber === 1) {
        var payout = Math.floor(Math.random() * (100 - 50 + 1)) + 50;
        console.log('You have won ' + payout + ' tokens!');
        numTokens = numTokens + payout;
        console.log('You have ' + numTokens + ' left.');
      } else {
          numTokens--;
          console.log('You did not win. Please try again.');
          console.log('You have ' + numTokens + ' left.');
      }
    }
}

var tokens = 1;
while(tokens) {
  lottery(tokens);
}
