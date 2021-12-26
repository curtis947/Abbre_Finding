# Abbre_Finding
This script can automatically find all the abrreviation in your file, and catch the description of them. What you need to do is to write down the input file path and output file path.

The basic logic of this method is that as the most abbreviation terms are capital letters, we can simply find words which are all capitals.
```Python
myabb=re.findall(r"\b[A-Z]{2,}\b", mytext)
```
Also, the basic information of the abbreviation is important, otherwise it's hard to figure out what it is. Since most people would write abbreviation in the bracket with its full words ahead, the information can be found if we search "(abbreviation)" and its sentence.
```Python
sent_find=re.findall(r'.*?\('+i+'\)', mytext)
```
