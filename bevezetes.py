def auto():
    print("I/A:")
    auto_neve: str= str(input(f"\tAutó neve: "))
    auto_gyartaasieve: int= int(input(f"\tGyártási dátum: "))
    print("I/B:")
    if auto_gyartaasieve == 2024:
        print(f"\tEz az {auto_neve} friss gyártás.")
    elif auto_gyartaasieve < 2000:
        print(f"\tEz az {auto_neve} öreg autó.")
    else:
        print(f"\tEz az {auto_neve} átlagos korú.")
    