import os
import time
# Now the dir becomes
# if not os.path.exists("Big data"):
#     os.mkdir("Big data")

# if i want that to make the 100 folder in the big data

# for i in range(0,100):
#     os.mkdir(f"Big data/day{i+1}")

#     Now if i want to rename all the folders then i can use the
# os.rename(src,des)

# for i in range(0,100):
#     os.rename(f"Big data/day{i+1}", f"Tutorial {i+1}")

# to check the list of the directories i can use the os.listdir
# if not os.path.exists("data"):
#     os.mkdir("data")
#
# for i in range(0,20):
#     os.mkdir(f"data/day {i+1}")


# if os.path.exists("data"):
#     folders = os.listdir("data")
#     print(folders)
#     for i in folders:
#         print(i)
# else:
#     print("No folders")

for i in range(0,20):
    file_path = f"data/day {i+1}"

    try:
        os.rmdir(file_path)
        print(f"File {file_path} removed successfully!")
    except Exception as e:
        print(f"Error removing file {file_path} : {e}")

