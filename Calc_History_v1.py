# Get data from user and store it in a list, then display the most recent three entries nicely

# Set up empty list
all_calcs = []

# Get five items of data
for item in range(0, 5):
    get_item = input("Enter an item: ")
    all_calcs.append(get_item)

# Show that everything made it to the list...
print()
print("*** The Full List ***")
print(all_calcs)

print()

print("*** Most Recent 3 ***")
# Print items starting at the end of the list
for item in range(0, 3):
    print(all_calcs[len(all_calcs) - item - 1])
