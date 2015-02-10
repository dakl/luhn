#!/usr/bin/env python

# Luhn's algo doesn't change digit certain transpositions
# 90 <-> 09
# 22 <-> 55
# 33 <-> 66
# 44 <-> 77
# based on http://en.wikipedia.org/wiki/Luhn_algorithm#Strengths_and_weaknesses
REJECTED_STRS = ["09", "90", "22", "55", "33", "66", "44", "77"]

def padToQuad(num):
	while len(str(num)) < 4:
		num = "0" + str(num)
	return str(num)


# implementation of standard Luhn mod 10 from 
# http://en.wikipedia.org/wiki/Luhn_algorithm#Implementation_of_standard_Mod_10
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10
 
def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0
 
def calculate_luhn(partial_card_number):
    check_digit = luhn_checksum(int(partial_card_number) * 10)
    return check_digit if check_digit == 0 else 10 - check_digit       
    
for i in range(1,10000):
    id = padToQuad(i)
    if not any(REJECTED_STR in id for REJECTED_STR in REJECTED_STRS):
		idWithControl = id + "" + str(calculate_luhn(id))
		if is_luhn_valid(idWithControl):
			print idWithControl

