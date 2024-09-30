import os
from glob import glob
result = [y for x in os.walk('c:/users/santony/Documents') for y in glob(os.path.join(x[0], '*.txt'))]
for index, item in enumerate(result):
    print(index, item)
