from random import randint


def start_field(W, H):
    field = []
    for x in range(0, W):
        columns = []
        for y in range(0, H):
            columns.append(randint(0, 1))
        field.append(columns)
    return field


def start_field_next_step(W, H):
    field = []
    for x in range(0, W):
        columns = []
        for y in range(0, H):
            columns.append(0)
        field.append(columns)
    return field


def is_alive(x, y, current_field):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if current_field[i][j] >= 1:
                count += 1
                if i == x and j == y:
                    count -= 1
    return count


def field_next_step(W, H, current_field):
    field = start_field_next_step(W, H)
    for x in range(1, W - 1):
        for y in range(1, H - 1):
            count = is_alive(x, y, current_field)
            if current_field[x][y] >= 1 and (count == 2 or count == 3):
                field[x][y] = current_field[x][y] + 1
            elif current_field[x][y] >= 1 and (count < 2 or count > 3):
                field[x][y] = 0
            elif current_field[x][y] == 0 and count == 3:
                field[x][y] = 1
            else:
                field[x][y] = 0
    return field

##current_field = [[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]]

##print (field_next_step(5, 5, current_field))