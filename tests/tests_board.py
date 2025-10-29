import random

def matrix_size():
    return int(input('Matrix size: '))

size = matrix_size()

def create_matrix(size: int, fill: int = 0) -> list[list[int]]:
    ships = [[fill for i in range(size)] for i in range(size)]
    return ships
#print (create_matrix(matrix_size()))

def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
    shots = [[fill for i in range(size)] for j in range(size)]
    return shots
#print(create_bool_matrix(matrix_size()))

def in_bounds(size: int, x: int, y: int) -> bool:
    return 0 <= x < size and 0 <= x < size
#print (in_bounds(matrix_size(),1,0))

def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]]) -> int:
    counter = 0
    for i in range(len(shots)):
        for j in range(len(shots)):
            if ships[i][j] == 0 and shots[i][j]:
                counter += 1
    return counter
    
#print(count_remaining_ships(create_matrix(size),create_bool_matrix(size, True)))

def number_of_submarines() -> int:
    return int(input('How many submarines? '))

def check_number_of_submarines(size):
    amount = number_of_submarines()
    if amount > size*size or amount < 1:
        check_number_of_submarines(size)
    return amount
    
#print (check_number_of_submarines(size))

def random_index(size):
    num = random.randrange(size)
    #print (num)
    return num


def add_submarines_in_metrix(metrix: list[list[int]], submarines: int, size: int):
    counter = submarines
    #print (counter)
    while counter > 0:
        x = random_index(size)
        y = random_index(size)
        if metrix[x][y] is False:
            metrix[x][y] = True
            print (metrix)
            counter -= 1
            #print (counter)
    return metrix
#print (add_submarines_in_metrix(create_bool_matrix(size), check_number_of_submarines(size), size))