
# Define the filename
file_name = "status_report.txt"

# Create and write to the file
try:
    with open(file_name, "w") as file:
        file.write("Program has been run")
    print(f"Success! '{file_name}' has been created.")
except Exception as e:
    print(f"An error occured: {e}")

