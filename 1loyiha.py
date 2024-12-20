# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 22:56:27 2024

@author: Shahzod
#1-loyiha oddiy kalkulator
"""

son1=int(input("Birinchi sonni kiriting: "))
print("Amallar =:>  * + - / ildiz daraja % ")
amal=input("Ishorani kiriting: ")
son2=int(input("Ikkinchi sonni kiriting: "))
if amal=="*":
    print(son1*son2)
elif amal=="+":
    print(son1+son2)
elif amal=="/":
    print(son1/son2)
elif amal=="ildiz":
    print(f"1-son={pow(son1,1/2)} va 2-son={pow(son2,1/2)}")
elif amal=="daraja":
    a=int(input("Nechanchi daraja? "))
    print(f"1-{pow(son1,a)} va 2-{pow(son2,a)}")
elif amal=="%":
    print(son1%son2)
else:
    print("Bunday amal yo'q")



