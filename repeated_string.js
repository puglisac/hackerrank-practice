// Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.

// Given an integer, n, find and print the number of letter a's in the first  letters of Lilah's infinite string.

// For example, if the string s='abcac and n=10 , the substring we consider is abcacabcac, the first 10 characters of her infinite string. There are 4 occurrences of a in the substring.

// Function Description

// Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length n in the infinitely repeating string.

// repeatedString has the following parameter(s):

// s: a string to repeat
// n: the number of characters to consider
// Input Format

// The first line contains a single string, s.
// The second line contains an integer, n.


function countA(s, n) {
    const rem = n % s.length;
    const addRem = s.slice(0, rem);
    let counter = 0;
    let remainderCount = 0;
    for (char of s) {
        if (char == "a") {
            counter++;
        }
    }
    for (char of addRem) {
        if (char == "a") {
            remainderCount++;
        }
    }
    return counter * Math.floor(n / s.length) + remainderCount;
}

console.log(countA("abaa", 10));