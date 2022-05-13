exampleText = "My name is Nnaemeka"

with open("tt.txt", "w") as f:
    f.write(exampleText);
    # do we have to close the file ?
    # I think the file closes this way
    f.close()
