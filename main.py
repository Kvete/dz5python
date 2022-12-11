user_list = [2, 2, 2, 7, 23, 7, 2, 8, 44, 44]
res = [el for el in user_list if user_list.count(el) == 1]
print(res)
res = list(map(lambda el: el ** 2, res))
print(res)
res = list(filter(lambda el: user_list.count(el) == 1, user_list))
print(res)
