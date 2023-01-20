import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!£$%&*"

print('*'*50)
print( '\t' '\t' "Password generator")
print('*'*50)

def main():
    while 1:
        all_passwords=[]

        password_len = int(input("De que longitud desea sus contraseñas (0 Close) :"))
        if(password_len==0):
            break
        password_count = int(input("Cuantas contraseñas quieres : "))

        number=1

        for x in range(0,password_count):
            password  = ""
            for x in range(0,password_len):
                password_char = random.choice(chars)
                password      = password + password_char
            print(str(number)+" - Esta es tu contraseña: ", password)
            all_passwords.append(password)
            number=number+1

        print("\n")

if __name__ == '__main__':
    main()