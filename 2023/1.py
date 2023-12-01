with open("input1.txt", "r") as f:
    data = f.read()
    
lines = data.split('\n')

total_calibration = 0
total_calibration2 = 0

for line in lines:
    list_digits = []
    list_digits2 = []
    for i, char in enumerate(line):            
        if char.isdigit():
            list_digits.append(char)
            list_digits2.append(char)
        for j, value in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(value):
                list_digits2.append(str(j+1))
                
    total_calibration += int(list_digits[0] + list_digits[-1])
    total_calibration2 += int(list_digits2[0] + list_digits2[-1])
    
print(total_calibration, total_calibration2)