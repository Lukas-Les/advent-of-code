#!/bin/bash

# Read input from the file
task_input=$(<input.txt)

# Define a function to create batches and sum the top three
create_batches() {
    echo "$1" | awk 'BEGIN { RS = ""; FS = "\n" }
    {
        sum = 0
        for (i = 1; i <= NF; i++) {
            sum += $i
        }
        print sum
    }' | sort -nr | head -n 3 | awk '{ sum += $1 } END { print sum }'
}

# Call the function and print the result
create_batches "$task_input"
