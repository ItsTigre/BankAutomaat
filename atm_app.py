from bankautomaat import bankaccount

accounts = [
    bankaccount("42069420", "2771", "Raul Mendez", 100),
    bankaccount("12345678", "1234", "Sophie De Jong", 500),
    bankaccount("87654321", "5678", "Pieter Janssen", 250),
]


def login():
    print("Welkom bij de bankautomaat!")
    for _ in range(3):
        account_id = input("Voer uw rekeningnummer in: ")
        account = next((acc for acc in accounts if acc.account_id == account_id), None)
        if account:
            for _ in range(3):
                pin = input("Voer uw pincode in: ")
                if pin == account.pin_code:
                    print(f"Welkom, {account.holder_name}!")
                    return account
                else:
                    print("Ongeldige pincode. Probeer opnieuw.")
            print("Te veel mislukte pogingen. De applicatie wordt afgesloten.")
            return None
        else:
            print("Rekening niet gevonden. Probeer opnieuw.")
    print("Te veel mislukte pogingen. De applicatie wordt afgesloten.")
    return None


def atm_menu(account):
    while True:
        print("******************************")
        print("**      Bankautomaat        **")
        print("******************************")
        print(f"**   Jouw Saldo: €{account.balance:.2f}    **")
        print("******************************")
        print("** 1) Geld Afhalen          **")
        print("** 2) Geld Storten          **")
        print("** 3) Verlaten              **")
        print("******************************")

        try:
            option = int(input("Selecteer een optie (1-3): "))
        except ValueError:
            print("Alsjeblieft, een nummer tussen 1 en 3 invoeren.")
            continue

        if option == 1:
            try:
                amount = float(input("Hoeveel wilt u afhalen (EUR): "))
                account.withdraw(amount)
            except ValueError:
                print("Ongeldige hoeveelheid, voer een geldig nummer in.")

        elif option == 2:
            try:
                amount = float(input("Hoeveel wilt u storten (EUR): "))
                account.deposit(amount)
            except ValueError:
                print("Ongeldige hoeveelheid, voer een geldig nummer in.")

        elif option == 3:
            print("Dankjewel voor het gebruik van onze bankautomaat. Fijne dag verder!")
            break

        else:
            print("Ongeldige optie. Kies een nummer tussen 1 en 3.")


def main():
    account = login()
    if account:
        atm_menu(account)


if __name__ == "__main__":
    main()
