



grep "SRR072893" SRR072893_map.sam_ cut -f 3 | sort | uniq -c

cut -f 3 | sort | uniq -c


for 


f = open('SRR072893.sam')
counter = 0
for i, line in enumerate( f ):
    if line.startswith("@", ""):
        continue
    fields = line.split("\t")
    if fields[2] == "*":
        continue
    counter += 1
    
print (counter)
