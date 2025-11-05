//code for which number is larger

// function compareNumber(n1,n2){
//     if(n1>n2){
//         console.log(`the Larger number is: ` +n1);
//     }

//     else if(n2>n1){
//         console.log(`the Larger number is: ` +n2);
//     }

//     else{
//         console.log(`Numbers are equal`)
//     }
// }

// compareNumber(45,55)


//Write a JavaScript for loop that iterates from 0 to 15.
//For each iteration, it checks if the current number is
//odd or even, and displays a message on the screen.

// for(let i = 0 ; i <= 100 ; i++ ){
//     if(i % 2 == 0)
//         {
//         console.log(` ${i} is even`);
//         }
    
//     else{
//         console.log(` ${i} is odd `);
        
//     }
// }

//Write a JavaScript program that computes the average marks of the 
// following students. Then, this average is used to determine the 
// corresponding grade.


// Student Name	Marks
// David	80
// Vinoth	77
// Divya	88
// Ishitha	95
// Thomas	68
// The grades are computed as follows :

// Range	Grade
// <60	F
// <70	D
// <80	C
// <90	B
// <100	A


//to find the average 

let p1 = 80
let p2 = 77
let p3 = 88
let p4 = 95
let p5 = 68

let sum = p1+p2+p3+p4+p5

console.log(sum)
console.log(typeof(sum))

let average = (sum) / 5

console.log(average)
console.log(typeof(average))

let marks = [80, 77, 88, 95, 68]

for(let i of marks){
    
    console.log();
    
}
