var hour = 7;
var minute = 30;
var period = 'AM';

if (minute < 30 && minute != 0 && minute != 5) {
    if(period == 'PM') {
        console.log('It is just after', hour, 'in the evening.');
    } else{
        console.log('It is just after', hour, 'in the morning.');
    }
} else if (minute > 30) {
    console.log('It is almost', hour+1, period);
} else if (minute == 0) {
    console.log('It is', hour, period, 'on the dot.');
} else if (minute == 30) {
    if(period == 'PM') {
        console.log('It is half past', hour, 'in the evening.');
    } else {
        console.log('It is half past', hour, 'in the morning.');
    }
} else if (minute == 5) {
    if (period == 'PM') {
        console.log('It is five after', hour, 'in the evening.');
    } else {
        console.log('It is five after', hour, 'in the morning.');
    }
} else {
  console.log('It is', hour, minute, period);
}
