import sys
import secrets
import hashlib
import hmac

listOfThings = list(sys.argv)
del listOfThings[0]
countOfThings = len(listOfThings)
if countOfThings % 2 == 0 or countOfThings == 0:
    print("The count of arguments must be an odd number > 1")
else:
    def make_digest(message, key):
        key = bytes(key, 'UTF-8')
        message = bytes(message, 'UTF-8')
        digester = hmac.new(key, message, hashlib.sha3_512)
        return digester.hexdigest()

    def generate_random_number(to):
        secretsGenerator = secrets.SystemRandom()
        randomNumber = secretsGenerator.randint(0,to)
        return randomNumber

    print("******************************************************")
    i = 0
    while True:
       i = i + 1
       print(str(i) + " GAME")
       computerNumber = generate_random_number(countOfThings-1)
       secretkey = secrets.token_hex(32)
       s = make_digest(listOfThings[computerNumber],secretkey)
       print("HMAC:" + s)

       for index,e in enumerate(listOfThings):
            print(str((index+1)) + "." + e)
       print("0.Выход\n")

   
       selected = input("Choose, please :)\n") 
       if selected != "0":
           try:
            print("Your choose:", listOfThings[int(selected)-1])
           except Exception:
            print("\nException. Write correct number.")
            print("\n******************************************************\n")
            continue
       elif selected == '0':
            print("Good bye!")
            break
       print("Computer choose:", listOfThings[computerNumber])

       personNumber = int(selected) - 1
       range = countOfThings//2

       if personNumber == computerNumber:
           print("DRAW!")
       elif ((personNumber + range) >= computerNumber) and ((personNumber + range)<=countOfThings) and (computerNumber>personNumber):
           print("YOU WIN!")
       elif (personNumber + range) >= countOfThings:
           if (personNumber + range - countOfThings) >= computerNumber:
               print("YOU WIN!")
           else:
               print("COMPUTER WIN!")
       else: 
           print("COMPUTER WIN!")

       print("--------------------------------------------------")
       print("Secret key is '" + secretkey + "'" );
       print("To check result you should:")
       print("0. Go to: https://www.liavaag.org/English/SHA-Generator/HMAC/")
       print("1. In field \"Input\" write '" + listOfThings[computerNumber] + "'")
       print("2. In field \"Key\" write '" + secretkey + "'")
       print("3. Choose SHA3-512 variant and check result with HMAC")
       print("--------------------------------------------------")
       print("\n******************************************************\n")

           
