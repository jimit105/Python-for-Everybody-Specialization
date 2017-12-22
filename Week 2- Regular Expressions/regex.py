import re
file = open('regex_sum_37084.txt')
sum = 0
for line in file:
    line = line.rstrip()
    num_str = re.findall('[0-9]+', line)
    for i in range(len(num_str)):
        sum = sum + int(num_str[i])    
print(sum)
