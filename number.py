def divide_numbers():
    try:
        num1 = float(input("Ievadiet pirmo skaitli: "))
        num2 = float(input("Ievadiet pirmo skaitli: "))
        result = num1 / num2
        print(f"Rezultāts: {result}")

    except ZeroDivisionError:
        print("Kļūda: Dalīšana ar nulli nav atļauta. ")

    except ValueError:
        print("Kļūda: Lūdzu, ievadiet darīgus skaitļus. ")

    except Exception as e:
        print(f"Radās neparedzēta kļūda: {e}")

    finally:
        # Šis bloks vienmēr izpildās, neakarīgi no kļūdām
        print("Darbība pabeigta.")

# Izsaucam funkcija
divide_numbers()


