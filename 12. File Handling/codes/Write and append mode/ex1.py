file_name = input("Enter your file name: ")
with open(f"{file_name}.txt", "w") as f:
    while True:
        text = input("Write something or use q to quit: ")
        if text == "q" or text == "Q":
            break
        else:
            f.write(text + "\n")
