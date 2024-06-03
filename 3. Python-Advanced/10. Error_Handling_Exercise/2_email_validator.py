class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

given_email = input()

while given_email != "End":
    if "@" not in given_email:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        name, domain = given_email.split("@")
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if ".com" not in domain and ".bg" not in domain and ".org" not in domain and ".net" not in domain:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
    given_email = input()
