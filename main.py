# Import pandas library for data manipulation
import pandas as pd

# Import tabulate library for table formatting
from tabulate import tabulate

# Read the input file
file = input("Enter the file path: ")
df = pd.read_excel(file)

# Calculate shift duration
df["Shift Hours"] = (df["Time Out"] - df["Time"]).dt.total_seconds() / 3600

# Define helper functions
def check_consecutive_days(group):
    dates = group["Time"].dt.date.unique()
    count = 0
    flag = False
    for i in range(len(dates) - 1):
        if dates[i + 1] == dates[i] + pd.Timedelta(days=1):
            count += 1
        else:
            count = 0
        if count == 6:
            flag = True
            break
    return flag

def check_between_shifts(group):
    start_times = group["Time"]
    end_times = group["Time Out"]
    flag = False
    for i in range(len(start_times) - 1):
        time_diff = start_times.iloc[i + 1] - end_times.iloc[i]
        if pd.Timedelta(hours=1) < time_diff < pd.Timedelta(hours=10):
            flag = True
            break
    return flag

def check_long_shift(group):
    return (group["Shift Hours"] > 14).any()

# Group the dataframe and apply checks
grouped = df.groupby(["Position ID", "Employee Name"])
results = grouped.apply(lambda x: pd.Series({
    "Worked 7 consecutive days": check_consecutive_days(x),
    "Less than 10 hours between shifts": check_between_shifts(x),
    "Worked more than 14 hours in a single shift": check_long_shift(x)
}))

# Ask the user to enter the option
option = input("Enter the option to get the employees who have: \n a) worked for 7 consecutive days \n b) less than 10 hours of time between shifts but greater than 1 hour \n c) worked more than 14 hours in a single shift \n")

# Validate the option
if option not in ["a", "b", "c"]:
    print("Invalid option. Please enter a, b, or c.")
else:
    # Filter the results based on the option
    if option == "a":
        filtered = results[results["Worked 7 consecutive days"]]
    elif option == "b":
        filtered = results[results["Less than 10 hours between shifts"]]
    elif option == "c":
        filtered = results[results["Worked more than 14 hours in a single shift"]]

    # Convert the filtered dataframe to a tabular format
    table = tabulate(filtered.index.to_frame()[["Position ID", "Employee Name"]], headers="keys", tablefmt="psql")

    # Print the table
    print(table)
