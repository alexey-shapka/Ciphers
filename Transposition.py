import math

class Transposition:

    def __init__(self, string):
        self.key = 'ourkey'
        self.lenOfRow = len(self.key)
        self.string = string
        self.parts = math.ceil(len(self.string)/self.lenOfRow)
        self.indexes = list(map(lambda  i: [i, self.key[i]] , [j for j in range(len(self.key)) ]))
        self.indexes.sort(key=lambda x: x[1])
        self.flag = False

    def crypt(self):
        if self.flag == False:

            array = []
            newString = ''

            for i in range(self.parts):
                part = list(self.string[i*self.lenOfRow:(i+1)*self.lenOfRow])
                array.append(part)

            for i in self.indexes:
                for j in range(self.parts):
                    try:
                        newString += array[j][i[0]]
                    except:
                        continue

            self.string = newString
            self.flag = True

        else:
            print('Already crypt!')

    
    def encrypt(self):
        if self.flag == True:

            blanks = len(self.string)%self.lenOfRow
            array = []

            point=0
            for j in self.indexes:
                part=[]
                try:
                    if blanks != 0 and j[0]>=blanks:
                        for k in range(point, point+self.parts-1):
                            part.append(self.string[k])
                        part.append('')
                        point += self.parts-1
                    else:
                        for k in range(point, point+self.parts):
                            part.append(self.string[k])
                        point += self.parts
                except:
                    continue
                array.append(part)

            reshape = [['' for i in range(self.lenOfRow)] for i in range(self.parts)]

            point=0
            for i in self.indexes:
                for j in range(self.parts):
                    reshape[j][i[0]] = array[point][j]
                point += 1

            self.string = ''.join([''.join(i) for i in reshape])
            self.flag = False

        else:
            print('Already encrypt!')

    def getString(self):
        return self.string
        
        

word = 'WE ARE DISCOVERED SAVE YOURSELF'

print("Start string %s" % word)
trans = Transposition(word)
trans.crypt()
print(trans.getString())
trans.encrypt()
print(trans.getString())