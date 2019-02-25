#!/bin/python

try:
    wiek = int(input("podaj swoj wiek: "))
except ValueError:
    print("Wpisales tekst!")

if wiek > 18:
    print("Jestes dorosly")
elif wiek == 18:
    print("Masz dokladnie 18 lat")
else:
    print("Masz mniej niż 18")
