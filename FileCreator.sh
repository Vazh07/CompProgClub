#!/bin/bash

# Specify the directory containing the subfolders
parent_dir="/home/vazh07/Documents/CompetitivePrograming/OCI2023/"

# Loop through each subfolder
for folder in "$parent_dir"/*/; do
    if [ -d "$folder" ]; then
        # Extract the name of the subfolder
        folder_name=$(basename "$folder")

        # Create problem.desc file
        problem_desc_file="$folder/problem.desc"
        touch "$problem_desc_file"
        echo "Description of problem in $folder_name" > "$problem_desc_file"

        # Create sol.cpp file
        sol_cpp_file="$folder/sol.cpp"
        touch "$sol_cpp_file"
        echo "// Solution for problem in $folder_name" > "$sol_cpp_file"

        echo "Files created in $folder_name"
    fi
done
