var arr = ["James", "Jill", "Jane", "Jack"];


function fancy() {
  for (var x = 0; x < arr.length; x++) {
    console.log(x, '->', arr[x]);
  }
}

fancy();
