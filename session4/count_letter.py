sentence = 'aybceaefgwoifgjwf'

count_dictionary = {}
for char in sentence:
  if char in count_dictionary:
    count_dictionary[char] = count_dictionary[char] + 1
  else:
    count_dictionary[char] = 1

key_values_list = sorted(count_dictionary.items())

for key_value in key_values_list:
  print(key_value[0], key_value[1])

