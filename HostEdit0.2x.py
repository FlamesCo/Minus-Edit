## This is a host editor that eddits the whosts file
print("Would you like to edit the hosts file? (y/n)")
answer = input()
if answer == "y":
    def edit():
        print("What would you like to edit?")
        print("1. Add a host")
        print("2. Remove a host")
        print("3. Edit a host")
        print("4. Exit")
        choice = input()
        if choice == "1":
            print("What is the hostname?")
            hostname = input()
            print("What is the IP address?")
            ipaddress = input()
            print("What is the alias?")
            alias = input()
            with open("/etc/hosts", "a") as hosts:
                hosts.write(ipaddress + " " + alias + " " + hostname + "\n")
            print("Host added")
            edit()
        elif choice == "2":
            print("What is the hostname?")
            hostname = input()
            with open("/etc/hosts", "r") as hosts:
                lines = hosts.readlines()
            with open("/etc/hosts", "w") as hosts:
                for line in lines:
                    if hostname not in line:
                        hosts.write(line)
            print("Host removed")
            edit()
        elif choice == "3":
            print("What is the hostname?")
            hostname = input()
            with open("/etc/hosts", "r") as hosts:
                lines = hosts.readlines()
            with open("/etc/hosts", "w") as hosts:
                for line in lines:
                    if hostname in line:
                        print("What would you like to edit?")
                        print("1. IP address")
                        print("2. Alias")
                        print("3. Hostname")
                        choice = input()
                        if choice == "1":
                            print("What is the IP address?")
                            ipaddress = input()
                            hosts.write(ipaddress + " " + line[-1] + " " + line[-2] + "\n")
                            print("IP address changed")
                            edit()
                        elif choice == "2":
                            print("What is the alias?")
                            alias = input()
                            hosts.write(line[0] + " " + alias + " " + line[-1] + "\n")
                            print("Alias changed")