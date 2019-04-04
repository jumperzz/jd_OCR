import os

for each in os.walk('pupiao/'):
    print(each[2][0])