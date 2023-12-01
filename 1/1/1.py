# set file
fname = 'calibration-document.txt'

# read in file
with open(fname, 'r') as file:
    calibration_document = file.readlines()
    file.close()

# get digits from each line
digits = []
for line in calibration_document:
    temp = ''
    for value in line:
        if value.isdigit():
            temp += value
    digits.append(temp)

# get first and last digit
calibration_digits = []
for digit in digits:
    temp = ''
    if len(digit) < 2: # use value twice
        temp += digit * 2
    else:
        # get first and last digit
        temp += digit[0]
        temp += digit[-1]
    calibration_digits.append(int(temp))
        
# sum values
print(sum(calibration_digits))