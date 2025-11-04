uer_input = input("Input a color among red, yellow, or green: ")
color = uer_input.lower()


if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready to go")
elif color == "green":
    print("Go")
else:
    print("Invalid color")

