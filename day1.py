# DAY 1:
# I forgot to save the first question, but it was similar
ris = 0
numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
keys = numbers.keys()
with open('input.txt', 'r') as file:
    for line in file:
        first_number, last_number = None, None
        string = ''
        inverted_line = line[::-1]
        for char in line:
            if first_number is not None:
                break
            string += char
            if ord('0') <= ord(char) <= ord('9'):
                first_number = char
            for key in keys:
                if key in string:
                    first_number = numbers[key]
                    print(key, string)

        string = ''
        for char in inverted_line:
            string += char
            if last_number is not None:
                break
            if ord('0') <= ord(char) <= ord('9'):
                last_number = char
            for key in keys:
                if key in string[::-1]:
                    last_number = numbers[key]
        ris += int(first_number + last_number)
      
print(ris)
