# Display output using int / float

to_round = [1/1, 1/2, 1/3]
print("**** Numbers to round ****")
print(to_round)

print()
print("**** Rounded Numbers ****")

for item in to_round:
    if item%1 == 0:
        rounded = "{:.0f}".format(item)
    else:
        rounded = "{:.1f}".format(item)
