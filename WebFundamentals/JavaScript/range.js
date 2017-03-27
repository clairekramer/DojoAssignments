function printRange(start, end, skip) {
  for(var x = start; x < end; x = x + skip) {
    console.log(x);
  }
}

printRange(2, 10, 2);
