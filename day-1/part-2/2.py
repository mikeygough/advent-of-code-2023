# set file
fname = 'calibration-document.txt'

# read in file
with open(fname, 'r') as file:
    calibration_document = file.readlines()
    file.close()
    
alphanumeric_digits = {'zero': '0',
                      'one': '1',
                      'two': '2',
                      'three': '3',
                      'four': '4',
                      'five': '5',
                      'six': '6',
                      'seven': '7',
                      'eight': '8',
                      'nine': '9'}

# get digits from each line
digits = []
for line in calibration_document:
    written_digit = ''
    temp = ''
    for value in line:
        if value.isdigit(): # check for digit
            temp += value
        else: # check for written digit
            written_digit += value
            for key in alphanumeric_digits.keys():
                if key in written_digit: # found
                    temp += alphanumeric_digits[key] # add digit
                    # written_digit = ''
                    written_digit = written_digit[-2:] # reset check
                    # this allows us to read eighttwo -> [8, 2]
    print("Line", line)
    print("Temp", temp)
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

# print(digits)
# print(calibration_digits)
# sum values
print(sum(calibration_digits))