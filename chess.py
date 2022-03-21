import sys
main_board = [[44 * "-"], ["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2"], ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
         [2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " "], [2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " "],
         [2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " "], [2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " "],
         ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"], ["r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"], [44 * "-"]]
words_board = [[44 * "-"], ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"], ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
               ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"], ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"], ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
               ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"], ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"], ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]]
def initalize():
    global main_board
    main_board = [[44 * "-"], ["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2"], ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
         [2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " "], [2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " "],
         [2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " "], [2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " ", 2 * " "],
         ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"], ["r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"], [44 * "-"]]
def showboard():
    show_board = str(main_board).replace("], ", "\n").replace("[", "").replace("'", "").replace(44 * "-", 23 * "-").replace(",", "").replace("]", "")#Board görünümü
    return (show_board)
def find(piece):#taşı bulmak için sadece index olarak
    for i in range(1, 9):
        if piece in main_board[i]:
            first_index = i
            for j in range(8):
                if main_board[i][j] == piece:
                    second_index = j
    return first_index, second_index


def findlocation(location):#movement da location indexini bulmak için
    for i in range(1, 9):
        if location in words_board[i]:
            first_index = i
            for j in range(8):
                if words_board[i][j] == location:
                    second_index = j
    return first_index, second_index

temp_show = []

def showmoves(piece):
    temp_show.clear()
    if piece[0] == "P":  #Siyahın piyonu
        for i in range(1, 9):
            if int(piece[1]) == i:
                first, second = find(piece)
                if main_board[first + 1][second] == "  ":
                    temp_show.append(words_board[first + 1][second])
                elif main_board[first + 1][second][0].islower():
                    temp_show.append(words_board[first + 1][second])
    elif piece[0] == "p": #Beyazın piyonu
        for i in range(1, 9):
            if int(piece[1]) == i:
                first, second = find(piece)
                if main_board[first - 1][second] == "  ":
                    temp_show.append(words_board[first - 1][second])
                elif main_board[first - 1][second][0].isupper():
                    temp_show.append(words_board[first - 1][second])
    elif piece[0] == "R": #Siyahın Kalesi
        for i in range(1, 3):
            if int(piece[1]) == i:
                first, second = find(piece)
                for i in range(first, 8):#second sabit aşağı inmesi için
                    if main_board[first + 1][second][0].isupper():
                        break
                    elif main_board[first + 1][second] == "  ":
                        temp_show.append(words_board[first + 1][second])
                        first += 1
                    elif main_board[first + 1][second][0].islower():
                        temp_show.append(words_board[first + 1][second])
                        break
                first, second = find(piece)
                for i in range(8, first, -1):#second sabit yukarı çıkması için
                    if first == 1:
                        break
                    if main_board[first - 1][second][0].isupper():
                        break
                    elif main_board[first - 1][second] == "  ":
                        temp_show.append(words_board[first - 1][second])
                        first -= 1
                    elif main_board[first - 1][second][0].islower():
                        temp_show.append(words_board[first - 1][second])
                        break
                first, second = find(piece)
                for i in range(second, 8):#first sabit sağa gitmesi için
                    if second == 7:
                        break
                    if main_board[first][second + 1] == "  ":
                        temp_show.append(words_board[first][second + 1])
                        second += 1
                    elif main_board[first][second + 1][0].isupper():
                        break
                    elif main_board[first][second + 1].islower():
                        temp_show.append(words_board[first][second + 1])
                        break
                first, second = find(piece)
                for i in range(8, second, -1): #first sabit sola gitmesi için
                    if second == 0:
                        break
                    if main_board[first][second - 1] == "  ":
                        temp_show.append(words_board[first][second - 1])
                        second -= 1
                    elif main_board[first][second - 1][0].isupper():
                        break
                    elif main_board[first][second - 1].islower():
                        temp_show.append(words_board[first][second - 1])
                        break
    elif piece[0] == "r": #Beyazın kalesi
        for i in range(1, 3):
            if int(piece[1]) == i:
                first, second = find(piece)
                for i in range(first, 8):#second sabit aşağı inmesi için
                    if main_board[first + 1][second][0].islower():
                        break
                    elif main_board[first + 1][second] == "  ":
                        temp_show.append(words_board[first + 1][second])
                        first += 1
                    elif main_board[first + 1][second][0].isupper():
                        temp_show.append(words_board[first + 1][second])
                        break
                first, second = find(piece)
                for i in range(8, first, -1):#second sabit yukarı çıkması için
                    if first == 1:
                        break
                    if main_board[first - 1][second][0].islower():
                        break
                    elif main_board[first - 1][second] == "  ":
                        temp_show.append(words_board[first - 1][second])
                        first -= 1
                    elif main_board[first - 1][second][0].isupper():
                        temp_show.append(words_board[first - 1][second])
                        break
                first, second = find(piece)
                for i in range(second, 8):#first sabit sağa gitmesi için
                    if second == 7:
                        break
                    if main_board[first][second + 1] == "  ":
                        temp_show.append(words_board[first][second + 1])
                        second += 1
                    elif main_board[first][second + 1][0].islower():
                        break
                    elif main_board[first][second + 1].isupper():
                        temp_show.append(words_board[first][second + 1])
                        break
                first, second = find(piece)
                for i in range(8, second, -1): #first sabit sola gitmesi için
                    if second == 0:
                        break
                    if main_board[first][second - 1] == "  ":
                        temp_show.append(words_board[first][second - 1])
                        second -= 1
                    elif main_board[first][second - 1][0].islower():
                        break
                    elif main_board[first][second - 1].isupper():
                        temp_show.append(words_board[first][second - 1])
                        break
    elif piece[0] == "N": #Siyah At
        for i in range(1, 3):
            if int(piece[1]) == i:
                first, second = find(piece)
                if first < 7:#2 aşağı
                    if second < 7:#1sağa
                        if main_board[first + 2][second + 1] == "  ":
                            temp_show.append(words_board[first + 2][second + 1])
                        if main_board[first + 2][second + 1][0].islower():
                            temp_show.append(words_board[first + 2][second + 1])
                    if second > 0:#1sola
                        if main_board[first + 2][second - 1] == "  ":
                            temp_show.append(words_board[first + 2][second - 1])
                        if main_board[first + 2][second - 1][0].islower():
                            temp_show.append(words_board[first + 2][second - 1])
                if first > 2:#2 yukarı
                    if second < 7:#1 sağa
                        if main_board[first - 2][second + 1] == "  ":
                            temp_show.append(words_board[first - 2][second + 1])
                        if main_board[first - 2][second + 1][0].islower():
                            temp_show.append(words_board[first - 2][second + 1])
                    if second > 0:#1 sola
                        if main_board[first - 2][second - 1] == "  ":
                            temp_show.append(words_board[first - 2][second - 1])
                        if main_board[first - 2][second - 1][0].islower():
                            temp_show.append(words_board[first - 2][second - 1])
                if second < 6:#2 sağa
                    if first > 1:#1 yukarı
                        if main_board[first - 1][second + 2] == "  ":
                            temp_show.append(words_board[first - 1][second + 2])
                        if main_board[first - 1][second + 2][0].islower():
                            temp_show.append(words_board[first - 1][second + 2])
                    if first < 8:#1 aşağı
                        if main_board[first + 1][second + 2] == "  ":
                            temp_show.append(words_board[first + 1][second + 2])
                        if main_board[first + 1][second + 2][0].islower():
                            temp_show.append(words_board[first + 1][second + 2])
                if second > 1:#2 sola
                    if first > 1:#1 yukarı
                        if main_board[first - 1][second - 2] == "  ":
                            temp_show.append(words_board[first - 1][second - 2])
                        if main_board[first - 1][second - 2][0].islower():
                            temp_show.append(words_board[first - 1][second - 2])
                    if first < 8:#1 aşağı
                        if main_board[first + 1][second - 2] == "  ":
                            temp_show.append(words_board[first + 1][second - 2])
                        if main_board[first + 1][second - 2][0].islower():
                            temp_show.append(words_board[first + 1][second - 2])
                if first < 8 and second < 7:
                    if main_board[first + 1][second + 1] == "  ":
                        temp_show.append(words_board[first + 1][second + 1])
                if first < 8 and second > 0:
                    if main_board[first + 1][second - 1] == "  ":
                        temp_show.append(words_board[first + 1][second - 1])
                if first > 1 and second < 7:
                    if main_board[first - 1][second + 1] == "  ":
                        temp_show.append(words_board[first - 1][second + 1])
                if first > 1 and second > 0:
                    if main_board[first - 1][second - 1] == "  ":
                        temp_show.append(words_board[first - 1][second - 1])
    elif piece[0] == "n":#Beyaz AT
        for i in range(1, 3):
            if int(piece[1]) == i:
                first, second = find(piece)
                if first < 7:#2 aşağı
                    if second < 7:#1sağa
                        if main_board[first + 2][second + 1] == "  ":
                            temp_show.append(words_board[first + 2][second + 1])
                        if main_board[first + 2][second + 1][0].isupper():
                            temp_show.append(words_board[first + 2][second + 1])
                    if second > 0:#1sola
                        if main_board[first + 2][second - 1] == "  ":
                            temp_show.append(words_board[first + 2][second - 1])
                        if main_board[first + 2][second - 1][0].isupper():
                            temp_show.append(words_board[first + 2][second - 1])
                if first > 2:#2 yukarı
                    if second < 7:#1 sağa
                        if main_board[first - 2][second + 1] == "  ":
                            temp_show.append(words_board[first - 2][second + 1])
                        if main_board[first - 2][second + 1][0].isupper():
                            temp_show.append(words_board[first - 2][second + 1])
                    if second > 0:#1 sola
                        if main_board[first - 2][second - 1] == "  ":
                            temp_show.append(words_board[first - 2][second - 1])
                        if main_board[first - 2][second - 1][0].isupper():
                            temp_show.append(words_board[first - 2][second - 1])
                if second < 6:#2 sağa
                    if first > 1:#1 yukarı
                        if main_board[first - 1][second + 2] == "  ":
                            temp_show.append(words_board[first - 1][second + 2])
                        if main_board[first - 1][second + 2][0].isupper():
                            temp_show.append(words_board[first - 1][second + 2])
                    if first < 8:#1 aşağı
                        if main_board[first + 1][second + 2] == "  ":
                            temp_show.append(words_board[first + 1][second + 2])
                        if main_board[first + 1][second + 2][0].isupper():
                            temp_show.append(words_board[first + 1][second + 2])
                if second > 1:#2 sola
                    if first > 1:#1 yukarı
                        if main_board[first - 1][second - 2] == "  ":
                            temp_show.append(words_board[first - 1][second - 2])
                        if main_board[first - 1][second - 2][0].isupper():
                            temp_show.append(words_board[first - 1][second - 2])
                    if first < 8:#1 aşağı
                        if main_board[first + 1][second - 2] == "  ":
                            temp_show.append(words_board[first + 1][second - 2])
                        if main_board[first + 1][second - 2][0].isupper():
                            temp_show.append(words_board[first + 1][second - 2])
                if first < 8 and second < 7:
                    if main_board[first + 1][second + 1] == "  ":
                        temp_show.append(words_board[first + 1][second + 1])
                if first < 8 and second > 0:
                    if main_board[first + 1][second - 1] == "  ":
                        temp_show.append(words_board[first + 1][second - 1])
                if first > 1 and second < 7:
                    if main_board[first - 1][second + 1] == "  ":
                        temp_show.append(words_board[first - 1][second + 1])
                if first > 1 and second > 0:
                    if main_board[first - 1][second - 1] == "  ":
                        temp_show.append(words_board[first - 1][second - 1])
    elif piece[0] == "B":#Siyah fil
        for i in range(1, 3):
            if int(piece[1]) == i:
                first, second = find(piece)
                for i in range(8):#Aşağı sağa
                    if first == 8:
                        break
                    elif second == 7:
                        break
                    if main_board[first + 1][second + 1][0].isupper():
                        break
                    elif main_board[first + 1][second + 1] == "  ":
                        temp_show.append(words_board[first + 1][second + 1])
                        first += 1
                        second += 1
                    elif main_board[first + 1][second + 1][0].islower():
                        temp_show.append(words_board[first + 1][second + 1])
                        break
                first, second = find(piece)
                for i in range(8):#aşağı sola
                    if first == 8:
                        break
                    elif second == 0:
                        break
                    if main_board[first + 1][second - 1][0].isupper():
                        break
                    elif main_board[first + 1][second - 1] == "  ":
                        temp_show.append(words_board[first + 1][second - 1])
                        first += 1
                        second -= 1
                    elif main_board[first + 1][second - 1][0].islower():
                        temp_show.append(words_board[first + 1][second - 1])
                        break
    elif piece[0] == "b":#beyaz fil
        for i in range(1, 3):
            if int(piece[1]) == i:
                first, second = find(piece)
                for i in range(8):#yukarı sola
                    if first == 1:
                        break
                    elif second == 0:
                        break
                    if main_board[first - 1][second - 1][0].islower():
                        break
                    elif main_board[first - 1][second - 1] == "  ":
                        temp_show.append(words_board[first - 1][second - 1])
                        first -= 1
                        second -= 1
                    elif main_board[first - 1][second - 1][0].isupper():
                        temp_show.append(words_board[first - 1][second - 1])
                        break
                first, second = find(piece)
                for i in range(8):#yukarı sağa
                    if first == 1:
                        break
                    elif second == 7:
                        break
                    if main_board[first - 1][second + 1][0].islower():
                        break
                    elif main_board[first - 1][second + 1] == "  ":
                        temp_show.append(words_board[first - 1][second + 1])
                        first -= 1
                        second += 1
                    elif main_board[first - 1][second + 1][0].isupper():
                        temp_show.append(words_board[first - 1][second + 1])
                        break
    elif piece == "QU":
        first, second = find(piece)#Çapraz Mekanikler
        for i in range(8):#aşağı sağa
            if first == 8:
                break
            elif second == 7:
                break
            if main_board[first + 1][second + 1][0].isupper():
                break
            elif main_board[first + 1][second + 1] == "  ":
                temp_show.append(words_board[first + 1][second + 1])
                first += 1
                second += 1
            elif main_board[first + 1][second + 1][0].islower():
                temp_show.append(words_board[first + 1][second + 1])
                break
        first, second = find(piece)
        for i in range(8):#aşağı sola
            if first == 8:
                break
            elif second == 0:
                break
            if main_board[first + 1][second - 1][0].isupper():
                break
            elif main_board[first + 1][second - 1] == "  ":
                temp_show.append(words_board[first + 1][second - 1])
                first += 1
                second -= 1
            elif main_board[first + 1][second - 1][0].islower():
                temp_show.append(words_board[first + 1][second - 1])
                break
        first, second = find(piece)
        for i in range(8):#yukarı sola
            if first == 1:
                break
            elif second == 0:
                break
            if main_board[first - 1][second - 1][0].isupper():
                break
            elif main_board[first - 1][second - 1] == "  ":
                temp_show.append(words_board[first - 1][second - 1])
                first -= 1
                second -= 1
            elif main_board[first - 1][second - 1][0].islower():
                temp_show.append(words_board[first - 1][second - 1])
                break
        first, second = find(piece)
        for i in range(8):#yukarı sağa
            if first == 1:
                break
            elif second == 7:
                break
            if main_board[first - 1][second + 1][0].isupper():
                break
            elif main_board[first - 1][second + 1] == "  ":
                temp_show.append(words_board[first - 1][second + 1])
                first -= 1
                second += 1
            elif main_board[first - 1][second + 1][0].islower():
                temp_show.append(words_board[first - 1][second + 1])
                break
        first, second = find(piece)#düz mekanikler
        for i in range(8):#yukarı
            if first == 1:
                break
            if main_board[first - 1][second][0].isupper():
                break
            elif main_board[first - 1][second] == "  ":
                temp_show.append(words_board[first - 1][second])
                first -= 1
            elif main_board[first - 1][second][0].islower():
                temp_show.append(words_board[first - 1][second])
                break
        first, second = find(piece)
        for i in range(8):#aşağı
            if first == 8:
                break
            if main_board[first + 1][second][0].isupper():
                break
            elif main_board[first + 1][second] == "  ":
                temp_show.append(words_board[first + 1][second])
                first += 1
            elif main_board[first + 1][second][0].islower():
                temp_show.append(words_board[first + 1][second])
                break
        first, second = find(piece)
        for i in range(8):#sağa
            if second == 7:
                break
            if main_board[first][second + 1][0].isupper():
                break
            elif main_board[first][second + 1] == "  ":
                temp_show.append(words_board[first][second + 1])
                second += 1
            elif main_board[first][second + 1][0].islower():
                temp_show.append(words_board[first][second + 1])
                break
        first, second = find(piece)
        for i in range(8):#sola
            if second == 0:
                break
            if main_board[first][second - 1][0].isupper():
                break
            elif main_board[first][second - 1] == "  ":
                temp_show.append(words_board[first][second - 1])
                second -= 1
            elif main_board[first][second + 1][0].islower():
                temp_show.append(words_board[first][second - 1])
                break
    elif piece == "qu":
        first, second = find(piece)#Çapraz Mekanikler
        for i in range(8):#aşağı sağa
            if first == 8:
                break
            elif second == 7:
                break
            if main_board[first + 1][second + 1][0].islower():
                break
            elif main_board[first + 1][second + 1] == "  ":
                temp_show.append(words_board[first + 1][second + 1])
                first += 1
                second += 1
            elif main_board[first + 1][second + 1][0].isupper():
                temp_show.append(words_board[first + 1][second + 1])
                break
        first, second = find(piece)
        for i in range(8):#aşağı sola
            if first == 8:
                break
            elif second == 0:
                break
            if main_board[first + 1][second - 1][0].islower():
                break
            elif main_board[first + 1][second - 1] == "  ":
                temp_show.append(words_board[first + 1][second - 1])
                first += 1
                second -= 1
            elif main_board[first + 1][second - 1][0].isupper():
                temp_show.append(words_board[first + 1][second - 1])
                break
        first, second = find(piece)
        for i in range(8):#yukarı sola
            if first == 1:
                break
            elif second == 0:
                break
            if main_board[first - 1][second - 1][0].islower():
                break
            elif main_board[first - 1][second - 1] == "  ":
                temp_show.append(words_board[first - 1][second - 1])
                first -= 1
                second -= 1
            elif main_board[first - 1][second - 1][0].isupper():
                temp_show.append(words_board[first - 1][second - 1])
                break
        first, second = find(piece)
        for i in range(8):#yukarı sağa
            if first == 1:
                break
            elif second == 7:
                break
            if main_board[first - 1][second + 1][0].islower():
                break
            elif main_board[first - 1][second + 1] == "  ":
                temp_show.append(words_board[first - 1][second + 1])
                first -= 1
                second += 1
            elif main_board[first - 1][second + 1][0].isupper():
                temp_show.append(words_board[first - 1][second + 1])
                break
        first, second = find(piece)#düz mekanikler
        for i in range(8):#yukarı
            if first == 1:
                break
            if main_board[first - 1][second][0].islower():
                break
            elif main_board[first - 1][second] == "  ":
                temp_show.append(words_board[first - 1][second])
                first -= 1
            elif main_board[first - 1][second][0].isupper():
                temp_show.append(words_board[first - 1][second])
                break
        first, second = find(piece)
        for i in range(8):#aşağı
            if first == 8:
                break
            if main_board[first + 1][second][0].islower():
                break
            elif main_board[first + 1][second] == "  ":
                temp_show.append(words_board[first + 1][second])
                first += 1
            elif main_board[first + 1][second][0].isupper():
                temp_show.append(words_board[first + 1][second])
                break
        first, second = find(piece)
        for i in range(8):#sağa
            if second == 7:
                break
            if main_board[first][second + 1][0].islower():
                break
            elif main_board[first][second + 1] == "  ":
                temp_show.append(words_board[first][second + 1])
                second += 1
            elif main_board[first][second + 1][0].isupper():
                temp_show.append(words_board[first][second + 1])
                break
        first, second = find(piece)
        for i in range(8):#sola
            if second == 0:
                break
            if main_board[first][second - 1][0].islower():
                break
            elif main_board[first][second - 1] == "  ":
                temp_show.append(words_board[first][second - 1])
                second -= 1
            elif main_board[first][second + 1][0].isupper():
                temp_show.append(words_board[first][second - 1])
                break
    elif piece == "KI":
        first, second = find(piece)
        if first != 1:#yukarı
            if main_board[first - 1][second] == "  ":
                temp_show.append(words_board[first - 1][second])
            elif main_board[first - 1][second][0].islower():
                temp_show.append(words_board[first - 1][second])
        if first != 8:#aşağı
            if main_board[first + 1][second] == "  ":
                temp_show.append(words_board[first + 1][second])
            elif main_board[first + 1][second][0].islower():
                temp_show.append(words_board[first + 1][second])
        if second != 7:#sağa
            if main_board[first][second + 1] == "  ":
                temp_show.append(words_board[first][second + 1])
            elif main_board[first][second + 1][0].islower():
                temp_show.append(words_board[first][second + 1])
        if second != 0:#sola
            if main_board[first][second - 1] == "  ":
                temp_show.append(words_board[first][second - 1])
            elif main_board[first][second - 1][0].islower():
                temp_show.append(words_board[first][second - 1])
        if first != 1 and second != 0:#yukarı sol
            if main_board[first - 1][second - 1] == "  ":
                temp_show.append(words_board[first - 1][second - 1])
            elif main_board[first - 1][second - 1][0].islower():
                temp_show.append(words_board[first - 1][second - 1])
        if first != 1 and second != 7:#yukarı sağ
            if main_board[first - 1][second + 1] == "  ":
                temp_show.append(words_board[first - 1][second + 1])
            elif main_board[first - 1][second + 1][0].islower():
                temp_show.append(words_board[first - 1][second + 1])
        if first != 8 and second != 0:#aşağı sol
            if main_board[first + 1][second - 1] == "  ":
                temp_show.append(words_board[first + 1][second - 1])
            elif main_board[first + 1][second - 1][0].islower():
                temp_show.append(words_board[first + 1][second - 1])
        if first != 8 and second != 7:#aşağı sağ
            if main_board[first + 1][second + 1] == "  ":
                temp_show.append(words_board[first + 1][second + 1])
            elif main_board[first + 1][second + 1][0].islower():
                temp_show.append(words_board[first + 1][second + 1])
    elif piece == "ki":
        first, second = find(piece)
        if first != 1:#yukarı
            if main_board[first - 1][second] == "  ":
                temp_show.append(words_board[first - 1][second])
            elif main_board[first - 1][second][0].isupper():
                temp_show.append(words_board[first - 1][second])
        if first != 8:#aşağı
            if main_board[first + 1][second] == "  ":
                temp_show.append(words_board[first + 1][second])
            elif main_board[first + 1][second][0].isupper():
                temp_show.append(words_board[first + 1][second])
        if second != 7:#sağa
            if main_board[first][second + 1] == "  ":
                temp_show.append(words_board[first][second + 1])
            elif main_board[first][second + 1][0].isupper():
                temp_show.append(words_board[first][second + 1])
        if second != 0:#sola
            if main_board[first][second - 1] == "  ":
                temp_show.append(words_board[first][second - 1])
            elif main_board[first][second - 1][0].isupper():
                temp_show.append(words_board[first][second - 1])
        if first != 1 and second != 0:#yukarı sol
            if main_board[first - 1][second - 1] == "  ":
                temp_show.append(words_board[first - 1][second - 1])
            elif main_board[first - 1][second - 1][0].isupper():
                temp_show.append(words_board[first - 1][second - 1])
        if first != 1 and second != 7:#yukarı sağ
            if main_board[first - 1][second + 1] == "  ":
                temp_show.append(words_board[first - 1][second + 1])
            elif main_board[first - 1][second + 1][0].isupper():
                temp_show.append(words_board[first - 1][second + 1])
        if first != 8 and second != 0:#aşağı sol
            if main_board[first + 1][second - 1] == "  ":
                temp_show.append(words_board[first + 1][second - 1])
            elif main_board[first + 1][second - 1][0].isupper():
                temp_show.append(words_board[first + 1][second - 1])
        if first != 8 and second != 7:#aşağı sağ
            if main_board[first + 1][second + 1] == "  ":
                temp_show.append(words_board[first + 1][second + 1])
            elif main_board[first + 1][second + 1][0].isupper():
                temp_show.append(words_board[first + 1][second + 1])
    first, second = find("KI")
    if words_board[first][second] in temp_show:
        temp_show.remove(words_board[first][second])
    first, second = find("ki")
    if words_board[first][second] in temp_show:
        temp_show.remove(words_board[first][second])
    temp_show.sort()
    return str(temp_show).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
def move(piece, location):
    firstpi, secondpi = find(piece)
    firstlo, secondlo = findlocation(location)
    showmoves(piece)
    if location in temp_show:
        main_board[firstpi][secondpi] = "  "
        main_board[firstlo][secondlo] = piece
        return "OK"
    else:
        return "FAILED"
inputFile = open(sys.argv[1], "r")
commands = [line.split() for line in inputFile.readlines()]
for i in range(len(commands)):
    if commands[i][0] == "move":
        print("> " + str(commands[i]).replace("[", "").replace("]", "").replace("'", "").replace(",", ""))
        print(move(commands[i][1], commands[i][2]))
    elif commands[i][0] == "print":
        print("> print")
        print(showboard())
    elif commands[i][0] == "showmoves":
        showmoves(commands[i][1])
        if temp_show != []:
            print("> showmoves {}".format(commands[i][1]))
            print(showmoves(commands[i][1]))
        else:
            print("> showmoves {}".format(commands[i][1]))
            print("FAILED")
    elif commands[i][0] == "initialize":
        print("> initialize")
        print("OK")
        initalize()
        print(showboard())
    elif commands[i][0] == "exit":
        print("> exit")
        exit()
inputFile.close()
