# Authors: Git-Rigoras & INF-Zenyth
# Description: Une idée qui nous est passé par la tête qu'on va essayer de déveloper (plusieurs langages?)
import json
import string


class MDPGen:

    def __init__(self):
        self.__config = self.__getConfig()
        self.__version = self.__config["version"]
        self.__authors = self.__config["authors"]
        self.__lettersLower = list(string.ascii_lowercase)
        self.__lettersUpper = list(string.ascii_uppercase)
        self.__numbers = [str(number) for number in range(0, 10)]
        self.__specialCharacters = ["!", "@", "#", "$", "%", "^", "&", "*"]
        self.__defaultProfile = self.__config["default"]["profileID"]
        self.__selectedProfile = self.__config["profiles"][self.__defaultProfile]

    def __getConfig(self):
        with open("config.json", "r") as configFile:
            return json.load(configFile)

    def addProfile(self):
        name = input("Profile name: ")
        length = input("Password length: ")
        print("Supported characters:\n\tLowercase Letters (1)\n\tUppercase Letters (2)\n\tNumbers (3)\n\tSpecial Characters (4)")

        charsUnformatted = input(
            "Password characters (seperate types with ','): ")
        chars = [mode.strip() for mode in charsUnformatted.split(",")]

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
            print(f"Successfully added profile '{name}'!")

    def showProfiles(self):
        configFileData = self.__getConfig()
        for profile in configFileData["profiles"]:
            print(
                profile["name"] +
                " >>> Length: " + profile["length"] +
                " && Characters: " + str(profile["chars"])
            )

    def deleteProfile(self):
        print("Available Profiles:")
        self.showProfiles()
        name = input("Profile to delete (enter name): ")
        configFileData = self.__getConfig()
        profiles = configFileData["profiles"]

        for i in range(len(profiles)):
            if profiles[i]["name"] == name:
                profiles.pop(i)
                print(f"Successfully deleted profile '{name}'!")
                break

        with open("config.json", "w") as configFile:
            configFileData = json.dump(configFileData, configFile, indent=4)

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


def main():

    app = MDPGen()
    print(f"\nMDPGen v{app.version}\n")
    app.addProfile()
    app.deleteProfile()


if __name__ == "__main__":
    main()
