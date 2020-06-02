teen_code = {
  'hc': 'học',
  'nc': 'nói chuyện',
  'vk': 'vũ khí',
  'ck': 'chuyển khoản',
}

while True:
  for key in teen_code:
    print(key, end='\t')
  print()
  print('*'*30)

  input_key = input('enter the word you want to search: ')
  if input_key in teen_code:
    print('it`s mean: ', teen_code[input_key])
  else:
    prompt = input('word not found, would u like to contribute it`s meaning?')
    if prompt == 'y':
      teen_code[input_key] = input('enter meaning: ')
    else:
      print('bye')
      break