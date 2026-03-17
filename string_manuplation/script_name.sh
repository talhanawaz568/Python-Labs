#!/bin/bash
echo "Enter a string"
read user_input
echo "You entered: $user_input"

string_length=${#user_input}
echo "The length of the string is: $string_length"

substring=${user_input:2:4}
echo "Substring from position 2 to 5 : $substring"

modified_string=${user_input//abc/xyz}
echo "Modified string: $modified_string"
