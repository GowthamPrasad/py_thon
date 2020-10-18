test_list = ["True", "False", "True", "True", "False"]
print("The original list : " + str(test_list))
res = [ele == "True" for ele in test_list]
print("The converted Boolean values : " + str(res))