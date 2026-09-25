#Marcus Ee
#file_extensions
#prompts the user for the name of a file and then outputs that file’s media type

def printFileType():
    print(f"image/{file.split(".")[1]}")

file = input("File name: ").casefold()
match file.split(".")[1]:
    case "png":
        printFileType()
    case "jpg":
        printFileType()
    case "gif":
        printFileType()
    case "jpeg":
        printFileType()
    case "pdf":
        printFileType()
    case "txt":
        printFileType()
    case "zip":
        printFileType()
    case _:
        print("Invalid file type")
    