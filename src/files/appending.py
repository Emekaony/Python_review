

# def addNameToDatabase(name):
#     with open("fileDatabase.json", "r+") as db_file:
#         # convert the json string from a file into a python dictionary
#         # when parsing json files, use json.load()
#         # when parsing strings with json content, use json.loads()
#         myObj = json.load(db_file)
#         if name in myObj.keys():
#             message = input(f"{name} already exists in the database. Press y to append to the data ")
#             if message.upper() == "Y":
#                 data = input("Enter the data: ")
#                 # add the new string to the key in json file
#                 myObj["Emeka"].append({"data": data})
#                 db_file.seek(0)
                
#                 json.dump(myObj, db_file)
        
#         # dump the newly created json file back into the file
        

# o = addNameToDatabase("Emeka")

fileName = "tt.txt"

with open(fileName, mode="a") as file:
    # add newLine character so that stuff starts on a new line
    file.write("\nadded this to the file")
    file.writelines("\nthis too")
