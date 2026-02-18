print("The Cursed Antique Shop Part 1")
cursed_antiques = ["Talisman", "Monkeys Paw", "Cursed Mirror", "Haunted Painting", "Voodoo Doll", "Crystal Ball", "Cursed Ball", "Cursed Locket", "Ancient Amulet", "Phantom Clock ", "Dorian Gray's Portrait" , "Cursed Ring "]

# Part 1.1 add (do not remove this line)
cursed_antiques.append("Demon key ")
cursed_antiques.append("Horcrux")

# End Part 1.1 (do not remove this line)
print("After adding cursed antiques (part 1.1)") # (do not remove this line)
print(cursed_antiques) # (do not remove this line)


# part 1.2 sorting and removing (do not remove this line)
# YOUR CODE BELOW
cursed_antiques.sort()
cursed_antiques.pop(4)
cursed_antiques.pop(8)


# end part 1.2 (do not remove this line)

print("After sorting and removing (part 1.2)") # (do not remove this line)
print(cursed_antiques) # (do not remove this line)

print("All cursed antiques and their index in point form (part 1.3)") # (do not remove this line)

# part 1.3 using loops (do not remove this line)
# YOUR CODE BELOW
for idx, cursed in enumerate(cursed_antiques,1):
    print(f"{idx}: {cursed}")

# part 1.4 and 1.5 debugging below
cursed_antiques.remove("Shrunken Head")
cursed_antiques.pop(17)