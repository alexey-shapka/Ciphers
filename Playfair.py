import collections
import itertools
import math
import numpy
import pprint

class Playfair:

    def __init__(self, string):
        self.string = string.replace(" ", "")
        self.alphabet = [[chr(j) if j < 74 else chr(j+1) for j in range(65+i*5, 65+(i+1)*5)] for i in range(5)] 
        self.key = 'WHEATSTON'
        self.keyAlphabet = self.ChangeAlphabet()
        self.transposedKeyAlphabet = numpy.array(self.keyAlphabet).transpose().tolist()

    def ChangeAlphabet(self):
        newAlphabet =  "".join(collections.OrderedDict.fromkeys(self.key))
        for i in "".join(itertools.chain(*self.alphabet)):
            if i not in newAlphabet:
                newAlphabet += i
        newAlphabet = [[newAlphabet[j] for j in range(i*5, (i+1)*5)] for i in range(5)]
        return newAlphabet

    def Check(self, number):
        number+=1
        if number>4:
            return 0
        else:
            return number

    def Crypt(self):
        bigrams = []
        while(len(self.string)) != 0:
            bigram = self.string[0:2]
            if len(bigram) == 2:
                if bigram[0] == bigram[1]:
                    bigram = bigram[0] + 'X'
                    bigrams.append(bigram)
                    self.string = self.string[1:]
                else:
                    bigrams.append(bigram)
                    self.string = self.string[2:]
            else:
                bigram = bigram[0] + 'X'
                bigrams.append(bigram)
                self.string = ''

        pprint.pprint(self.keyAlphabet)
        for i in bigrams:
            letters = list(i)
            chars = []
            
            for j in range(5):
                if letters[0] in self.keyAlphabet[j] and  letters[1] in self.keyAlphabet[j]:
                    firstChar = self.keyAlphabet[j][self.Check(self.keyAlphabet[j].index(letters[0]))]
                    secondChar = self.keyAlphabet[j][self.Check(self.keyAlphabet[j].index(letters[1]))]
                    self.string += firstChar + secondChar# + '[{0}]'.format(letters[0]+letters[1])
                    break

                elif letters[0] in self.transposedKeyAlphabet[j] and  letters[1] in self.transposedKeyAlphabet[j]:
                    firstChar = self.transposedKeyAlphabet[j][self.Check(self.transposedKeyAlphabet[j].index(letters[0]))]
                    secondChar = self.transposedKeyAlphabet[j][self.Check(self.transposedKeyAlphabet[j].index(letters[1]))]
                    self.string += firstChar + secondChar# + '[{0}]'.format(letters[0]+letters[1])
                    break

                elif letters[0] in self.keyAlphabet[j]:
                    chars.append([j, self.keyAlphabet[j].index(letters[0]), letters[0]])

                elif letters[1] in self.keyAlphabet[j]:
                    chars.append([j, self.keyAlphabet[j].index(letters[1]), letters[1]])
            
            if len(chars) == 2:
                chars[0][1], chars[1][1] = chars[1][1], chars[0][1]
                if letters[0] == chars[0][2]:
                    self.string += self.keyAlphabet[chars[0][0]][chars[0][1]] + self.keyAlphabet[chars[1][0]][chars[1][1]]
                else:
                    self.string += self.keyAlphabet[chars[1][0]][chars[1][1]] + self.keyAlphabet[chars[0][0]][chars[0][1]]
            self.string += " "

    def getString(self):
        return self.string




start = 'IDIOCY OFTEN LOOKS LIKE INTELLIGENCE'
print("Start string '%s'"  % start)

string = Playfair(start)
string.Crypt()
print(string.getString())
# string.encrypt()
# print(string.getString())

