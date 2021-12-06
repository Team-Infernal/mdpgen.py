# Authors: Git-Rigoras & INF-Zenyth
# Description: Une idée qui nous est passé par la tête qu'on va essayer de déveloper (plusieurs langages?)
import json
import string


class MDPGen:

    def __init__(self):
        __config = self.__getConfig()
        self.__version = __config["version"]
        self.__authors = __config["authors"]
        self.__lettersLower = list(string.ascii_lowercase)
        self.__lettersUpper = list(string.ascii_uppercase)
        self.__numbers = [str(element) for element in range(0, 10)]
        self.__specialCharacters = ["!", "@", "#", "$", "%", "^", "&", "*"]

    def __getConfig(self):
        with open("config.json", "r") as configFile:
            return json.load(configFile)

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
    print(
        f"MDPGen v{app.version} developed by {app.authors[0]['name']} & {app.authors[1]['name']}")
    print(app.numbers)
    print(app.lettersLower)
    print(app.lettersUpper)
    print(app.specialCharacters)


if __name__ == "__main__":
    main()
