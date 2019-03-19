"""Joshua Bond"""


def main():
    MIN_LENGTH = 4
    password = input("Enter your password:: ")
    while len(password) < MIN_LENGTH:
        password = input("Your password must be {} longer::".format(MIN_LENGTH - len(password)))
    censored = ""
    for i in range(len(password)):
        censored += "*"

    print(censored)
main()