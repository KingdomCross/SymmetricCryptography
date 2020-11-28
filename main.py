# Alex Chheng
# 10/2/2020
# Lab 1: Substitution Cipher
# https://www.youtube.com/watch?time_continue=1&v=j7M7Xo_hd8M&feature=emb_title&ab_channel=Nh%E1%BA%ADtQuangNguy%E1%BB%85n, https://inventwithpython.com/hacking/chapter17.html, https://stackoverflow.com/questions/36188226/substitution-cipher-python, https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_simple_substitution_cipher.htm, https://stackoverflow.com/questions/10155729/replace-characters-in-string-from-dictionary-mapping, https://stackoverflow.com/questions/13500897/substitution-encryption-problemsetquestion-in-python, https://www.pythonpool.com/python-alphabet/#:~:text=%20Generating%20a%20list%20of%20Alphabets%20in%20Python,function%20to%20produce%20the%20list%20of...%20More%20, https://www.datasciencebytes.com/bytes/2014/11/03/get-a-list-of-all-english-words-in-python/

import random, sys, base64, hashlib, sys


# This work when working with more words
def SubstitutionCrack(encoded, lower):  # Using letter frequency analysis
    # print("Substitution Crack")

    # decoded = ""
    # for i in encoded:
    #     if ((i >= 'a' and i <= 'g') or (i == ' ')):
    #         if ((i >= 'a' and i <= 'g')):
    #             encoded = encoded + str(chr(ord(i) + 19))
    #         elif ((i >= 'h' and i <= 'z')):
    #             encoded = encoded + str(chr(ord(i) - 7))
    #         elif (i == ' '):
    #             encoded = encoded + str(i)
    #     else:
    #         continue
    # if (encoded == ""):
    #     print("No hidden message")
    # else:
    #     print("Decrypted text: %s " %encoded)

    frequency_lower = list(range(26))  # Used to create list of frequency
    for x in range(0, 26):
        frequency_lower[x] = 0

    for x in range(0, len(encoded)):  # Finding the frequency of the letters, using letter frequency analysis
        for y in range(0, 26):
            if encoded[x] == alphabetLower[y]:
                frequency_lower[y] = frequency_lower[y] + 1

    maxval_lower = max(frequency_lower)

    freq_list_lower = lower.copy()
    n = 0
    freq_test_lower = 0

    for x in range(0, maxval_lower + 1):  # Finding the frequency of the letters, using letter frequency analysis
        freq_test_lower = maxval_lower - x
        for y in range(0, 26):
            if frequency_lower[y] == freq_test_lower:
                freq_list_lower[n] = alphabetLower[y]
                n = n + 1

    # The frequency of the letter
    english_freq_lower = ['e', 't', 'a', 'o', 'i',
                          'n', 's', 'h', 'r', 'd',
                          'l', 'c', 'u', 'm', 'w',
                          'f', 'g', 'y', 'p', 'b',
                          'v', 'k', 'j', 'x', 'q', 'z']

    print()
    print("Letter frequency: ")
    print(english_freq_lower)
    print("Letters in encoded message ordered by frequency: ")
    print(freq_list_lower)
    # In alphabet order
    key = [freq_list_lower[2], freq_list_lower[19], freq_list_lower[11], freq_list_lower[9], freq_list_lower[0],
           freq_list_lower[15], freq_list_lower[16],
           freq_list_lower[7], freq_list_lower[4], freq_list_lower[22], freq_list_lower[21], freq_list_lower[10],
           freq_list_lower[13], freq_list_lower[5],
           freq_list_lower[3], freq_list_lower[18], freq_list_lower[24], freq_list_lower[8], freq_list_lower[6],
           freq_list_lower[1], freq_list_lower[12],
           freq_list_lower[20], freq_list_lower[14], freq_list_lower[23], freq_list_lower[17], freq_list_lower[25]]
    print("The alphabet letters")
    print(alphabetLower)
    print("The substitution key value")
    print(key)

    decoded = ""
    # Changing the frequency letter with the common english frequency letter
    for x in range(0, len(encoded)):
        if encoded[x] != " ":
            for y in range(0, 26):
                if encoded[x] == freq_list_lower[y]:
                    decoded = decoded + english_freq_lower[y]
        if encoded[x] == " ":
            decoded = decoded + " "
    print()
    print("Encoded message: " + encoded)
    print("Decoded message: " + decoded)


# using string to cipher, alphabet in lowercase and uppercase
def encryption(cipher, x, lower, upper):
    shuffledLower = lower.copy()
    shuffledUpper = upper.copy()

    random.seed(x)  # used to randomize the letter instead of the default random
    random.shuffle(shuffledLower)  # shuffle
    random.shuffle(shuffledUpper)

    encoded = ""
    for x in range(0, len(cipher)):  # length of the string
        if cipher[x] == " ":  # spacing of the string
            encoded = encoded + " "
        else:
            for y in range(0, 26):  # Letter check
                if cipher[x] == alphabetLower[y]:
                    encoded = encoded + shuffledLower[y]
                elif cipher[x] == alphabetUpper[y]:
                    encoded = encoded + shuffledUpper[y]

    print()
    print("Original message: " + cipher)  # output the stirngs to encrypt
    print("Encoded message: " + encoded)  # output the encrypt string
    print(
        "[Original lowercase letter] [shuffle lowercase letter] [original uppercase letter] [shuffle uppercase letter]")
    print(lower)
    print(shuffledLower)  # this is a lowercase shuffle key
    print(upper)
    print(shuffledUpper)  # This is uppercase shufflekey

    return encoded, shuffledLower, shuffledUpper  # return the encrypt, shuffleLower, shuffleUpper. It is used to output encryption and decryption with shuffled keys


# Decrypt using encryption word, alphabet in lowercase and uppercase
def decryption(encrypt, lower, upper):
    # print("decryption")
    cipher = encrypt[0]
    shuffledLower = encrypt[1]
    shuffledUpper = encrypt[2]

    encoded = ""

    for x in range(0, len(cipher)):
        if cipher[x] == " ":
            encoded = encoded + " "
        else:
            for y in range(0, 26):
                if cipher[x] == shuffledLower[y]:
                    encoded = encoded + lower[y]
                elif cipher[x] == shuffledUpper[y]:
                    encoded = encoded + upper[y]

    print()
    print("Encoded message: " + cipher)
    print("Original message: " + encoded)
    print(
        "[Original lowercase letter] [shuffle lowercase letter] [original uppercase letter] [shuffle uppercase letter]")
    print(lower)
    print(shuffledLower)
    print(upper)
    print(shuffledUpper)


# Used for the encryption and decryption
alphabetLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
alphabetUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']

# Assignment for encrypting the strings and decrypting
cipher1 = "He who fights with monsters should look to it that he himself does not become a monster. And if you gaze long into an abyss, the abyss also gazes into you."
cipher2 = "There is a theory which states that if ever anybody discovers exactly what the Universe is for and why it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable. There is another theory which states that this has already happened."
cipher3 = "Whenever I find myself growing grim about the mouth ; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off - then, I account it high time to get to sea as soon as I can."

print()
x = int(input(
    "Enter a seed (any integer): "))  # This is used to shuffle the randomize instead of the standard random python

# After the function, it return the value of the encryption, shuffle lowercase, shuffle uppercase
print("------------------Encrypt------------------------------")
encrypt1 = encryption(cipher1, x, alphabetLower, alphabetUpper)
encrypt2 = encryption(cipher2, x, alphabetLower, alphabetUpper)
encrypt3 = encryption(cipher3, x, alphabetLower, alphabetUpper)
print("------------------Decrypt------------------------------")
decryption(encrypt1, alphabetLower, alphabetUpper)
decryption(encrypt2, alphabetLower, alphabetUpper)
decryption(encrypt3, alphabetLower, alphabetUpper)
print()

encoded1 = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"
encoded2 = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy"
encoded3 = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"
encoded4 = "iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"

SubstitutionCrack(encoded1, alphabetLower)
SubstitutionCrack(encoded2, alphabetLower)
SubstitutionCrack(encoded3, alphabetLower)
SubstitutionCrack(encoded4, alphabetLower)
