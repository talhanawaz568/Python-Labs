#!/bin/bash

# 1. Define functions FIRST
show_date() {
    echo "Current date and time: $(date)"
}

list_files() {
    echo "Files in the current directory:"
    ls
}

exit_script() {
    echo "Exiting..."
    exit 0
}

# 2. Start the menu loop
while true; do 
    echo "==================="
    echo "Bash Menu Interface"
    echo "==================="
    echo "1. Show date"
    echo "2. List files"
    echo "3. Exit"
    echo -n "Enter your choice: "
    
    read choice

    # 3. Handle the choice inside the loop
    case $choice in
        1) show_date ;;
        2) list_files ;;
        3) exit_script ;;
        *) echo "Invalid option!" ;;
    esac
done
