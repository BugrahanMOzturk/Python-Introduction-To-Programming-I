print("Please enter feeding map as a list:")
harita = input()
h1 = harita.replace("[" , " ")
h2 = h1.replace("]" , " ")
h3 = h2.strip()
h4 = h3.replace("'" , "")
h5 = h4.split(" ,  ")
gor1 = h4.replace(" ,  " , "---")
gor2 = gor1.replace(" " , " ")
gor3 = gor2.replace("," , "")
Show_map = gor3.replace("---" , "\n") #Harita görünümü
Map_list = [] #Haritanın liste hali
for i in h5:
    i = i.split(", ")
    Map_list.append(i)
for s in range(len(Map_list)):
    if "*" in Map_list[s]:
        row = s #Tavşanın satırı
        for j in range(0 , len(Map_list[s])):
            if Map_list[s][j] == "*":
                columns = j #Tavşanın sütunu"""
print("Please enter direction of movements as a list:")
yonler = input()
yonler1 = yonler.replace("[" , "")
yonler2 = yonler1.replace("]" , "")
yonler3 = yonler2.replace("'" , "")
yonler4 = yonler3.replace(", " , "")
Movements_list = yonler3.split(", ")#yönler liste hali
point = 0
breaker = 0
print("Your board is:")
print(Show_map)
for k in range(0 , len(Movements_list)):
    if Movements_list[k] == "U":
        if row != 0:
            if Map_list[row - 1][columns] == "W":
                continue
            elif Map_list[row - 1][columns] == "C":
                point += 10
                Map_list[row - 1][columns] = "*"
                Map_list[row][columns] = "X"
                row -= 1
            elif Map_list[row - 1][columns] == "A":
                point += 5
                Map_list[row - 1][columns] = "*"
                Map_list[row][columns] = "X"
                row -= 1
            elif Map_list[row - 1][columns] == "M":
                point -= 5
                Map_list[row - 1][columns] = "*"
                Map_list[row][columns] = "X"
                row -= 1
            elif Map_list[row - 1][columns] == "X":
                Map_list[row - 1][columns] = "*"
                Map_list[row][columns] = "X"
                row -= 1
            elif Map_list[row - 1][columns] == "P":
                Map_list[row - 1][columns] = "*"
                Map_list[row][columns] = "X"
                break
            else:
                continue
        else:
            continue
    elif Movements_list[k] == "D":
        if Map_list[row] != Map_list[-1]:
            if Map_list[row + 1][columns] == "W":
                continue
            elif Map_list[row + 1][columns] == "C":
                point += 10
                Map_list[row + 1][columns] = "*"
                Map_list[row][columns] = "X"
                row += 1
            elif Map_list[row + 1][columns] == "A":
                point += 5
                Map_list[row + 1][columns] = "*"
                Map_list[row][columns] = "X"
                row += 1
            elif Map_list[row + 1][columns] == "M":
                point -= 5
                Map_list[row + 1][columns] = "*"
                Map_list[row][columns] = "X"
                row += 1
            elif Map_list[row + 1][columns] == "X":
                Map_list[row + 1][columns] = "*"
                Map_list[row][columns] = "X"
                row += 1
            elif Map_list[row + 1][columns] == "P":
                Map_list[row + 1][columns] = "*"
                Map_list[row][columns] = "X"
                break
            else:
                continue
        else:
            continue
    elif Movements_list[k] == "L":
        if columns != 0:
            if Map_list[row][columns - 1] == "W":
                continue
            elif Map_list[row][columns - 1] == "C":
                point += 10
                Map_list[row][columns - 1] = "*"
                Map_list[row][columns] = "X"
                columns -= 1
            elif Map_list[row][columns - 1] == "A":
                point += 5
                Map_list[row][columns - 1] = "*"
                Map_list[row][columns] = "X"
                columns -= 1
            elif Map_list[row][columns - 1] == "M":
                point -= 5
                Map_list[row][columns - 1] = "*"
                Map_list[row][columns] = "X"
                columns -= 1
            elif Map_list[row][columns - 1] == "X":
                Map_list[row][columns - 1] = "*"
                Map_list[row][columns] = "X"
                columns -= 1
            elif Map_list[row][columns - 1] == "P":
                Map_list[row][columns - 1] = "*"
                Map_list[row][columns] = "X"
                break
            else:
                continue
        else:
            continue
    elif Movements_list[k] == "R":
        if Map_list[row][columns] != Map_list[row][-1]:
            if Map_list[row][columns + 1] == "W":
                continue
            elif Map_list[row][columns + 1] == "C":
                point += 10
                Map_list[row][columns + 1] = "*"
                Map_list[row][columns] = "X"
                columns += 1
            elif Map_list[row][columns + 1] == "A":
                point += 5
                Map_list[row][columns + 1] = "*"
                Map_list[row][columns] = "X"
                columns += 1
            elif Map_list[row][columns + 1] == "M":
                point -= 5
                Map_list[row][columns + 1] = "*"
                Map_list[row][columns] = "X"
                columns += 1
            elif Map_list[row][columns + 1] == "X":
                Map_list[row][columns + 1] = "*"
                Map_list[row][columns] = "X"
                columns += 1
            elif Map_list[row][columns + 1] == "P":
                Map_list[row][columns + 1] = "*"
                Map_list[row][columns] = "X"
                break
            else:
                break
        else:
            continue
sh = str(Map_list)
sh2 = sh.replace("[" , " ")
sh3 = sh2.replace("]" , " ")
sh4 = sh3.replace("'" , "")
sh5 = sh4.replace(" ,  " , "---")
sh6 = sh5.replace("," , "")
sh7 = sh6.strip()
Last_map = sh7.replace("---" , "\n")
print("Your output should be like this:")
print(Last_map)
print("Your score is : {}".format(point))

