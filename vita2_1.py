str = input()
AB = str.find("12")
BA = str.find("21")

#print(str[:AB] + str[AB+2:])
#print(str[:BA] + str[BA+2:])

if ((AB != -1) and ((str[:AB] + str[AB+2:]).find("21") != -1)) or ((BA != -1) and ((str[:BA] + str[BA+2:]).find("12") != -1)):
    print("Yes")
else:
    print("No")
