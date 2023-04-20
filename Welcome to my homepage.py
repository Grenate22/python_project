print("Welcome to my homepage")
lang = input("Your language? ")
name = input("Your name? ")


def lan():
    if lang.title() == "Yoruba":
        return "Kaabo"
    if lang.lower() == "igbo":
        return "ndewo"
    if lang.lower() == "hausa":
        return "barka da zuwa"


print(lan(), name)
