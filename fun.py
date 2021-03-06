import subprocess
from pandas import DataFrame as DF

def chartotext(x):
    '''
    a function that converts the processe characters into text codes 
    '''
    letters = []
    for element in x:
        # this separates the individual character values intro single digits
        val = 0
        h = 0
        for one in element:
            val += int(one) * (2**h)
            h += 1
        letters.append(val)
    return letters

def bintotext(a):
    '''
    a function that takes in a list of numbers and returns its character code
    '''
    characters = []
    for item in a :
        work = str(item)[3:]
        b = work[::-1]
        # up to here each number in the series is reveresed and only represent characters
        characters.append(b)
        # a list of all the bionarys that have already been processed 
    return characters
                 
x = [1100010,1100101,1110010,1011111,1010011,110010,1100011,1110101,1110010,1101001,1110100,1111001,100000,1001000,1110101,1100010]
y = chartotext(bintotext(x))
z =[]
for i in x:
    a = str(i)
    b = a[0:3]
    z.append(int(b))

words = {
    'code': y,
    'case': z
}

# creating a dataframe to be converted to csv
df = DF(words, columns = ['case','code'])
export = df.to_csv(r'~/Documents/Fun/letters.csv')
# confirming the file has been made
print(df)

subprocess.call("go run main.go", shell=True)