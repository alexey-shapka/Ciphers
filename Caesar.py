class Caesar:

    def __init__(self, string, number):
        self.string = string
        self.number = number
        self.change = self.number % 26
        self.flag = False
    
    def crypt(self):
        if self.flag == False:
            newString = ""
            newOrd = 0
            for i in self.string:
                currentOrd = ord(i)
                if i.islower() == True:
                    if currentOrd + self.change > 122:
                        newOrd = (currentOrd + self.change - 97) % 26 + 97
                    else: 
                        newOrd = currentOrd + self.change
                else:
                    if currentOrd + self.change > 90:
                        newOrd = (currentOrd + self.change - 65 ) % 26 + 65
                    else: 
                        newOrd = currentOrd + self.change
                newString += chr(newOrd)
            self.string = newString
            self.flag = True
        else:
            print('Already crypt!')

    def encrypt(self):
        if self.flag == True:
            newString = ""
            newOrd = 0
            for i in self.string:
                currentOrd = ord(i)
                if i.islower() == True: 
                    if currentOrd - self.change < 97:
                        newOrd = 122 - (currentOrd - 97)
                    else: 
                        newOrd = currentOrd - self.change
                else:
                    if currentOrd - self.change < 65:
                        newOrd = 90 - (currentOrd - 65)
                    else: 
                        newOrd = currentOrd - self.change
                newString += chr(newOrd)
            self.string = newString
            self.flag = False
        else:
            print('Already encrypt!')
    
    def getString(self):
        return self.string

start = 'abcABC'
print("Start string '%s'"  % start)

string = Caesar(start, 23)
string.crypt()
print(string.getString())
string.encrypt()
print(string.getString())

