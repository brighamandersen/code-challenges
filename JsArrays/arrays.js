/* PUSH TO FRONT - CUSTOM (NO BUILT-IN METHODS) */

function pushToFront(arr, val) {
  // Shift all values to the right 1
  for (let i = arr.length - 1; i >= 0; i--) {
    arr[i+1] = arr[i]
  }
  // Change first value to be what was passed in
  arr[0] = val
  // Return the modified array
  return arr
}

let array = [1,2,3,4]
console.log('Original: ', array)
array = pushToFront(array, 5)
console.log('After push to front: ', array, '\n')


/* INSERT - CUSTOM (NO BUILT-IN METHODS) */

function insert(arr, idx, val) {
  // Shift all values from that index to the right to the right 1
  for (let i = arr.length - 1; i >= idx; i--) {
    arr[i+1] = arr[i]
  }
  // Change the value at that index to be new value
  arr[idx] = val
  // Return the modified array
  return arr
}

array = [1,2,3,4]
console.log('Original: ', array)
array = insert(array, 2, 5)
console.log('After insertion: ', array, '\n')


/* POP FROM FRONT - CUSTOM (NO BUILT-IN METHODS) */

function popFromFront(arr) {
  // Store first value since it will be popped off and returned
  let poppedVal = arr[0]
  // Shift all items but first one to the left 1
  for (let i = 1; i < arr.length; i++) {
    arr[i-1] = arr[i]
  }
  // Remove last item from array (items got shifted left 1, so it shouldn't exist)
  arr.pop()   // This probably is a built-in method, but I'm not sure how to remove an element - setting it to undefined still shows it
  // Return the modified array and the value that got popped off
  return {arr, poppedVal}
}

array = [1,2,3,4]
console.log('Original: ', array)
let {array: arr, poppedVal} = popFromFront(array)
console.log('After pop from front: ', array)
console.log('Value popped off: ', poppedVal, '\n')