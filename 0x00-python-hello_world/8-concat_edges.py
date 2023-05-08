#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
start_index = str.index("interpreted")
end_index = str.index("language") - 1
mid_index1 = str.index("object")
mid_index2 = str.index("with") - 1
new_str = str[start_index:end_index] + str[mid_index1:mid_index2] + str[:6]
print(new_str)
