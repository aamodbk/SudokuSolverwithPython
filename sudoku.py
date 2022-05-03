from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time

class Sudoku:
    def __init__(self):
        self.sudoku = [[[0 for i in range(10)] for k in range(9)] for z in range(9)]
        self.solve = False
        self.changes = 0
        self.freq_table = [[0 for i in range(9)] for k in range(9)]
        self.freq = [0 for i in range(81)]
        self.row = [0 for i in range(81)]
        self.column = [0 for i in range(81)]
        self.number_list = []
        self.unsolved = 0

    def Accept(self):
        for i in range(9):
            print("Enter Sudoku line", i+1)
            inp = str(input())
            acc = 0
            for k in inp:
                if k != ' ':
                    self.sudoku[i][acc][0] = int(k)
                acc = acc + 1
        for i in range(9):
            for k in range(9):
                if(self.sudoku[i][k][0] == 0):
                    for z in range(1, 10):
                        self.sudoku[i][k][z] = z

    def Display(self):
        for i in range(9):
            for k in range(9):
                if k <= 7:
                    if self.sudoku[i][k][0] != 0:
                        print("", self.sudoku[i][k][0], "|", end = "")
                    else:
                        print("   |", end = "")
                elif k == 8:
                    if self.sudoku[i][k][0] != 0:
                        print("", self.sudoku[i][k][0], " ", end = "")
                    else:
                        print("   ", end = "")
            print()
            if i <= 7:
                for k in range(9):
                    if(k <= 7):
                        print("___|", end = "")
                    else:
                        print("___", end = "")
            else:
                for k in range(9):
                    if k <= 7:
                        print("   |", end = "")
                    else:
                        print("   ", end = "")
            print()

    def Check(self):
        flag = True
        f = False
        for i in range(9):
            for k in range(9):
                if(self.sudoku[i][k][0] == 0):
                    flag = False
                    f = True
                    break
            if f == True:
                break
        self.solve = flag

    def Primitive_Elimination(self):
        for i in range(9):
            for k in range(9):
                if self.sudoku[i][k][0] != 0:
                    S.PEliminate(self.sudoku[i][k][0], i, k)

    def PEliminate(self, n, r, c):
        #Row elimination:-
        for i in range(9):
            if self.sudoku[r][i][0] == 0:
                self.sudoku[r][i][n] = 0
        #Column elimination:-
        for i in range(9):
            if self.sudoku[i][c][0] == 0:
                self.sudoku[i][c][n] = 0
        #Box elimination
        if r >= 0 and r <= 2 and c >= 0 and c <= 2:
            for i in range(3):
                for k in range(3):
                    if self.sudoku[i][k][0] == 0:
                        self.sudoku[i][k][n] = 0
        elif r >= 0 and r <= 2 and c >= 3 and c <= 5:
            for i in range(3):
                for k in range(3, 6):
                    if self.sudoku[i][k][0] == 0:
                        self.sudoku[i][k][n] = 0
        elif r >= 0 and r <= 2 and c >= 6 and c <= 8:
            for i in range(3):
                for k in range(6, 9):
                    if self.sudoku[i][k][0] == 0:
                        self.sudoku[i][k][n] = 0
        elif r >= 3 and r <= 5 and c >= 0 and c <= 2:
            for i in range(3, 6):
                for k in range(3):
                    if self.sudoku[i][k][0] == 0:
                        self.sudoku[i][k][n] = 0
        elif r >= 3 and r <= 5 and c >= 3 and c <= 5:
            for i in range(3, 6):
                for k in range(3, 6):
                    if self.sudoku[i][k][0] == 0:
                        self.sudoku[i][k][n] = 0
        elif r >= 3 and r <= 5 and c >= 6 and c <= 8:
            for i in range(3, 6):
                for k in range(6, 9):
                    if self.sudoku[i][k][0] == 0:
                        self.sudoku[i][k][n] = 0
        elif r >= 6 and r <= 8 and c >= 0 and c <= 2:
            for i in range(6, 9):
                for k in range(3):
                    if self.sudoku[i][k][0] == 0:
                        self.sudoku[i][k][n] = 0
        elif r >= 6 and r <= 8 and c >= 2 and c <= 5:
            for i in range(6, 9):
                for k in range(3, 6):
                    if self.sudoku[i][k][0] == 0:
                        self.sudoku[i][k][n] = 0
        elif r >=6 and r <= 8 and c>= 6 and c <= 8:
            for i in range(6, 9):
                for k in range(6, 9):
                    if self.sudoku[i][k][0] == 0:
                        self.sudoku[i][k][n] = 0

    def Primitive_Fill(self):
        S.P1Fill()
        S.PRFill()
        S.PCFill()
        S.PBFill()

    def Fill_Protocol(self, n, r, c):
        self.changes+=1
        for i in range(1, 10):
            self.sudoku[r][c][i] = 0

    def P1Fill(self):
        for i in range(9):
            for k in range(9):
                if self.sudoku[i][k][0] != 0:
                    continue
                else:
                    freq = 0
                    for z in range(1, 10):
                        if self.sudoku[i][k][z] == z:
                            freq+=1
                    if freq == 1:
                        for z in range(1, 10):
                            if self.sudoku[i][k][z] == z:
                                self.sudoku[i][k][0] = z
                                #Single frequency fill
                                S.Fill_Protocol(z, i, k)
                                S.Primitive_Elimination()
                                break
                    
    def PRFill(self):
        freq = 0
        for i in range(9):
            for k in range(1, 10):
                freq = 0
                for z in range(9):
                    if self.sudoku[i][z][0] == 0 and self.sudoku[i][z][k] == k:
                        freq = freq + 1
                if freq == 1:
                    for z in range(9):
                        if self.sudoku[i][z][0] == 0 and self.sudoku[i][z][k] == k:
                            self.sudoku[i][z][0] = k
                            #Row fill
                            S.Fill_Protocol(k, i, z)
                            S.Primitive_Elimination()
                            break

    def PCFill(self):
        freq = 0
        for i in range(9):
            for k in range(1, 10):
                freq = 0
                for z in range(9):
                    if self.sudoku[z][i][0] == 0 and self.sudoku[z][i][k] == k:
                        freq = freq + 1
                if freq == 1:
                    for z in range(9):
                        if self.sudoku[z][i][0] == 0 and self.sudoku[z][i][k] == k:
                            self.sudoku[z][i][0] = k
                            #Column fill
                            S.Fill_Protocol(k, z, i)
                            S.Primitive_Elimination()
                            break

    def PBFill(self):
        freq = 0
        #box 1
        for z in range(1, 10):
            freq = 0
            for i in range(3):
                for k in range(3):
                    if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                        freq = freq + 1
            if freq == 1:
                flag = False
                for i in range(3):
                    for k in range(3):
                        if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                            self.sudoku[i][k][0] = z
                            #Box fill
                            S.Fill_Protocol(z, i, k)
                            S.Primitive_Elimination()
                            flag = True
                            break
                    if flag == True:
                        break
        #box 2
        for z in range(1, 10):
            freq = 0
            for i in range(3):
                for k in range(3, 6):
                    if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                        freq = freq + 1
            if freq == 1:
                flag = False
                for i in range(3):
                    for k in range(3, 6):
                        if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                            self.sudoku[i][k][0] = z
                            #Box fill
                            S.Fill_Protocol(z, i, k)
                            S.Primitive_Elimination()
                            flag = True
                            break
                    if flag == True:
                        break
        #box 3
        for z in range(1, 10):
            freq = 0
            for i in range(3):
                for k in range(6, 9):
                    if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                        freq = freq + 1
            if freq == 1:      
                flag = False
                for i in range(3):
                    for k in range(6, 9):
                        if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                            self.sudoku[i][k][0] = z
                            #Box fill
                            S.Fill_Protocol(z, i, k)
                            S.Primitive_Elimination()
                            flag = True
                            break
                    if flag == True:
                        break
        #box 4
        for z in range(1, 10):
            freq = 0
            for i in range(3, 6):
                for k in range(3):
                    if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                        freq = freq + 1
            if freq == 1:
                flag = False
                for i in range(3, 6):
                    for k in range(3):
                        if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                            self.sudoku[i][k][0] = z
                            #Box fill
                            S.Fill_Protocol(z, i, k)
                            S.Primitive_Elimination()
                            flag = True
                            break
                    if flag == True:
                        break
        #box 5
        for z in range(1, 10):
            freq = 0
            for i in range(3, 6):
                for k in range(3, 6):
                    if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                        freq = freq + 1
            if freq == 1:      
                flag = False
                for i in range(3, 6):
                    for k in range(3, 6):
                        if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                            self.sudoku[i][k][0] = z
                            #Box fill
                            S.Fill_Protocol(z, i, k)
                            S.Primitive_Elimination()
                            flag = True
                            break
                    if flag == True:
                        break
        #box 6
        for z in range(1, 10):
            freq = 0
            for i in range(3, 6):
                for k in range(6, 9):
                    if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                        freq = freq + 1
            if freq == 1:
                flag = False
                for i in range(3, 6):
                    for k in range(6, 9):
                        if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                            self.sudoku[i][k][0] = z
                            #Box fill
                            S.Fill_Protocol(z, i, k)
                            S.Primitive_Elimination()
                            flag = True
                            break
                    if flag == True:
                        break
        #box 7
        for z in range(1, 10):
            freq = 0
            for i in range(6, 9):
                for k in range(3):
                    if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                        freq = freq + 1
            if freq == 1:
                flag = False
                for i in range(6, 9):
                    for k in range(3):
                        if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                            self.sudoku[i][k][0] = z
                            #Box fill
                            S.Fill_Protocol(z, i, k)
                            S.Primitive_Elimination()
                            flag = True
                            break
                    if flag == True:
                        break
        #box 8
        for z in range(1, 10):
            freq = 0
            for i in range(6, 9):
                for k in range(3, 6):
                    if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                        freq = freq + 1
            if freq == 1:
                flag = False
                for i in range(6, 9):
                    for k in range(3, 6):
                        if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                            self.sudoku[i][k][0] = z
                            #Box fill
                            S.Fill_Protocol(z, i, k)
                            S.Primitive_Elimination()
                            flag = True
                            break
                    if flag == True:
                        break
        #box 9
        for z in range(1, 10):
            freq = 0
            for i in range(6, 9):
                for k in range(6, 9):
                    if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                        freq = freq + 1
            if freq == 1:
                flag = False
                for i in range(6, 9):
                    for k in range(6, 9):
                        if self.sudoku[i][k][0] == 0 and self.sudoku[i][k][z] == z:
                            self.sudoku[i][k][0] = z
                            #Box fill
                            S.Fill_Protocol(z, i, k)
                            S.Primitive_Elimination()
                            flag = True
                            break
                    if flag == True:
                        break

    def Valid_Sudoku(self):
        flag = True
        for i in range(1, 10):
            #row check
            for k in range(9):
                freq = 0
                for z in range(9):
                    if self.sudoku[k][z][0] == i:
                        freq+=1
                if freq > 1:
                    flag = False
                    return flag
            #column check
            for k in range(9):
                freq = 0
                for z in range(9):
                    if self.sudoku[z][k][0] == i:
                        freq+=1
                if freq > 1:
                    flag = False
                    return flag
            #box check
            #box 1
            freq = 0
            for k in range(3):
                for z in range(3):
                    if self.sudoku[k][z][0] == i:
                        freq+=1
                if freq > 1:
                    flag = False
                    return flag
            #box 2
            freq = 0
            for k in range(3):
                for z in range(3, 6):
                    if self.sudoku[k][z][0] == i:
                        freq+=1
                if freq > 1:
                    flag = False
                    return flag
            #box 3
            freq = 0
            for k in range(3):
                for z in range(6, 9):
                    if self.sudoku[k][z][0] == i:
                        freq+=1
                if freq > 1:
                    flag = False
                    return flag
            #box 4
            freq = 0
            for k in range(3, 6):
                for z in range(3):
                    if self.sudoku[k][z][0] == i:
                        freq+=1
                if freq > 1:
                    flag = False
                    return flag
            #box 5
            freq = 0
            for k in range(3, 6):
                for z in range(3, 6):
                    if self.sudoku[k][z][0] == i:
                        freq+=1
                if freq > 1:
                    flag = False
                    return flag
            #box 6
            freq = 0
            for k in range(3, 6):
                for z in range(6, 9):
                    if self.sudoku[k][z][0] == i:
                        freq+=1
                if freq > 1:
                    flag = False
                    return flag
            #box 7
            freq = 0
            for k in range(6, 9):
                for z in range(3):
                    if self.sudoku[k][z][0] == i:
                        freq+=1
                if freq > 1:
                    flag = False
                    return flag
            #box 8
            freq = 0
            for k in range(6, 9):
                for z in range(3, 6):
                    if self.sudoku[k][z][0] == i:
                        freq+=1
                if freq > 1:
                    flag = False
                    return flag
            #box 9
            freq = 0
            for k in range(6, 9):
                for z in range(6, 9):
                    if self.sudoku[k][z][0] == i:
                        freq+=1
                if freq > 1:
                    flag = False
                    return flag
        return flag

    def Advanced_Step1(self):
        count = 0
        for i in range(9):
            for k in range(9):
                count = 0
                if self.sudoku[i][k][0] == 0:
                    for z in range(1, 10):
                        if self.sudoku[i][k][z] != 0:
                            count+=1
                if count != 0:
                    self.freq_table[i][k] = count
                else:
                    self.freq_table[i][k] = 10
        acc = 0
        for i in range(9):
            for k in range(9):
                self.freq[acc] = self.freq_table[i][k]
                self.row[acc] = i
                self.column[acc] = k
                acc+=1
        for i in range(80):
            for k in range(80-i):
                if self.freq[k] > self.freq[k+1]:
                    swap = self.freq[k]
                    self.freq[k] = self.freq[k+1]
                    self.freq[k+1] = swap
                    swap = self.row[k]
                    self.row[k] = self.row[k+1]
                    self.row[k+1] = swap
                    swap = self.column[k]
                    self.column[k] = self.column[k+1]
                    self.column[k+1] = swap
        for i in range(9):
            for k in range(9):
                if self.sudoku[i][k][0] == 0:
                    self.unsolved+=1
        for i in range(30):
            buff = []
            r = self.row[i]
            c = self.column[i]
            for z in range(1, 10):
                if self.sudoku[r][c][z] != 0:
                    buff.append(z)
            self.number_list.append(buff)

    def Antifill(self, n):
        for i in range(n, 15):
            if self.sudoku[self.row[i]][self.column[i]][0] != 0:
                for z in range(10):
                    self.sudoku[self.row[i]][self.column[i]][z] = self.sudoku3[self.row[i]][self.column[i]][z]

    def Advanced(self):
        S.Advanced_Step1()
        print("unsolved boxes =", self.unsolved)
        if self.unsolved <= 10:
            #lets make 5 guesses
            print("Advanced solving done, 5 assumptions taken")
            sudoku2 = [[[0 for i in range(10)] for k in range(9)] for z in range(9)]
            for i in range(9):
                for k in range(9):
                    for z in range(10):
                        sudoku2[i][k][z] = self.sudoku[i][k][z]
            for a in self.number_list[0]:
                if self.solve == True:
                    break
                for b in self.number_list[1]:
                    if self.solve == True:
                        break
                    for c in self.number_list[2]:
                        if self.solve == True:
                            break
                        for d in self.number_list[3]:
                            if self.solve == True:
                                break
                            for e in self.number_list[4]:
                                self.sudoku[self.row[0]][self.column[0]][0] = a
                                self.sudoku[self.row[1]][self.column[1]][0] = b
                                self.sudoku[self.row[2]][self.column[2]][0] = c
                                self.sudoku[self.row[3]][self.column[3]][0] = d
                                self.sudoku[self.row[4]][self.column[4]][0] = e
                                S.Fill_Protocol(a, self.row[0], self.column[0])
                                S.Fill_Protocol(b, self.row[1], self.column[1])
                                S.Fill_Protocol(c, self.row[2], self.column[2])
                                S.Fill_Protocol(d, self.row[3], self.column[3])
                                S.Fill_Protocol(e, self.row[4], self.column[4])
                                flag = S.Valid_Sudoku()
                                if flag == False:
                                    for i in range(9):
                                        for k in range(9):
                                            for z in range(10):
                                                self.sudoku[i][k][z] = sudoku2[i][k][z]
                                    continue
                                else:
                                    S.Primitive_Elimination()
                                    while(True):
                                        self.changes = 0
                                        S.Primitive_Fill()
                                        if self.changes == 0:
                                            S.Primitive_Fill()
                                            if self.changes == 0:
                                                S.Check()
                                                break
                                    if self.solve == True:
                                        S.Display()
                                        print("Sudoku Solved!!")
                                        break
                                    else:
                                        for i in range(9):
                                            for k in range(9):
                                                for z in range(10):
                                                    self.sudoku[i][k][z] = sudoku2[i][k][z]
        elif self.unsolved <= 20 and self.solve == False:
        #lets make 10 guesses
            print("Advanced solving done, 10 assumptions taken")
            sudoku2 = [[[0 for i in range(10)] for k in range(9)] for z in range(9)]
            for i in range(9):
                for k in range(9):
                    for z in range(10):
                        sudoku2[i][k][z] = self.sudoku[i][k][z]
            for a in self.number_list[0]:
                if self.solve == True:
                    break
                for b in self.number_list[1]:
                    if self.solve == True:
                        break
                    for c in self.number_list[2]:
                        if self.solve == True:
                            break
                        for d in self.number_list[3]:
                            if self.solve == True:
                                break
                            for e in self.number_list[4]:
                                if self.solve == True:
                                    break
                                for f in self.number_list[5]:
                                    if self.solve == True:
                                        break
                                    for g in self.number_list[6]:
                                        if self.solve == True:
                                            break
                                        for h in self.number_list[7]:
                                            if self.solve == True:
                                                break
                                            for i in self.number_list[8]:
                                                if self.solve == True:
                                                    break
                                                for j in self.number_list[9]:
                                                    self.sudoku[self.row[0]][self.column[0]][0] = a
                                                    self.sudoku[self.row[1]][self.column[1]][0] = b
                                                    self.sudoku[self.row[2]][self.column[2]][0] = c
                                                    self.sudoku[self.row[3]][self.column[3]][0] = d
                                                    self.sudoku[self.row[4]][self.column[4]][0] = e
                                                    self.sudoku[self.row[5]][self.column[5]][0] = f
                                                    self.sudoku[self.row[6]][self.column[6]][0] = g
                                                    self.sudoku[self.row[7]][self.column[7]][0] = h
                                                    self.sudoku[self.row[8]][self.column[8]][0] = i
                                                    self.sudoku[self.row[9]][self.column[9]][0] = j
                                                    S.Fill_Protocol(a, self.row[0], self.column[0])
                                                    S.Fill_Protocol(b, self.row[1], self.column[1])
                                                    S.Fill_Protocol(c, self.row[2], self.column[2])
                                                    S.Fill_Protocol(d, self.row[3], self.column[3])
                                                    S.Fill_Protocol(e, self.row[4], self.column[4])
                                                    S.Fill_Protocol(f, self.row[5], self.column[5])
                                                    S.Fill_Protocol(g, self.row[6], self.column[6])
                                                    S.Fill_Protocol(h, self.row[7], self.column[7])
                                                    S.Fill_Protocol(i, self.row[8], self.column[8])
                                                    S.Fill_Protocol(j, self.row[9], self.column[9])
                                                    flag = S.Valid_Sudoku()
                                                    if flag == False:
                                                        for i in range(9):
                                                            for k in range(9):
                                                                for z in range(10):
                                                                    self.sudoku[i][k][z] = sudoku2[i][k][z]
                                                        continue
                                                    else:
                                                        S.Primitive_Elimination()
                                                        while(True):
                                                            self.changes = 0
                                                            S.Primitive_Fill()
                                                            if self.changes == 0:
                                                                S.Primitive_Fill()
                                                                if self.changes == 0:
                                                                    S.Check()
                                                                    break
                                                        if self.solve == True:
                                                            S.Display()
                                                            print("Sudoku Solved!!")
                                                            break
                                                        else:
                                                            for i in range(9):
                                                                for k in range(9):
                                                                    for z in range(10):
                                                                        self.sudoku[i][k][z] = sudoku2[i][k][z]

        else:
        #lets make 15 guesses
            acc = 1
            print("Advanced solving done, 15 assumptions taken")
            sudoku2 = [[[0 for i in range(10)] for k in range(9)] for z in range(9)]
            self.sudoku3 = [[[0 for i in range(10)] for k in range(9)] for z in range(9)]
            for i in range(9):
                for k in range(9):
                    for z in range(10):
                        self.sudoku3[i][k][z] = self.sudoku[i][k][z]
                        sudoku2[i][k][z] = self.sudoku[i][k][z]
            for a in self.number_list[0]:
                if(self.solve == True):
                    break
                for i in range(9):
                    for k in range(9):
                        for z in range(10):
                            self.sudoku[i][k][z] = sudoku2[i][k][z]
                self.sudoku[self.row[0]][self.column[0]][0] = a
                S.Fill_Protocol(a, self.row[0], self.column[0])
                for b in self.number_list[1]:
                    if self.solve == True:
                        break
                    S.Antifill(2)
                    self.sudoku[self.row[1]][self.column[1]][0] = b
                    S.Fill_Protocol(b, self.row[1], self.column[1])
                    if S.Valid_Sudoku() == False:
                        continue
                    for c in self.number_list[2]:
                        if self.solve == True:
                            break
                        S.Antifill(3)
                        self.sudoku[self.row[2]][self.column[2]][0] = c
                        S.Fill_Protocol(c, self.row[2], self.column[2])
                        if S.Valid_Sudoku() == False:
                            continue
                        for d in self.number_list[3]:
                            if self.solve == True:
                                break
                            S.Antifill(4)
                            self.sudoku[self.row[3]][self.column[3]][0] = d
                            S.Fill_Protocol(d, self.row[3], self.column[3])
                            if S.Valid_Sudoku() == False:
                                continue
                            for e in self.number_list[4]:
                                if self.solve == True:
                                    break
                                S.Antifill(5)
                                self.sudoku[self.row[4]][self.column[4]][0] = e
                                S.Fill_Protocol(e, self.row[4], self.column[4])
                                if S.Valid_Sudoku() == False:
                                    continue
                                for f in self.number_list[5]:
                                    if self.solve == True:
                                        break
                                    S.Antifill(6)
                                    self.sudoku[self.row[5]][self.column[5]][0] = f
                                    S.Fill_Protocol(f, self.row[5], self.column[5])
                                    if S.Valid_Sudoku() == False:
                                        continue
                                    for g in self.number_list[6]:
                                        if self.solve == True:
                                            break
                                        S.Antifill(7)
                                        self.sudoku[self.row[6]][self.column[6]][0] = g
                                        S.Fill_Protocol(g, self.row[6], self.column[6])
                                        if S.Valid_Sudoku() == False:
                                            continue
                                        for h in self.number_list[7]:
                                            if self.solve == True:
                                                break
                                            S.Antifill(8)
                                            self.sudoku[self.row[7]][self.column[7]][0] = h
                                            S.Fill_Protocol(h, self.row[7], self.column[7])
                                            if S.Valid_Sudoku() == False:                  
                                                continue
                                            for i in self.number_list[8]:
                                                if self.solve == True:
                                                    break
                                                S.Antifill(9)
                                                self.sudoku[self.row[8]][self.column[8]][0] = i
                                                S.Fill_Protocol(i, self.row[8], self.column[8])  
                                                if S.Valid_Sudoku() == False:                                                    
                                                    continue
                                                for j in self.number_list[9]:
                                                    if self.solve == True:
                                                        break
                                                    S.Antifill(10)
                                                    self.sudoku[self.row[9]][self.column[9]][0] = j
                                                    S.Fill_Protocol(j, self.row[9], self.column[9])
                                                    if S.Valid_Sudoku() == False:
                                                        continue
                                                    for k in self.number_list[10]:
                                                        if self.solve == True:
                                                            break
                                                        S.Antifill(11)
                                                        self.sudoku[self.row[10]][self.column[10]][0] = k
                                                        S.Fill_Protocol(k, self.row[10], self.column[10])
                                                        if S.Valid_Sudoku() == False:
                                                            continue
                                                        for l in self.number_list[11]:
                                                            if self.solve == True:
                                                                break
                                                            S.Antifill(12)
                                                            self.sudoku[self.row[11]][self.column[11]][0] = l
                                                            S.Fill_Protocol(l, self.row[11], self.column[11])
                                                            if S.Valid_Sudoku() == False:
                                                                continue
                                                            for m in self.number_list[12]:
                                                                if self.solve == True:
                                                                    break
                                                                S.Antifill(13)
                                                                self.sudoku[self.row[12]][self.column[12]][0] = m
                                                                S.Fill_Protocol(m, self.row[12], self.column[12])
                                                                if S.Valid_Sudoku() == False:
                                                                    continue
                                                                for n in self.number_list[13]:
                                                                    if self.solve == True:
                                                                        break
                                                                    S.Antifill(14)
                                                                    self.sudoku[self.row[13]][self.column[13]][0] = n
                                                                    S.Fill_Protocol(n, self.row[13], self.column[13])
                                                                    if S.Valid_Sudoku() == False:
                                                                        continue
                                                                    for o in self.number_list[14]:
                                                                        self.sudoku[self.row[14]][self.column[14]][0] = o
                                                                        S.Fill_Protocol(o, self.row[14], self.column[14])
                                                                        flag = S.Valid_Sudoku()
                                                                        if flag == False:
                                                                            continue
                                                                        else:
                                                                            acc+=1
                                                                            inter = [[[0 for i in range(10)] for k in range(9)] for z in range(9)]
                                                                            for i in range(9):
                                                                                for k in range(9):
                                                                                    for z in range(10):
                                                                                        inter[i][k][z] = self.sudoku[i][k][z]
                                                                            S.Primitive_Elimination()
                                                                            while(True):
                                                                                self.changes = 0
                                                                                S.Primitive_Fill()
                                                                                if self.changes == 0:
                                                                                    S.Primitive_Fill()
                                                                                    if self.changes == 0:
                                                                                        S.Check()
                                                                                        break
                                                                            if self.solve == True:
                                                                                #S.Display()
                                                                                print("Sudoku Solved!!")
                                                                                break
                                                                            else:
                                                                                #print(acc, "Assumption incorrect")
                                                                                acc+=1
                                                                                for i in range(9):
                                                                                    for k in range(9):
                                                                                        for z in range(10):
                                                                                            self.sudoku[i][k][z] = inter[i][k][z]
              
    def Solve(self):
        #S.Accept()
        print("Input sudoku matrix looks like this:-")
        S.Display()
        #print("Does your Sudoku matrix look like this? Enter 1 if yes, 0 otherwise")
        #a = int(input())
        a = 1
        if a == 1:
            S.Primitive_Elimination()
            while(True):
                self.changes = 0
                S.Primitive_Fill()
                if self.changes == 0:
                    S.Primitive_Fill()
                    if self.changes == 0:
                        S.Check()
                        break
            print("Primitive Solving done")
            #S.Display()
            if self.solve == True:
                print("Sudoku Solved!!")
            else:
                unsolve = 0
                for i in range(9):
                    for k in range(9):
                        if self.sudoku[i][k][0] == 0:
                            unsolve+=1
                if unsolve <= 65 and S.Valid_Sudoku() == True:
                    #Going to advanced
                    S.Advanced()
                else:
                    self.solve == False
        else:
            self.solve == False
        if self.solve == False:
            print("Couldnt solve sudoku")

S = Sudoku()
#S.Solve()


root=Tk()
root.title("Sudoku Solver")
root.geometry("500x400")

my_notebook=ttk.Notebook(root)
my_notebook.pack(pady=5)

#for keeping count of hints
hints=3

solved_sudoku=[[1 for i in range(9)] for k in range(9)]
question_sudoku=[[0 for i in range(9)] for k in range(9)]
#question_sudoku[1][0]=1

#creating frames
input_f=Frame(my_notebook,width=480,height=380,bg="#65CCB8")
input_f.pack(fill='both',expand=1)

answer_f=Frame(my_notebook,width=480,height=380,bg="#A8D0E6")
answer_f.pack(fill='both',expand=1)

unanswered_f=Frame(my_notebook,width=480,height=380, bg="burlywood1")
unanswered_f.pack(fill='both',expand=1)

gui_f=Frame(my_notebook,width=480,height=380, bg="powder blue")
gui_f.pack(fill='both',expand=1)

display_f=Frame(my_notebook,width=480,height=380, bg="NavajoWhite3")
display_f.pack(fill='both',expand=1)

#adding frames
my_notebook.add(input_f,text='Input')
my_notebook.add(answer_f,text='Solved')
my_notebook.add(unanswered_f,text='Unsolved')
my_notebook.add(gui_f,text='GUI')
my_notebook.add(display_f,text='Show Answer')

my_notebook.tab(1,state='disabled')
my_notebook.tab(2,state='disabled')
my_notebook.tab(3,state='disabled')
my_notebook.tab(4,state='disabled')



num=[0,1,2,3,4,5,6,7,8,9]               #list of numbers as options
click=StringVar()
def select(event):                      #event loop responds if we click on particular num and takes that as event 
    mylab=Label(input_f,text=click.get())
    mylab.grid(row=0,column=0)
 

click1=[[0 for i in range(9)] for k in range(9)]

#display frame
def display():
    for i in range(9):
        for k in range(9):
            Label(display_f, text=str(solved_sudoku[i][k]), bg="medium spring green", fg="dark green", borderwidth = 3, width = 6, relief="groove").grid(row=i, column=k)#, ipadx=2, ipady=2)

#loop for storing values selected in dropdown box
for i in range(9):
    for k in range(9):
        click1[i][k]=IntVar()

drop = [[0 for i in range(9)] for k in range(9)]
drop=[[OptionMenu(input_f, click1[i][k],*num, command=select) for k in range(9)] for i in range(9)]

for i in range(9):
    for k in range(9):
        drop[i][k].grid(row=i,column=k)
        drop[i][k].config(bg="#EAE7DC", fg="#2B7A78")         #giving colours to drop down lists
    
solve_button_flag = False
#setting the values in question sudoku
def set_button():
    for i in range(9):
        for k in range(9):
            drop[i][k].configure(state='disabled',bg="#D8C3A5", fg="#E85A4F")

#contains code to solve the sudoku
def solve_sudoku():
    global solve_button_flag
    if solve_button_flag == True:
        messagebox.showerror("Error", "Solve button can be clicked only once! It already has been, you can click on exit.")
    else:
        #set button is called
        set_button()
        solve_button_flag = True
        #solving code
        for i in range(9):
            for k in range(9):
                S.sudoku[i][k][0] = int(click1[i][k].get())
                question_sudoku[i][k] = int(click1[i][k].get())
                for z in range(1, 10):
                    if S.sudoku[i][k][0] == 0:
                        S.sudoku[i][k][z] = z
                    else:
                        S.sudoku[i][k][z] = 0
        S.Solve()
        if(S.solve == True):
            for i in range(9):
                for k in range(9):
                    solved_sudoku[i][k] = S.sudoku[i][k][0]
            my_notebook.tab(1,state='normal')
        else:
            my_notebook.tab(2,state='normal')

#unblocking the grid for editing
def unblock():
    global solve_button_flag
    if solve_button_flag == True:               #to prevent multiple 'Solve' clicks
        messagebox.showwarning("Warning", "Solve button can be clicked only once. It's already been clicked once. Further changes would be fruitless.")
    for i in range(9):
        for k in range(9):
            drop[i][k].configure(state='normal',bg="#EAE7DC", fg="#2B7A78")

def lets_quit():
    root.destroy()

b1=Button(input_f,text="Set",command=set_button,bg="#3B945E", fg="#254E58")     #to set question sudoku
b1.grid(row=11,column=0)

b2=Button(input_f,text="Solve",command=solve_sudoku,bg="#9B786F", fg="#4F4A41") #to solve question sudoku
b2.grid(row=12,column=0,columnspan=2)

b3=Button(input_f,text="Unblock",command=unblock,bg="#3B945E", fg="#254E58")    #to unlock locked grid
b3.grid(row=11,column=1,columnspan=2)

b4=Button(input_f, text="Exit", command=lets_quit,bg="#9B786F", fg="#4F4A41")   #to exit the application
b4.grid(row = 12, column = 1, columnspan=2)

#gui frame
click=StringVar()

def select2(x):                 #event loop responds if we click on particular num and takes that as event
    mylab=Label(gui_f,text=click.get())
    mylab.grid(row=0,column=0)

click2=[[0 for i in range(9)] for k in range(9)]        #variables to hold values from drop-down menu
for i in range(9):
    for k in range(9):
        click2[i][k]=IntVar()
    
num2=[0,1,2,3,4,5,6,7,8,9,10]

drop2=[[0 for i in range(9)] for k in range(9)]

t_start=0                   #for checking time taken to solve
t_end=0

wrong_attempts = 0             #for counting number of wrong attempts

def entry_check():              #command of the Check entries button
    global hints
    global wrong_attempts
    global t_start
    global t_end
    for i in range(9):
        for k in range(9):
            #for hints
            if((click2[i][k].get()==10) and hints>0):
                hints-=1
                #question_sudoku[i][k]=solved_sudoku[i][k]
                str1="Hint given, number is "+str(solved_sudoku[i][k])+" at ("+str(i)+", "+str(k)+"), hints remaining= "+str(hints)
                messagebox.showinfo("Information", str1)
            
            elif((click2[i][k].get()==10) and hints<=0):
                messagebox.showerror("Error", "Out of hints!")
            
            #error message on wrong entry
            elif(click2[i][k].get()!=0):
                if(click2[i][k].get()!=solved_sudoku[i][k]):
                    wrong_attempts+=1
                    str2="Wrong value entered at ("+str(i)+", "+str(k)+")"+" Please change value there back to 0, if you do not know the answer."
                    messagebox.showerror("Error", str2)
                else:
                    question_sudoku[i][k]=click2[i][k].get()            #no messagebox and correct entries and grid locked
                    drop2[i][k].configure(state='disabled', bg="medium aquamarine")
    
    if solved_sudoku == question_sudoku:
        t_end = time.time()                     #end time count
        elapsed = t_end-t_start                 
        m = elapsed/60
        m=int(m)
        s = elapsed%60
        s = int(s)
        st = "Sudoku solved. Wrong attempts = "+str(wrong_attempts)+". Hints used = "+str((3-hints))+". Time taken to solve = "+str(m)+" minutes and "+str(s)+" seconds."
        messagebox.showinfo("Information", st)                 #messagebox shows number of mistakes, number of hints used and time taken to solve
        messagebox.showinfo("Information", "You win! Congrats. You can click on exit on the 'Input' tab now")

ans_b=Button(gui_f, text="Check entries", command=entry_check)      #Check entries button
ans_b.grid(row=11, column=0, columnspan = 3)

for i in range(9):
    for k in range(9):
        drop2[i][k]=OptionMenu(gui_f, click2[i][k], *num2, command=select2)         #creating sudoku grid for gui

#For setting up gui frame
def guifun():                               #this adds dropdown menu for user entries and adds labels for the non zero question sudoku entries
    for i in range(9):
        for k in range(9):
            if(question_sudoku[i][k]==0):
                drop2[i][k].grid(row=i, column=k)
                drop2[i][k].configure(bg="pale green", fg="dark green")
            else:
                Label(gui_f, text=str(question_sudoku[i][k]), bg="#EAE7DC", fg="#2B7A78", borderwidth = 3, width = 6, relief="groove").grid(row=i, column=k)
    
    hint_label=Label(gui_f, text="For hint, enter value 10 in the block. 0 means undefined(empty)")     #legend for number entries of 0 and 10
    hint_label.grid(row = 12, column = 0,columnspan=9)


#solve frame
answer_see_flag = False         #flags to ensure anti-cheating measures
enable_gui_flag = False

def enable_gui():               #command to enable gui
    global t_start
    global answer_see_flag
    global enable_gui_flag
    enable_gui_flag = True
    if answer_see_flag == True:
        messagebox.showerror("Error", "You can't use the GUI after seeing the answer. Sorry.")
    else:
        my_notebook.tab(3,state='normal')
        t_start = time.time()
        guifun()

def see_answer():               #command to show answer sudoku
    global answer_see_flag
    global enable_gui_flag
    answer_see_flag = True
    if enable_gui_flag == True:
        messagebox.showwarning("Warning", "GUI is disabled now, since you have enabled the answer.")
        my_notebook.tab(3,state='disabled')
    my_notebook.tab(4,state='normal')
    display()

b5=Button(answer_f,text="Enable GUI",command=enable_gui, bg="#25274D", fg="#2B7A78")        #button for enabling gui
b5.pack(pady=5)

b6=Button(answer_f,text="See answer",command=see_answer, bg="#464866", fg="#2E9CCA")        #button to show answer frame
b6.pack(pady=5)

#unsolved frame
mylab2=Label(unanswered_f,text="Couldn't solve sudoku :( ", font=("Helvetica", 17), borderwidth=2, relief="sunken", bg="burlywood1")
mylab2.pack()
mylab4=Label(unanswered_f,text="Too little entries were provided, or were invalid.", bg="burlywood1", font=("Helvetica", 17), borderwidth=2, relief="sunken")
mylab4.pack()
mylab3=Label(unanswered_f,text="Click on exit in 'Input' tab.", font=("Helvetica", 17), bg="burlywood1", borderwidth=2, relief="sunken")
mylab3.pack()


root.resizable(0,0)
root.mainloop()
