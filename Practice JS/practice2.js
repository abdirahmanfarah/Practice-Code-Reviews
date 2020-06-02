const _ = {};

//Takes array as args where forEach is a method on an array
// .each is called with three args, (element, index, list)
_.each = function (list, callback) {
  // check if the first argument is an array
  if (Array.isArray(list)) {
    // loop through array
    for (let i = 0; i < list.length; i++) {
      // call the callback with a list item
      callback(list[i], i, list);
      // list[i] is the value, or element, i is the index, and list the array
    }else { //object
        // loop through object
        for(var key in list){
           callback(list[key], key, list) //key is property name
      }
  }
};

_.map = function(list, callback) {
    var storage = [];

    // for(var i =0; i<list.length; i++){
    //     storage.push(callback(list[i], i, list));
    // }
    _.each(list, function(v, i, list) {
        storage.push(callback(v, i, list))
    });
    return storage;
}
_.map([1,2,3], function(val) {return val + 1;})


_.each(["sally", "george", "porgie"], function (name, i, list) {
  if (list[i + 1]) {
    console.log(name, "is younger than", list[i + 1]);
  } else {
    console.log(name, "is the oldest");
  }
});


// Map
const weapons = ["candlestick", "lead pipe", "revolver"];

const makeBroken = function (item) {
  return `broken ${item}`;
};

const brokenWeapons = _.map(weapons, makeBroken);

brokenWeapons;

// Filter

_.filter = function(arr, cb){
    const storage = [];
    // loop through array
    
    // _.each(arr, function(item, i, list) {
    //     if(cb(item, i, list) === true){
    //          storage.push(item)
    //     }
    // });

    for(let i=0; i<arr.length; i++){
        // check if cb return true because we are filtering through array
        if(cb(arr[i], i, arr) === true){ //arr[i] is element, i is index, and arr is arr
            // if returns true, push into array
            storage.push(arr[i])
        }
    }
    return storage;
}

