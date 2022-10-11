""" 
BIBLIOTECA PHONENUMBERS: fornece vários recursos, como informações básicas de um número de telefone, 
validação de um número de telefone, etc...
"""
import phonenumbers
from phonenumbers import geocoder

phone = input("Digite o telefone no formato +551140028922: ")

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, "pt"))
