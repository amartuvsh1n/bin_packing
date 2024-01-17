### Download lib
``` pip install binpacking ```

### excel file shoud be like below
```
volume	count	length
6.2	    2	    	12
5.15	9		    12
4.8	    48		    12
3.75	9		    12
6.36	26		    12
5.31	9		    12
4.96	36		    12
3.91	9		    12
```



### Run app
``` 
git clone https://github.com/amartuvsh1n/bin_packing.git
pip install pandas binpacking openpyxl
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
