from misc_functions import *
import base64

"""
Finds the private key given the public key and modulo when their values are small
"""
def wienerAttack(N, e):
    conv = convergents(continued_fraction(e, N))
    length = len(conv)
    for i in range(length):
        denominator = conv[i].denominator
        if congruent(pow(pow(2, e, N), denominator, N), 2, N):
            return denominator

"""
Decodes the base64 message into a string
Returns a list with the RSA encrypted numbers found in the decoded string

cipher : The encoded message string
"""
def decode(cipher):
    base64_bytes = cipher.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    
    number_string = message[3:len(message)-1]
    encoded_lines = number_string.splitlines()
    encoded_numbers = []
    for line in encoded_lines:
        split_string = line.split(",")
        for n in split_string:
            encoded_numbers.append(n)
    return encoded_numbers


if __name__ == "__main__":
    (N, e) = (194749497518847283, 50736902528669041)
    cipher = "Qz1bNDc0MDYyNjMxOTI2OTM1MDksNTEwNjUxNzgyMDExNzIyMjMsMzAyNjA1NjUyMzUxMjg3MDQsODIzODU5NjMzMzQ0MDQyNjgNCjgxNjkxNTY2NjM5Mjc5MjksNDc0MDYyNjMxOTI2OTM1MDksMTc4Mjc1OTc3MzM2Njk2NDQyLDEzNDQzNDI5NTg5NDgwMzgwNg0KMTEyMTExNTcxODM1NTEyMzA3LDExOTM5MTE1MTc2MTA1MDg4MiwzMDI2MDU2NTIzNTEyODcwNCw4MjM4NTk2MzMzNDQwNDI2OA0KMTM0NDM0Mjk1ODk0ODAzODA2LDQ3NDA2MjYzMTkyNjkzNTA5LDQ1ODE1MzIwOTcyNTYwMjAyLDE3NDYzMjIyOTMxMjA0MTI0OA0KMzAyNjA1NjUyMzUxMjg3MDQsNDc0MDYyNjMxOTI2OTM1MDksMTE5MzkxMTUxNzYxMDUwODgyLDU3MjA4MDc3NzY2NTg1MzA2DQoxMzQ0MzQyOTU4OTQ4MDM4MDYsNDc0MDYyNjMxOTI2OTM1MDksMTE5MzkxMTUxNzYxMDUwODgyLDQ3NDA2MjYzMTkyNjkzNTA5DQoxMTIxMTE1NzE4MzU1MTIzMDcsNTI4ODI4NTEwMjYwNzI1MDcsMTE5MzkxMTUxNzYxMDUwODgyLDU3MjA4MDc3NzY2NTg1MzA2DQoxMTkzOTExNTE3NjEwNTA4ODIsMTEyMTExNTcxODM1NTEyMzA3LDgxNjkxNTY2NjM5Mjc5MjksMTM0NDM0Mjk1ODk0ODAzODA2DQo1NzIwODA3Nzc2NjU4NTMwNiw0NzQwNjI2MzE5MjY5MzUwOSwxODU1ODIxMDUyNzUwNTA5MzIsMTc0NjMyMjI5MzEyMDQxMjQ4DQoxMzQ0MzQyOTU4OTQ4MDM4MDYsODIzODU5NjMzMzQ0MDQyNjgsMTcyNTY1Mzg2MzkzNDQzNjI0LDEwNjM1NjUwMTg5MzU0NjQwMQ0KODE2OTE1NjY2MzkyNzkyOSw0NzQwNjI2MzE5MjY5MzUwOSwxMDM2MTA1OTcyMDYxMDgxNiwxMzQ0MzQyOTU4OTQ4MDM4MDYNCjExOTM5MTE1MTc2MTA1MDg4MiwxNzI1NjUzODYzOTM0NDM2MjQsNDc0MDYyNjMxOTI2OTM1MDksODE2OTE1NjY2MzkyNzkyOQ0KNTI4ODI4NTEwMjYwNzI1MDcsMTE5MzkxMTUxNzYxMDUwODgyLDgxNjkxNTY2NjM5Mjc5MjksNDc0MDYyNjMxOTI2OTM1MDkNCjQ1ODE1MzIwOTcyNTYwMjAyLDE3NDYzMjIyOTMxMjA0MTI0OCwzMDI2MDU2NTIzNTEyODcwNCw0NzQwNjI2MzE5MjY5MzUwOQ0KNTI4ODI4NTEwMjYwNzI1MDcsMTE5MzkxMTUxNzYxMDUwODgyLDExMTUyMzQwODIxMjQ4MTg3OSwxMzQ0MzQyOTU4OTQ4MDM4MDYNCjQ3NDA2MjYzMTkyNjkzNTA5LDExMjExMTU3MTgzNTUxMjMwNyw1Mjg4Mjg1MTAyNjA3MjUwNywxMTkzOTExNTE3NjEwNTA4ODINCjU3MjA4MDc3NzY2NTg1MzA2LDExOTM5MTE1MTc2MTA1MDg4MiwxMTIxMTE1NzE4MzU1MTIzMDcsODE2OTE1NjY2MzkyNzkyOQ0KMTM0NDM0Mjk1ODk0ODAzODA2LDU3MjA4MDc3NzY2NTg1MzA2XQ=="
    private_key = wienerAttack(N, e)
    encrypted_message = decode(cipher)
    decrypted_string = decrypt(encrypted_message, private_key, N)
    print(decrypted_string)
