start_pos, end_pos = input().split('-')
start_row = 8 - int(start_pos[1])
start_col = 'abcdefgh'.index(start_pos[0])
end_row = 8 - int(end_pos[1])
end_col = 'abcdefgh'.index(end_pos[0])

if ((abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1)
        or (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2)):
        print('Верно')
else:
        print('Ошибка')