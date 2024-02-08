def graph_to_matrix(target, matrix):
    nine_counter = 0
    node = 0
    while node - nine_counter < target:
        if matrix[node // 9][node % 9] == 9:
            nine_counter += 1
        node += 1
    return matrix[(target + nine_counter - 1) // 9][(target + nine_counter - 1) % 9], nine_counter, target


def start_coordinate_finder(face_color):
    if face_color == 4:
        start_x = 3
        start_y = 0
    if face_color == 1:
        start_x = 0
        start_y = 3
    if face_color == 2:
        start_x = 3
        start_y = 3
    if face_color == 0:
        start_x = 6
        start_y = 3
    if face_color == 5:
        start_x = 3
        start_y = 6
    if face_color == 3:
        start_x = 3
        start_y = 9
    return start_x, start_y


def rotate_face_clockwise(net, face_color):
    face_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    rotated_face = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    start_x, start_y = start_coordinate_finder(face_color)
    for a in range(3):
        for b in range(3):
            face_matrix[a][b] = net[a+start_y][b+start_x]
    for i in range(3):
        for j in range(3):
            rotated_face[i][j] = face_matrix[2-j][i]
    return rotated_face


def rotate_entre_face_clockwise(net, face_color):
    start_x, start_y = start_coordinate_finder(face_color)
    rotated_face = rotate_face_clockwise(net, face_color)
    for i in range(3):
        for j in range(3):
            net[i+start_y][j+start_x] = rotated_face[i][j]
    adjacent_indices = {
        4: [(graph_to_matrix(10, net), graph_to_matrix(13, net), graph_to_matrix(16, net), graph_to_matrix(54, net)),
            (graph_to_matrix(11, net), graph_to_matrix(14, net), graph_to_matrix(17, net), graph_to_matrix(53, net)),
            (graph_to_matrix(12, net), graph_to_matrix(15, net), graph_to_matrix(18, net), graph_to_matrix(52, net))],

        1: [(graph_to_matrix(1, net)[0], graph_to_matrix(13, net)[0], graph_to_matrix(37, net)[0], graph_to_matrix(46, net)[0]),
            (graph_to_matrix(4, net)[0], graph_to_matrix(22, net)[0], graph_to_matrix(40, net)[0], graph_to_matrix(49, net)[0]),
            (graph_to_matrix(7, net)[0], graph_to_matrix(31, net)[0], graph_to_matrix(43, net)[0], graph_to_matrix(52, net)[0])],

        2: [(graph_to_matrix(7, net)[0], graph_to_matrix(16, net)[0], graph_to_matrix(39, net)[0], graph_to_matrix(30, net)[0]),
            (graph_to_matrix(8, net)[0], graph_to_matrix(25, net)[0], graph_to_matrix(38, net)[0], graph_to_matrix(21, net)[0]),
            (graph_to_matrix(9, net)[0], graph_to_matrix(34, net)[0], graph_to_matrix(37, net)[0], graph_to_matrix(12, net)[0])],

        0: [(graph_to_matrix(3, net)[0], graph_to_matrix(15, net)[0], graph_to_matrix(39, net)[0], graph_to_matrix(48, net)[0]),
            (graph_to_matrix(6, net)[0], graph_to_matrix(24, net)[0], graph_to_matrix(42, net)[0], graph_to_matrix(51, net)[0]),
            (graph_to_matrix(9, net)[0], graph_to_matrix(33, net)[0], graph_to_matrix(45, net)[0], graph_to_matrix(54, net)[0])],

        3: [(graph_to_matrix(28, net)[0], graph_to_matrix(31, net)[0], graph_to_matrix(34, net)[0], graph_to_matrix(48, net)[0]),
            (graph_to_matrix(29, net)[0], graph_to_matrix(32, net)[0], graph_to_matrix(35, net)[0], graph_to_matrix(47, net)[0]),
            (graph_to_matrix(30, net)[0], graph_to_matrix(33, net)[0], graph_to_matrix(36, net)[0], graph_to_matrix(46, net)[0])],

        5: [(graph_to_matrix(10, net)[0], graph_to_matrix(3, net)[0], graph_to_matrix(36, net)[0], graph_to_matrix(43, net)[0]),
            (graph_to_matrix(19, net)[0], graph_to_matrix(2, net)[0], graph_to_matrix(27, net)[0], graph_to_matrix(44, net)[0]),
            (graph_to_matrix(28, net)[0], graph_to_matrix(1, net)[0], graph_to_matrix(18, net)[0], graph_to_matrix(45, net)[0])]
    }
    for indices in adjacent_indices[face_color]:
        net[(indices[0][1] + indices[0][2] - 1) // 9][(indices[0][1] + indices[0][2] - 1) % 9], net[(indices[1][1] + indices[1][2] - 1) // 9][(indices[1][1] + indices[1][2] - 1) % 9], net[(indices[2][1] + indices[2][2] - 1) // 9][(indices[2][1] + indices[2][2] - 1) % 9], net[(indices[3][1] + indices[3][2] - 1) // 9][(indices[3][1] + indices[3][2] - 1) % 9] = net[(indices[3][1] + indices[3][2] - 1) // 9][(indices[3][1] + indices[3][2] - 1) % 9], net[(indices[0][1] + indices[0][2] - 1) // 9][(indices[0][1] + indices[0][2] - 1) % 9], net[(indices[1][1] + indices[1][2] - 1) // 9][(indices[1][1] + indices[1][2] - 1) % 9], net[(indices[2][1] + indices[2][2] - 1) // 9][(indices[2][1] + indices[2][2] - 1) % 9]
    return net


CUBE_NET = [[9, 9, 9, 2, 4, 1, 9, 9, 9],
            [9, 9, 9, 3, 4, 2, 9, 9, 9],
            [9, 9, 9, 3, 2, 1, 9, 9, 9],
            [4, 1, 0, 5, 1, 5, 2, 0, 3],
            [3, 1, 5, 1, 2, 4, 1, 0, 0],
            [4, 5, 3, 0, 3, 1, 3, 3, 0],
            [9, 9, 9, 4, 5, 4, 9, 9, 9],
            [9, 9, 9, 2, 5, 4, 9, 9, 9],
            [9, 9, 9, 2, 0, 2, 9, 9, 9],
            [9, 9, 9, 1, 4, 5, 9, 9, 9],
            [9, 9, 9, 0, 3, 5, 9, 9, 9],
            [9, 9, 9, 0, 2, 5, 9, 9, 9]]
print(CUBE_NET)
print(rotate_entre_face_clockwise(CUBE_NET, 4))
