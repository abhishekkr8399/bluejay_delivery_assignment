Bluejay Delivery Assignment
This is a software development internship short assignment for Bluejay Delivery. The goal of this project is to write a program that analyzes a spreadsheet file containing employee timecard data and prints the names and positions of employees who meet certain criteria.

Requirements
Python 3.8 or higher
pandas library
openpyxl library

Installation
To install the required libraries, run the following command in your terminal:

Python

pip install pandas openpyxl

Usage
To run the program, download the spreadsheet file from this link:

Assignment_Timecard.xlsx

Then, run the following command in your terminal, replacing path with the location of the spreadsheet file on your computer:

Python

python main.py path

For example, if the spreadsheet file is in the same folder as the main.py file, you can run:

Python

python main.py Assignment_Timecard.xlsx
The program will print the name and position of employees who:

have worked for 7 consecutive days
have less than 10 hours between shifts but greater than 1 hour
have worked for more than 14 hours in a single shift
The output will be saved as output.txt in the same folder as the main.py file.
