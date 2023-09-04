### Download lib
``` pip install binpacking ```
### Run app
``` 
git clone https://github.com/amartuvsh1n/bin_packing.git
pip install pandas binpacking
python main.py 
```

### example code
```
# don't know now, How to read exactly counts from excel
import binpacking

items = [2, 5, 5, 10, 2]

# binpacking can sort 
items.sort(reverse=True)

# 12 is the volume count
armaturs = binpacking.to_constant_volume(b,12)
print(armaturs) 
```

example result 
``` [[5, 5, 2], [10, 2]] ```
