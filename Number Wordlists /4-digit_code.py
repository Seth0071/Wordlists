#4-digit Wordlist Creator for Diciotnary Attacks

password = 0

list1 = open('4-digit_list.txt', 'w')

for i in range(9999):
    password = password + 1
    if (password <= 9):
        passw = "000" + str(password)
        #list1.write(f"{passw}\n")  #    < Delete comment for wordlist file
        print(passw) #     < Delete comment for shell output of wordlist
    elif (password <= 99):
        passw = "00" + str(password)
        #list1.write(f"{passw}\n") #    < Delete comment for wordlist file
        print(passw) #     < Delete comment for shell output of wordlist
    elif (password <= 999):
        passw = "0" + str(password)
        #list1.write(f"{passw}\n") #    < Delete comment for wordlist file
        print(passw) #     < Delete comment for shell output of wordlist
    elif (password <= 9999):
        passw = "" + str(password)
        #list1.write(f"{passw}\n") #    < Delete comment for wordlist file
        print(passw) #     < Delete comment for shell output of wordlist
list1.close()
