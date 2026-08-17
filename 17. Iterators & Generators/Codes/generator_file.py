# ============================================================
# GENERATOR EXAMPLE 2: READING A FILE
# ============================================================

def read_file(file_path):

    with open(file_path) as file:

        for line in file:

            # yield gives one cleaned line at a time.
            yield line.strip()


# File path
filepath = "random.txt"


# The generator provides one line at a time.
for line in read_file(filepath):
    print(line)


# ============================================================
# WHY USE A GENERATOR HERE?
# ============================================================

# A large file does not need to be loaded completely
# into memory at once.
#
# The generator reads and provides one line at a time.
#
# This makes generators useful for processing large files
# and large amounts of data.