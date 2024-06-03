class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

email_min_len = 5
valid_domains = ["com", "bg", "org", "net"]

while True:
    given_email = input()
    if given_email == "End":
        break

    if "@" not in given_email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(given_email.split("@")[0]) < email_min_len:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = given_email.split(".")[-1]

    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

