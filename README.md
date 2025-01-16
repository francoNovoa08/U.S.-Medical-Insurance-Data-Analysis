# Insurance Data Analysis Tool

## Overview
The Insurance Data Analysis Tool is a Python program designed to analyse health insurance data from a CSV file on U.S. Medical Insurance. It computes statistical metrics such as mean, median, and standard deviation for various attributes like age, BMI, number of children, insurance charges, and more. Additionally, it provides insights into demographic distributions such as gender, smoking habits, and regional representation.

## Features
- **Age Analysis**: Calculates mean, median, and standard deviation.
- **BMI Analysis**: Provides mean, median, and standard deviation.
- **Children Analysis**: Analyses the mean, median, and standard deviation of the number of children.
- **Insurance Charges Analysis**: Computes mean, median, and standard deviation of insurance charges.
- **Gender Analysis**: Counts and computes the percentage of males and females.
- **Smoker Analysis**: Provides counts and percentages of smokers and non-smokers.
- **Region Analysis**: Counts and calculates the percentage of individuals from different regions.

## Requirements
- Python 3
- A CSV file named `insurance.csv` with the following structure:
age, sex, bmi, children, smoker, region, charges
### Example CSV:
age, sex, bmi, children, smoker, region, charges
19, female, 27.9, 3, no, southwest, 16884.924


## Installation
1. Clone this repository or download the Python file.
2. Ensure you have Python installed on your system.
3. Place the `insurance.csv` file in the same directory as the script.

## Usage
1. Open a terminal or command prompt.
2. Run the script using the following command:
 ```bash
 python main.py
```

The program will read the file and output the analysis to the console. Functionality is stored within a class; function calls can be removed for unwanted data.
Error Handling
If the insurance.csv file is missing, the program will display:
 ```bash
The file 'insurance.csv' was not found
```
If the CSV file has invalid or missing data, an appropriate error message will be displayed.
