import csv

def read_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def write_csv(file_path, data):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def add_status_column(data):
    # Add the new column to the header
    header = data[0]
    header.append('Status')

    # Add the default value "Pending" to each row
    for row in data[1:]:
        row.append('Pending')
    
def main():
    input_file = 'security_incidents.csv'  # Input CSV file path
    output_file = 'security_incidents_modified.csv'  # Output CSV file path

    # Read the CSV file
    data = read_csv(input_file)

    # Add the new column "Status" with default value "Pending"
    add_status_column(data)

    # Write the modified data to the new CSV file
    write_csv(output_file, data)

if __name__ == "__main__":
    main()
