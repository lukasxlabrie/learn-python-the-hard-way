# tells the script to use command-line arguments
from sys import argv

# checks if a file exists on the filesystem
from os.path import exists

# defines argv as the script name, the source file, and the destination file
script, from_file, to_file = argv

# opens file and stores contents into a var
in_file = open(from_file)
indata = in_file.read()

# prints the names of the source and destination files, length in bytes, checks for output file, and prompts user to cancel or continue
print(f"""
Copying from {from_file} to {to_file}...
The input file is {len(indata)} bytes long...
Does the output file exist? {exists(to_file)}...
Ready, hit RETURN to continue, CTRL-C to abort.
""")
input()

# opens the destination file in write mode, writes the data, closes and saves
out_file = open(to_file, 'w')
out_file.write(indata)
out_file.close()
in_file.close()