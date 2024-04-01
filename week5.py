try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("This is line 1.\n")
        file.write("12345\n")
        file.write("Another line with text and numbers: 67890\n")

    # File Reading and Display
    print("Contents of my_file.txt:")
    with open("my_file.txt", "r") as file:
        for line in file:
            print(line.strip())

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("This is an appended line.\n")
        file.write("54321\n")
        file.write("Another appended line: 09876\n")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied while accessing the file.")
except Exception as e:
    print("An error occurred:", e)

finally:
    print("End of file handling operations.")
