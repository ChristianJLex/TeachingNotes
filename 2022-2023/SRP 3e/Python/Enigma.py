# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 12:58:56 2023

@author: CJLex
"""

"""
 The following is a simulator of an Enigma machine. 
 You can specify your own rotors and plugboard settings or use the 
 build-in functions to generate rotors, reflector and plugboard settings
 at random. 
"""

import random as rd

# N is the size of the alphabet. The enigma machine used historically
# had 26 letters. N should be even or the reflector wont work properly.
N = 26


def rotor_construct(number_of_rotors):
    rotors = []
    notch = rd.sample(range(N), number_of_rotors-1)
    for i in range(number_of_rotors):
        rotor = list(range(N))
        rd.shuffle(rotor)
        rotors.append(rotor)
    return notch, rotors

def reflector_construct():
    sample_lst = rd.sample(range(N),N)
    reflector = ['placeholder']*int(N)
    while(len(sample_lst)>0):
        j = 0
        while(reflector[j] != 'placeholder'):
            j += 1
        if(j == sample_lst[0]):
            reflector[j] = sample_lst[1]
            reflector[sample_lst[1]] = j
            sample_lst.pop(1)
            sample_lst.remove(j)
        else:
            reflector[j] = sample_lst[0]
            reflector[sample_lst[0]] = j
            sample_lst.remove(j)
            sample_lst.pop(0)
    return reflector
    
def plugboard_setting(number_of_plugs):
    if number_of_plugs > N/2:
        raise ValueError("number of plugs must be less than 14")
    plugs = rd.sample(range(N),2*number_of_plugs)
    return plugs



def letter_encode(letter,rotors,reflector,plugs):
    def plugflow(letter,plugs):
        for i in range(len(plugs)):
            if letter == plugs[i]:
                letter = plugs[int((i + len(plugs)/2) % len(plugs))]
                break
        return letter
    letter = plugflow(letter,plugs)
    for rotor in rotors:
        letter = rotor[letter]
    letter = reflector[letter]
    rev = reversed(rotors)
    for rotor in rev:
        for i in range(N):
            if(letter == rotor[i]):
                letter = i
                break
    letter = plugflow(letter,plugs)
    return letter


def letter_check(rotors,reflector,plugs):
    lst = []
    rev_lst = []
    for i in range(N):
        lst.append(letter_encode(i,rotors,reflector,plugs))
        rev_lst.append(letter_encode(lst[i],rotors,reflector,plugs))
    if rev_lst == list(range(N)):
        return True
    else:
        return False

def list_rotate(lst):
    new = []
    for i in range(len(lst)):
        new.append(lst[(i-1) % len(lst)])
    return new
    
def rotor_shift(notch,rotors):
    for i in range(len(notch)):
        if(i == 0 and notch[0] == rotors[0][0]):
            rotors[1] = list_rotate(rotors[1])
        if(notch[i] == rotors[i][0] and i != 0):
            rotors[i] = list_rotate(rotors[i])
            rotors[i+1] = list_rotate(rotors[i+1])
    rotors[0] = list_rotate(rotors[0])   
    return rotors


def string_to_intlist(string):
    intlist = []
    for i in string:
        intlist.append(ord(i)-97)
    return intlist

def intlist_to_string(lst):
    string = ''
    for i in lst:
        string = string + chr(i+97)
    return string

def Enigma_encoder(plaintext,notch,rotors,reflector,plugs):
    as_lst = string_to_intlist(plaintext)
    cipher_lst = []
    for i in as_lst:
        cipher_lst.append(letter_encode(i, rotors, reflector, plugs))
        rotors = rotor_shift(notch,rotors)
    cipher_text = intlist_to_string(cipher_lst)
    return cipher_text
            

if __name__ == "__main__":
    #It is possible to change the size of the alphabet - but don't!
    N = 26
    
    
    #            [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7,  8 , 9 , 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    rotors =    [[22, 9 , 17, 16, 6 , 0 , 15, 21, 4 , 23, 3 , 18, 2 , 19, 10, 1 , 24, 14, 25, 8 , 7 , 12, 20, 11, 5 , 13],
                 [16, 23, 13, 6 , 1 , 12, 25, 11, 4 , 0 , 17, 8 , 22, 21, 18, 15, 9 , 20, 19, 3 , 5 , 24, 10, 7 , 2 , 14],
                 [20, 18, 17, 23, 8 , 12, 10, 11, 6 , 15, 19, 25, 13, 14, 1 , 3 , 21, 5 , 7 , 16, 2 , 24, 9 , 22, 4 , 0 ]]
    reflector =  [4 , 24, 5 , 6 , 0 , 2 , 3 , 21, 19, 11, 14, 9 , 20, 18, 10, 22, 17, 16, 13, 8 , 12, 7 , 15, 25, 1 , 23]

    notch = [4,11]
    plugs = [0,1,2,3,4,5]


    #notch, rotors = rotor_construct(3)
    #reflector = reflector_construct()
    
    print(Enigma_encoder('ylhlhndtrgedakiag',notch,rotors,reflector,plugs))
    



