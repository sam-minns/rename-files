# File Renaming Script
A Python script that allows you to rename files in bulk by removing or replacing text in their names. The script also includes an option to scan for files with double extensions and rename them accordingly.

## Requirements
   
   * Python 3.x
   * Tested on Windows operating system

## Installation

  Clone the repository to your local machine:
    
      git clone https://github.com/sam-minns/rename-files.git

  Navigate to the cloned directory:

      cd file-renaming-script

   Run the script:

      python file_renaming_script.py

## Usage

   Upon running the script, you will be prompted to enter the full directory path where the files are located.

   You will then be prompted to choose from the following options:
       
       Option 1: Scan for files with double extensions and rename them accordingly
       Option 2: Mass rename files by removing or replacing text in their names
       Option 3: Quit the script

## Option 1: Scan for Files with Double Extensions

If you choose option 1, the script will scan the directory and its subdirectories for files with double extensions (e.g., .pdf.pdf or .xlsx.xlsx). If any files with double extensions are found, the script will prompt you to rename them.

## Option 2: Mass Rename Files

If you choose option 2, the script will prompt you to enter the text that you want to remove from the file names and the text that you want to replace it with.

The script will then scan the directory and its subdirectories for files that match the text you want to remove and replace the text in their names. For example, if you want to remove "old" from all file names and replace it with "new", the script will rename "file_old.txt" to "file_new.txt".

## Option 3: Quit the Script

If you choose option 3, the script will exit.
License

This project is licensed under the MIT License - see the LICENSE.md file for details.
