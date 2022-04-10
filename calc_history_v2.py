# Get data from user and store it in a list
# then display the most recent three entries nicely

# Set up empty list
all_calcs = []

# Get five items of data
get_item = ""
while get_item != "xxx":
    get_item = input("Enter an item: ")

    if get_item == "xxx":
        break

    all_calcs.append(get_item)

print()

if len(all_calcs) == 0:
    print("Oops - the list is empty")

else:

    # Show that everything made it to the list...
    print()
    print("*** The Full List ***")
    print(all_calcs)

    # print items starting at the END of the list
    if len(all_calcs) >= 3:
        print("*** Most Recent 3 ***")
        for item in range(0,3):
            print(all_calcs[len(all_calcs) - item - 1])

    else:
        print("*** Items from Newest to Oldest ***")
        for item in range(len(all_calcs)):
            print(all_calcs[len(all_calcs) - item - 1])
