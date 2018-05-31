import os
import sys
import time


def main(root, name=False, customize=False):
    # Rename to specified filename if so desired
    if name and customize:
        print("Please only use one optional argument.")
        return

    if name:
        yes = True

        print("\n*RENAMING FILES TO {}. USE ON ONLY ONE FOLDER.*".format(name))

        while (yes):
            answer = input("CONTINUE? y/n: ")
            if answer == 'n':
                print("Quitting.")
                return
            if answer == 'y':
                yes = False
                continue
            else:
                continue

    if customize:
        yes = True

        print("\nCustomize will allow you to set a custom filename" +
              " for each subfolder when they are encountered.")

        while (yes):
            answer = input("Continue? y/n: ")
            if answer == 'n':
                print("Quitting.")
                return
            if answer == 'y':
                yes = False
                continue
            else:
                continue

    # Types of files to rename
    extensions = ['png', 'jpeg', 'jpg', 'gif', 'webm']

    # Actual traversals and renaming happens here
    start_time = time.time()
    j = 0

    for dirName, subdirList, fileList in os.walk(root):
        print('Found directory: %s' % dirName)

        temp = dirName.split("\\")[-1]

        if customize:
            yes = True
            while (yes):
                answer = input("\tCustomize folder {}? y/n: ".format(temp))
                if answer == 'n':
                    print("\tContinuing.")
                    yes = False
                    continue
                if answer == 'y':
                    temp = input("\tGive a filename: ")
                    print("\tContinuing with filename {}.".format(temp))
                    yes = False
                    continue
                else:
                    continue

        if name:
            temp = name

        i = 1

        for fname in fileList:
            f_split = fname.split('.')
            # Check for file extension to not rename dangerous shit
            if f_split[-1] not in extensions:
                print("\tSorry, not going to rename that.")
                i += 1
                continue

            oldname = '%s\\%s' % (dirName, fname)
            newname = '%s\\%s_%02d%s%s' % (dirName, temp, i, ".", f_split[-1])

            print('\t%s' % fname + " is being renamed to {}.".format(
                '%s_%02d%s%s' % (temp, i, ".", f_split[-1])))

            try:
                os.rename(oldname, newname)
                j += 1
            except FileExistsError:
                print("Could not rename {}: already exists.".format(oldname))
            except PermissionError:
                print("Could not rename {}: no permissions.".format(oldname))

            i += 1

        print("\n")
    end_time = time.time()

    # Interesting stats!
    if j > 0:
        print("Total time elapsed was: \t %.2f seconds" %
              (end_time - start_time))
        print("Number of files renamed:\t {}".format(j))
    else:
        print("Didn't find anything? Probably an incorrect path.")


# Hi I run the program
if __name__ == "__main__":
    helpmsg = "\nUsage:\n\t" + "python rename.py \"C:\\path\\to\\folder\"" + \
        " (optional arguments \"filename\" and \"customize\" also supported)"

    argc = len(sys.argv)

    if argc == 1:
        print(helpmsg)
        quit(1)
    if argc >= 2:
        arg1 = sys.argv[1]
    if argc >= 3:
        arg2 = sys.argv[2]

    # Check for actual filepath before trying
    try:
        if argc < 3:
            if arg1 == "help":
                print(helpmsg)
                quit(0)
            else:
                if os.path.isabs(arg1):
                    main(arg1)
                else:
                    print("helpmsg")
        elif argc < 4:
            if (arg2 == "customize"):
                main(arg1, name=False, customize=arg2)
            else:
                main(arg1, name=arg2)
        else:
            print(helpmsg)
            quit(1)
    except IndexError:
        print(helpmsg)
        quit(1)
