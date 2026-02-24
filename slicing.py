# Slicing guide -> list[start:stop:step]

# Variable
names = ["polar", "pixie", "leon", "nikka"]

# ==================================================

# 1. start only (Start at index 1, go to the end.)
names[1:]

# OUTPUT
# ["pixie", "leon", "nikka"]

# ==================================================

#2. stop only (Start at 0, stop before index 2.)
names[:2]

# OUTPUT
# ["polar", "pixie"]

# ==================================================

#3. step only (Start at 0 (default), go to end (default), move forward by 2 each time.)
names[::2]

# OUTPUT
# ["polar", "leon"]

# ==================================================

#4. start and stop
names[1:3]

# OUTPUT
# ["pixie", "leon"]

# ==================================================

#5. start and step
names[1::2]

# OUTPUT
# ["pixie", "nikka"]

# ==================================================

#6. stop and step
names[:3:2]

# OUTPUT
# ["polar", "leon"]

# ==================================================

#7. start, stop and step
names[0:4:2]

# OUTPUT
# ["polar", "leon"]

# ==================================================

#8. reverse negative (Take everything, but walk backwards.)
names[::-1]

# OUTPUT
# ["nikka", "leon", "pixie", "polar"]
