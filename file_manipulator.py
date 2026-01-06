import sys

if len(sys.argv)<2:
    print("Error: command is required")
    sys.exit(1)

command = sys.argv[1]

if command == "reverse":
    if len(sys.argv) != 4:
        print("Usage: reverse inputpath outputpath")
        sys.exit(1)

    input_path = sys.argv[2]
    output_path = sys.argv[3]

    with open(input_path, "r") as f:
        contents = f.read()

    with open(output_path, "w") as f:
        f.write(contents[::-1])

elif command == "copy":
    if len(sys.argv) != 4:
        print("Usage: copy inputpath outputpath")
        sys.exit(1)
    
    input_path = sys.argv[2]
    output_path = sys.argv[3]

    with open(input_path, "r") as f:
        contents = f.read()

    with open(output_path, "w") as f:
        f.write(contents)

elif command == "duplicate-contents":
    if len(sys.argv) != 4:
        print("Usage: duplicate-contents inputpath n")
        sys.exit(1)
    
    input_path = sys.argv[2]
    n = int(sys.argv[3])

    with open(input_path, "r") as f:
        contents = f.read()
    with open(input_path, "w") as f:
        f.write(contents * n)

elif  command == "replace-string":
    if len(sys.argv) != 5:
        print("Usage: replace-string inputpath needle newstring")
        sys.exit(1)

    input_path = sys.argv[2]
    needle = sys.argv[3]
    newstring = sys.argv[4]

    with open(input_path, "r") as f:
        contents = f.read()

    contents = contents.replace(needle,newstring)

    with open(input_path, "w") as f:
        f.write(contents)

else:
    print("unknown command")