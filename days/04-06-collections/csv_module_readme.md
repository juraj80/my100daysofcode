### Python CSV tutorial - read write CSV

Python CSV tutorial shows how to read and write CSV data with Python csv module.

### CSV

CSV (Comma Separated Values) is a very popular import and export data format used in spreadsheets and databases. Each line in a CSV file is a data record. Each record consists of one or more fields, separated by commas. While CSV is a very simple data format, there can be many differecies, such as different delimiters, new lines, or quoting characters.

###Python csv module

The csv module implements classes to read and write tabular data in CSV format. The csv module's reader and writer objects read and write sequences. Programmers can also read and write data in dictionary form using the DictReader and DictWriter classes.


### Python CSV methods

The following table shows Python csv methods:

Method	| Description 
---| ---
csv.reader |	returns a reader object which iterates over lines of a CSV file
csv.writer |	returns a writer object which writes data into CSV file
csv.register_dialect |	registers a CSV dialect
csv.unregister_dialect |	unregisters a CSV dialect
csv.get_dialect |	returns a dialect with the given name
csv.list_dialects |	returns all registered dialects
csv.field_size_limit |	returns the current maximum field size allowed by the parser


### Using Python csv module

`
import csv
`

To use Python CSV module, we import csv.

### Python CSV reader

The `csv.reader()` method returns a reader object which iterates over lines in the given CSV file.

`$ cat numbers.csv 
16,6,4,12,81,6,71,6`

The `numbers.csv` file contains numbers.

_read_csv.py_
```#!/usr/bin/python3

import csv

f = open('numbers.csv', 'r')

with f:

    reader = csv.reader(f)

    for row in reader:
        for e in row:
            print(e)
            
```

In the code example, we open the `numbers.csv` for reading and read its contents.

`reader = csv.reader(f)`

We get the reader object.
```
for row in reader:
    for e in row:
        print(e)
```
With two for loops, we iterate over the data.
```
$ ./read_csv.py 
16
6
4
12
81
6
71
6
```

This is the output of the example.

### Python CSV reader with different delimiter

The `csv.reader()` method allows to use a different delimiter with its delimiter attribute.
```
$ cat items.csv 
pen|cup|bottle
chair|book|tablet
```
The `items.csv` contains values separated with '|' character.

_read_csv.py_
```
#!/usr/bin/python3

import csv

f = open('items.csv', 'r')

with f:

    reader = csv.reader(f, delimiter="|")
    
    for row in reader:
        
        for e in row:            
            print(e)
```
The code example reads and displays data from a CSV file that uses a '|' delimiter.
```
$ ./read_csv2.py 
pen
cup
bottle
chair
book
tablet
```

This is the output of the example.

### Python CSV DictReader

The `csv.DictReader` class operates like a regular reader but maps the information read into a dictionary. The keys for the dictionary can be passed in with the fieldnames parameter or inferred from the first row of the CSV file.
```
$ cat values.csv 
min,avg,max
1, 5.5, 10
2, 3.5, 5
```
The first line of the file consists of dictionary keys.

_read_csv_dictionary.py_
```
#!/usr/bin/python3

# read_csv3.py

import csv

f = open('values.csv', 'r')

with f:

    reader = csv.DictReader(f)
    
    for row in reader:
        print(row['min'], row['avg'], row['max'])
```

The example reads the values from the `values.csv` file using the `csv.DictReader`.
```
for row in reader:
    print(row['min'], row['avg'], row['max'] )
```    
The row is a Python dictionary and we reference the data with the keys.

### Python CSV writer

The `csv.writer()` method returns a writer object which converts the user's data into delimited strings on the given file-like object.

_write_csv.py_
```
#!/usr/bin/python3

import csv

nms = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]

f = open('numbers2.csv', 'w')

with f:

    writer = csv.writer(f)
    
    for row in nms:
        writer.writerow(row)
```
The script writes numbers into the `numbers2.csv` file. The `writerow()` method writes a row of data into the specified file.
```
$ cat numbers2.csv 
1,2,3,4,5,6
7,8,9,10,11,12
```
It is possible to write all data in one shot. The `writerows()` method writes all given rows to the CSV file.

_write_csv2.py_
```
#!/usr/bin/python3

import csv

nms = [[1, 2, 3], [7, 8, 9], [10, 11, 12]]

f = open('numbers3.csv', 'w')

with f:

    writer = csv.writer(f)
    writer.writerows(nms)
```
The code example writes three rows of numbers into the file using the `writerows()` method.

### Python CSV DictWriter

The `csv.DictWriter` class operates like a regular writer but maps Python dictionaries into CSV rows. The fieldnames parameter is a sequence of keys that identify the order in which values in the dictionary passed to the `writerow()` method are written to the CSV file.

_write_csv_dictionary.py_
```
#!/usr/bin/python3

import csv

f = open('names.csv', 'w')

with f:
    
    fnames = ['first_name', 'last_name']
    writer = csv.DictWriter(f, fieldnames=fnames)    

    writer.writeheader()
    writer.writerow({'first_name' : 'John', 'last_name': 'Smith'})
    writer.writerow({'first_name' : 'Robert', 'last_name': 'Brown'})
    writer.writerow({'first_name' : 'Julia', 'last_name': 'Griffin'})
```
The example writes the values from Python dictionaries into the CSV file using the `csv.DictWriter`.

`
writer = csv.DictWriter(f, fieldnames=fnames) 
`

New `csv.DictWriter` is created. The header names are passed to the fieldnames parameter.

`writer.writeheader()`

The `writeheader()` method writes the headers to the CSV file.

`writer.writerow({'first_name' : 'John', 'last_name': 'Smith'})`

The Python dictionary is written to a row in a CSV file.
```
$ cat names.csv 
first_name,last_name
John,Smith
Robert,Brown
Julia,Griffin
```
This is the output.

### Python CSV custom dialect

A custom dialect is created with the `csv.register_dialect()` method.

_custom_dialect.py_
```
#!/usr/bin/python3

import csv

csv.register_dialect("hashes", delimiter="#")

f = open('items3.csv', 'w')

with f:

    writer = csv.writer(f, dialect="hashes")
    writer.writerow(("pens", 4)) 
    writer.writerow(("plates", 2))
    writer.writerow(("bottles", 4))
    writer.writerow(("cups", 1))
```
The program uses a (#) character as a delimiter. The dialect is specified with the dialect option in the `csv.writer()` method.
```
$ cat items3.csv 
pens#4
plates#2
bottles#4
cups#1
```
This is the output.