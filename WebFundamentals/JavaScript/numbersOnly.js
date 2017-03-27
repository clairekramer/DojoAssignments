var arr = [1, 'apple', -3, 'orange', 0.5];
var newArr = [];

function numbersOnly() {
  for (var x = 0; x < arr.length; x++) {
    if (typeof arr[x] === 'number') {
      newArr.push(arr[x]);
    } else {
      continue;
    }
    console.log(newArr);
  }
}

numbersOnly();
