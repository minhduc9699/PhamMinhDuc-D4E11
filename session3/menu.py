monan1 = 'phở'
monan2 = 'bún chả'
monan3 = 'trứng rán'
monan4 = 'thịt chó'
monan5 = 'cơm'

monan = ['phở', 'bún chả', 'trứng rán', 'thịt chó']
for i in range(len(monan)):
  print(i+1, monan[i])

# update_value = input('nhập tên món ăn muốn đổi')
# if update_value in monan:
#   index = monan.index(update_value)

#   monan[index] = input('nhập tên món ăn mới')
#   print(monan)
# else:
#   print('k tìm thấy món đó đâu mannn')

# a = input()
# monan.append(a) # CREATE
for i in range(len(monan)):
  print(monan[i]) # READ
monan[0] = 'cơm' # UPDATE
# print('trứng' in monan)
# print(monan.index('trứng r'))
monan.pop(0) # DELETE by index
monan.remove('bún chả') # DELETE by value
print(monan)