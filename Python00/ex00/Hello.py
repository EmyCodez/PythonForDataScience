ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list.append('World!')
ft_tuple = ft_tuple[:1] + ("UAE!",)
ft_set.discard("tutu!")
ft_set.add("Abudhabi!")
ft_dict["Hello"] = "42Abudhabi!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
