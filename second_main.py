# garaltiin davhtsliig toogoor bichih
# diametereer ni yalgah
import pandas as pd
import binpacking
from collections import Counter

# a array will be use sorted volume sizes
a=[]
data = pd.read_excel(r'./demo.xlsx') 
# in excel included 2 rows such as volume and count
df = pd.DataFrame(data, columns=['Required Length','Quantity', 'Diameter', 'Quality'])

# v for count repeat per volume
v=0

# i will take count values
for i in df['Quantity']:
    # j will take count of volume values 
    j=0
    while j < i: 
        # append in a 
        a.append(df['Required Length'][v])
        j += 1
    v += 1

# no need but I used sort.
a.sort(reverse=True)

# 12 is the volume count
maxVol=12
# classification
out1 = binpacking.to_constant_volume(a,maxVol)
# write to output.xlsx
#pd.DataFrame(out1).to_excel('output.xlsx', header=False, index=False)



#-----------------------------------

import numpy as np



# Find the maximum length among all sublists
max_length = max(len(sublist) for sublist in out1)

# Pad shorter sublists with zeros to make them the same length
padded_list = [sublist + [0] * (max_length - len(sublist)) for sublist in out1]

# Convert the padded list to a NumPy array
my_array = np.array(padded_list)

print(type(my_array))
