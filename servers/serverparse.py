filepath= "" # "~/mycode/servers/"


def resetOutputFiles():
    with open(filepath + "org.txt", "w") as txtfile:
        txtfile.write("")
    with open("com.txt", "w") as txtfile:
        txtfile.write("")

def processFile():
    with open(filepath + "servers.txt") as servers:
        with open(filepath + "com.txt", "a") as com:
            with open(filepath + "org.txt", "a") as org:
                for line in servers:
                    splitline = line.split(".")
                    if splitline[-1] == "com\n":
                        com.write(line)
                        continue
                    if splitline[-1] == "org\n":
                        org.write(line)
                        continue

resetOutputFiles()
processFile()