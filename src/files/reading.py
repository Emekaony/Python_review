filename = "tt.txt"

# with open(filename, "r") as f:
#     data = f.read()
#     print(data.split("\n"))

with open(filename, "r") as f:
    # reading line by line
    # for line in f.readlines():
    #     print(line)
    
    print(f.readlines())