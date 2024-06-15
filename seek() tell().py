
with open('Writing.txt','r') as f:
    # Taken the data to the given numbered byte
    f.seek(10)
    # now it will read the data from the 10th byte
    data = f.read()

print(data)

# This will print the data in from the writing.txt

