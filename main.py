from pojistenec import Pojistenec
import os


pojistenci = []

aplikace = True
while aplikace:
    print("------------------------------------")
    print("Evidence pojištěných")
    print("------------------------------------")
    print("Vyberte si akci:")
    print("1\tPřidat nového pojistného")
    print("2\tVypsat všechny pojistné")
    print("3\tVyhledat pojistného")
    print("4\tKonec")
    volba = int(input())
    zadavani = True
    if volba == 1:
        while zadavani:
            jmeno = input("Zadej jméno pojštěného: ")
            prijmeni = input("Zadej příjmení: ")
            telefon = int(input("Zadej telefonní číslo ve tvaru xxxxxxxxx: "))
            vek = int(input("Zadej vek: "))
            uzivatel = Pojistenec(jmeno, prijmeni, telefon, vek)
            pojistenci.append(uzivatel)
            volba = input("Další záznam? y/n ")
            nove_zadani = True
            while nove_zadani:
                if volba == "y" or volba == "Y":
                    zadavani = True
                    nove_zadani = False
                elif volba == "n" or volba == "N":
                    zadavani = False
                    nove_zadani = False
                else:
                    print("špatná volba")
                    nove_zadani = True
        input("Pokračujte stiskem libovolné klávesy...")
    if volba == 2:
        for i in pojistenci:
            print(i)
        input("Pokračujte stiskem libovolné klávesy...")
    if volba == 3:
        vyhledat = input("Zadej jméno/příjmení: ")
        vyhledat = vyhledat.upper().strip()
        hledani = [uzivatel for uzivatel in pojistenci if (uzivatel.hledat_jmeno == vyhledat or
                                                           uzivatel.hledat_prijmeni == vyhledat)]
        if len(hledani) == 0:
            print(f"{vyhledat.strip()} - pojištěný nenalezen!")
        else:
            for uzivatel in hledani:
                print(uzivatel)
        input("Pokračujte stiskem libovolné klávesy...")
    if volba == 4:
        aplikace = False
    os.system('cls')
input("Děkujeme za využití naší databáze. Pro ukončení stiskněte libovolné tlačítko...")
