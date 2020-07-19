function flatten(exampleArr){
    for(let i = 0; i<exampleArr.length; i++){
        if(i == [ or i == ]){
            exampleArr.pop(i)
        }
        else{
            i += 1
        }
    }
    return exampleArr
}

console.log(flatten([1,2,[3,4 [5,6,7], 8], 9, 10]))