import pandas as pd
import binpacking

# a array will be use sorted volume sizes
a=[]
data = pd.read_excel(r'./demo.xlsx') 
# in excel included 2 rows such as volume and count
df = pd.DataFrame(data, columns=['volume','count'])

# v for count repeat per volume
v=0

# i will take count values
for i in df['count']:
    # j will take count of volume values 
    j=0
    while j < i: 
        # append in a 
        a.append(df['volume'][v])
        j += 1
    v += 1

# no need but I used sort.
a.sort(reverse=True)

# 12 is the volume count, in future maxVol read from excel
maxVol=12
# classification
out = binpacking.to_constant_volume(a,maxVol)
# write to output.xlsx
pd.DataFrame(out).to_excel('output.xlsx', header=False, index=False)
