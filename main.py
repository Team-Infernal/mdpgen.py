# Authors: Git-Rigoras & INF-Zenyth
# Description: Une idée qui nous est passé par la tête qu'on va essayer de déveloper (plusieurs langages?)
import json
import string
import sys
import secrets
from termcolor import colored


class MDPGen:

    def __init__(self):
        self.__config = self.__getConfig()
        self.__version = self.__config["version"]
        self.__authors = self.__config["authors"]
        self.__lettersLower = list(string.ascii_lowercase)
        self.__lettersUpper = list(string.ascii_uppercase)
        self.__numbers = [str(number) for number in range(0, 10)]
        self.__specialCharacters = ["!", "@", "#", "$", "%", "^", "&", "*"]

    def __getConfig(self):
        with open("config.json", "r") as configFile:
            return json.load(configFile)

    def addProfile(self):
        name = input("Profile name: ")
        length = int(input("Password length: "))
        print("Supported characters:\n\tLowercase Letters (1)\n\tUppercase Letters (2)\n\tNumbers (3)\n\tSpecial Characters (4)")

        charsUnformatted = input(
            "Password characters (seperate types with ','): ")
        chars = [mode.strip() for mode in charsUnformatted.split(",")]

        for i in range(len(chars)):
            if chars[i] != "1" and chars[i] != "2" and chars[i] != "3" and chars[i] != "4":
                return print("Invalid input for character set. (Use 1, 2, 3 and/or 4)")

        data = {
            "name": name,
            "length": length,
            "chars": chars,
        }

        with open("config.json", "r+") as configFile:
            configFileData = json.load(configFile)
            configFileData["profiles"].append(data)
            configFile.seek(0)
            json.dump(configFileData, configFile, indent=4)
            print(f"Successfully added profile {colored(name, 'blue')}!")

    def showProfiles(self):
        configFileData = self.__getConfig()
        for profile in configFileData["profiles"]:
            pName = str(profile["name"])
            pLength = str(profile["length"])
            charsList = list(profile["chars"])
            pCharsList = []

            for i in range(len(charsList)):
                if int(charsList[i]) == 1:
                    pCharsList.append("Lowercase")
                elif int(charsList[i]) == 2:
                    pCharsList.append("Uppercase")
                elif int(charsList[i]) == 3:
                    pCharsList.append("Numbers")
                elif int(charsList[i]) == 4:
                    pCharsList.append("Special")

            pChars = ", ".join(pCharsList)
            print(
                f"Name: {colored(pName, 'blue')}\n > Length: {colored(pLength, 'cyan')} characters\n > Character Set: {colored(pChars, 'cyan')}\n")

    def deleteProfile(self):
        print("Available Profiles:")
        self.showProfiles()
        name = input("Profile to delete (enter name): ")
        configFileData = self.__getConfig()
        profiles = configFileData["profiles"]

        for i in range(len(profiles)):
            if profiles[i]["name"] == name:
                profiles.pop(i)
                print(f"Successfully deleted profile {colored(name, 'blue')}!")
                break
            return print("Couldn't find that profile.")

        with open("config.json", "w") as configFile:
            configFileData = json.dump(configFileData, configFile, indent=4)

    def generatePassword(self, profile):
        configFileData = self.__getConfig()
        profiles = configFileData["profiles"]
        foundProfile = None

        for i in range(len(profiles)):
            if profiles[i]["name"] == profile:
                foundProfile = profiles[i]
                break

        if not foundProfile:
            return print("Couldn't find that profile.")

        print(
            f"Generating password using the {colored(foundProfile['name'], 'blue')} profile...")

        password = ""

        for i in range(foundProfile["length"]):
            charType = int(secrets.choice(foundProfile["chars"]))
            if charType == 1:
                password += secrets.choice(self.__lettersLower)
            elif charType == 2:
                password += secrets.choice(self.__lettersUpper)
            elif charType == 3:
                password += secrets.choice(self.__numbers)
            elif charType == 4:
                password += secrets.choice(self.__specialCharacters)

        print(colored(password, "blue"))

    @property
    def version(self):
        return self.__version

    @property
    def authors(self):
        return self.__authors

    @property
    def numbers(self):
        return self.__numbers

    @property
    def lettersLower(self):
        return self.__lettersLower

    @property
    def lettersUpper(self):
        return self.__lettersUpper

    @property
    def specialCharacters(self):
        return self.__specialCharacters


if __name__ == "__main__":

    app = MDPGen()
    print(f"\nMDPGen v{app.version}\n")

    if len(sys.argv) <= 1:
        print("""Available options:

        Create profile
            -cp
            --create-profile

        Delete profile
            -dp
            --delete-profile

        Show available profiles
            -sp
            --show-profiles

        Generate password using profile
            -g <name of profile>
            --generate <name of profile>
        """)

    else:
        if "-cp" in sys.argv or "--create-profile" in sys.argv:
            app.addProfile()
        if "-dp" in sys.argv or "--delete-profile" in sys.argv:
            app.deleteProfile()
        if "-sp" in sys.argv or "--show-profiles" in sys.argv:
            app.showProfiles()
        if "-g" in sys.argv or "--generate" in sys.argv:
            if len(sys.argv) <= 2:
                print("Missing profile name")
            elif sys.argv[2].startswith("-"):
                print("Can't start profile name with '-'.")
            else:
                profileName = []
                for i in range(2, len(sys.argv)):
                    profileName.append(sys.argv[i])
                app.generatePassword(" ".join(profileName))
