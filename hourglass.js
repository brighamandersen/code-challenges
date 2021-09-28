'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

function hourglassSum(arr) {
    let sums = []
    
    for (let i = 1; i < arr.length - 1; i++) {
        for (let j = 1; j < arr.length - 1; j++) {
            let topSection = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
            let midSection = arr[i][j]
            let bottomSection = arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            let currentSum = topSection + midSection + bottomSection
            sums.push(currentSum)
        }
    }
    return Math.max(...sums)
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    let arr = Array(6);

    for (let i = 0; i < 6; i++) {
        arr[i] = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }

    const result = hourglassSum(arr);

    ws.write(result + '\n');

    ws.end();
}
