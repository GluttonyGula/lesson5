immutable_var = 1, True, 'привет'
print(immutable_var)
#immutable_var[0] = 10 #переменная immutable_var яыляется кортежем, т.е. неизменяемым типом даных (tuple)
mutable_list = 1, 2, [4, 'apple', 8]
mutable_list[2][1] = 'peach'
print(mutable_list)