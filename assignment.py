# 문제 1
string = input("문자열을 입력하세요 > ")
cnt = 0
if "e" not in string:
    print(-1)
else:
    for i in string:
        if " " == i:
            continue
        else:
            cnt += 1
            if "e" == i:
                print(cnt)
                break


# 문제 2
strings = list(input("문자열을 입력하세요 > ").split())
string_dict = {}
for string in strings:
    cnt = 0
    for string_2 in strings:
        if string == string_2:
            cnt += 1
            string_dict[string] = cnt

for string, cnt in string_dict.items():
    print(string, cnt)


# 문제 3
strings = input("문자열을 입력하세요 > ")
string_list = []
for string in strings:
    if string == "e":
        continue
    else:
        string_list.append(string)

for word in string_list:
    print(word, end="")


# 문제 4
string_list = list(input().split())
cnt = 0
for word in string_list[0]:
    if word == string_list[1]:
        cnt += 1
print(cnt)
    

# 문제 5
a, b, c = list(input("문자열을 입력하세요 > ").split())
print("{0}-{1}-{2}".format(a, b, c))


# 문제 6
number = int(input("문자열을 입력하세요 > "))

if number < 0:
    print(-1)
else:
    a = number // 100
    b = (number - a * 100) // 10
    c = number - (a * 100 + b * 10)
    print(a + b + c)

