#!/usr/bin/node
// Script that prints a message depending on the number of arguments passed

const args = process.argv.length - 2; // Subtract 2 to ignore the node and script path arguments

if (args === 0) {
    console.log("No argument");
} else if (args === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}

