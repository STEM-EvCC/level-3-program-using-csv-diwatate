import csv

def process_security_incidents(input_file, output_file):
    # Read the CSV file and store the data in a list
    with open(input_file, 'r', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    # Add a new column named Status with a default value of "Pending" for all rows
    for row in data:
        row.append("Pending")

    # Save the modified data to a new CSV file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
if __name__ == "__main__":
    input_file = "security_incidents.csv"
    output_file = "security_incidents_modified.csv"
    process_security_incidents(input_file, output_file)
    print("Processing complete. Modified data saved to", output_file)
