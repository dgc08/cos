import os
def shell(exit_after=-1):
    while exit_after != 0:
        command = input("cShell on '" + os.environ["USERNAME"] +"' || " + os.getcwd()+"> $ ")
        if command == "cex":
            return
        elif command == "help":
            print("For bash-help type 'help sys'. For cShell help type 'help c'.")
        elif command.startswith("pycom"):
            com = command.replace("pycom ", "")
            exec(com)
        elif command == "help sys":
            os.system("help")
        elif command.startswith("cd "):
            com = command.replace("cd ", "")
            os.chdir(com)
        elif command.startswith("ls"):
            os.system("dir")
        elif command == "help c":
            print("cShell help:\n"
                  "| pycom [command]:    executes a one-line python command.\n"
                  "| help:               Displays the help.\n"
                  "| cex:                exit cShell and return to the Python Shell or Python script.\n")
        else:
            os.system(command)
        exit_after -= 1


if __name__ == "__main__":
    shell()