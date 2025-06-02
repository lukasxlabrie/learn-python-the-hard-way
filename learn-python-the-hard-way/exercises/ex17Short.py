# tells the script to use command-line arguments
from sys import argv

# checks if a file exists on the filesystem
from os.path import exists

# defines argv as the script name, the source file, and the destination file
script, from_file, to_file = argv

# prints the names of the source and destination files
print(f"Copying from {from_file} to {to_file}")

# opens the source file and reads its contents into a variable
in_file = open(from_file)
indata = in_file.read()

# prints the size of the input file in bytes
print(f"The input file is {len(indata)} bytes long")

# checks and prints whether the output file already exists
print(f"Does the output file exist? {exists(to_file)}")

# tells the user how to proceed or cancel
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# opens the destination file in write mode and writes the data
out_file = open(to_file, 'w')
out_file.write(indata)

# confirms completion
print("Alright, all done.")

# closes both files to save changes and free resources
out_file.close()
in_file.close()