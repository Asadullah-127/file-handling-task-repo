# file_handling_tasks.py

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.
import csv

def create_sample_csv():
    #Creates a sample CSV file named 'data.csv' for Task 8.
    sample_data = [
        ["name", "age", "city"],
        ["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"],
        ["Charlie", 35, "Chicago"]
    ]
    with open("data.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sample_data)
    print("Sample CSV file 'data.csv' created!")

def task1_create_file():
   with open("OSSD.txt","w") as f:
        f.write("Hello World\n")

def task2_read_file():
   with open("OSSD.txt","r") as f:
       content = f.read()
       print(content)
def task3_append_file():
   with open("OSSD.txt","a") as f:
       f.write("This is an appended line in task 3.\n")
   

def task4_count_lines():
  
   with open("OSSD.txt","r") as f:
       lines = f.readlines()
       print(f"The file '{"OSSD.txt"}' has {len(lines)} lines.")

def task5_find_word():
    # TODO: Find whether a specific word exists in the file and how many times.
    word = "task"
    with open("OSSD.txt","r") as f:
        content = f.read()
        occ = content.lower().count(word.lower())
        if occ == 0:
            print(f"the word {word} does not exist in the file {"OSSD.txt"}.")
        else:
            print(f"The word '{word}' occured {occ} times in the file '{"OSSD.txt"}'.")


def task6_copy_file():
    # TODO: Copy the contents of one file to another.
    with open("OSSD.txt","r") as sf, open("OSSDcopy.txt","w") as df:
        for line in sf:
            df.write(line)
        print(f"Content copied from file {"OSSD.txt"} to file {"OSSDcopy.txt"} successfully.")

def task7_replace_word():
    # TODO: Replace a specific word in the file with another word.
    with open("OSSD.txt", "r") as f:
            content = f.read()
            new_content = content.replace("World", "Universe")
    with open("OSSD.txt", "w") as f:
        f.write(new_content)
        print(f"Replaced all occurrences of '{"World"}' with '{"Universe"}' in '{"OSSD.txt"}'.")

def task8_read_csv():
    # TODO: Read a CSV file and print each row.
    filename = "data.csv"
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        print(f"\nReading '{filename}':")
        for row in reader:
            print(row)

def task9_write_csv():
    # TODO: Write a list of dictionaries to a CSV file.
    data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"}
    ]
    filename = "output.csv"
    with open(filename, "w", newline='') as csvfile:
        fieldnames = ["name", "age", "city"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    print(f"\nData written to '{filename}'!")

def task10_json_file():
    # TODO: Create a JSON file from a Python dictionary and read it back.
    pass


