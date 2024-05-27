def graph_to_matrix(target, matrix):
    nine_counter = 0
    node = 0
    while node - nine_counter < target:
        if matrix[node // 9][node % 9] == 9:
            nine_counter += 1
        node += 1
    return matrix[(target + nine_counter - 1) // 9][(target + nine_counter - 1) % 9], nine_counter, target


def rotation_to_color(rotation):
    if rotation == 'F':
        return 2
    if rotation == 'B':
        return 3
    if rotation == 'U':
        return 4
    if rotation == 'D':
        return 5
    if rotation == 'L':
        return 1
    if rotation == 'R':
        return 0
    if rotation == 'F_inv':
        return -2
    if rotation == 'B_inv':
        return -3
    if rotation == 'U_inv':
        return -4
    if rotation == 'D_inv':
        return -5
    if rotation == 'L_inv':
        return -1
    if rotation == 'R_inv':
        return -6

# TODO: Add dictionary for these functions


def start_coordinate_finder(face_color):
    x, y = 0, 0
    if abs(face_color) == 4:
        x = 3
        y = 0
    if abs(face_color) == 1:
        x = 0
        y = 3
    if abs(face_color) == 2:
        x = 3
        y = 3
    if face_color == 0 or face_color == -6:
        x = 6
        y = 3
    if abs(face_color) == 5:
        x = 3
        y = 6
    if abs(face_color) == 3:
        x = 3
        y = 9
    return x, y


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


def rotate_face_counterclockwise(net, face_color):
    face_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    rotated_face = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    start_x, start_y = start_coordinate_finder(face_color)
    for a in range(3):
        for b in range(3):
            face_matrix[a][b] = net[a+start_y][b+start_x]
    for i in range(3):
        for j in range(3):
            rotated_face[i][j] = face_matrix[j][2-i]
    return rotated_face


def rotate_entre_face(net, face_color):
    start_x, start_y = start_coordinate_finder(face_color)
    if face_color >= 0:
        rotated_face = rotate_face_clockwise(net, face_color)
    else:
        rotated_face = rotate_face_counterclockwise(net, face_color)
    for i in range(3):
        for j in range(3):
            net[i+start_y][j+start_x] = rotated_face[i][j]
    adjacent_indices = {
        -4: [(graph_to_matrix(10, net), graph_to_matrix(13, net), graph_to_matrix(16, net), graph_to_matrix(54, net)),
             (graph_to_matrix(11, net), graph_to_matrix(14, net), graph_to_matrix(17, net), graph_to_matrix(53, net)),
             (graph_to_matrix(12, net), graph_to_matrix(15, net), graph_to_matrix(18, net), graph_to_matrix(52, net))],

        4: [(graph_to_matrix(54, net), graph_to_matrix(16, net), graph_to_matrix(13, net), graph_to_matrix(10, net)),
            (graph_to_matrix(53, net), graph_to_matrix(17, net), graph_to_matrix(14, net), graph_to_matrix(11, net)),
            (graph_to_matrix(52, net), graph_to_matrix(18, net), graph_to_matrix(15, net), graph_to_matrix(12, net))],

        1: [(graph_to_matrix(1, net), graph_to_matrix(13, net), graph_to_matrix(37, net), graph_to_matrix(46, net)),
            (graph_to_matrix(4, net), graph_to_matrix(22, net), graph_to_matrix(40, net), graph_to_matrix(49, net)),
            (graph_to_matrix(7, net), graph_to_matrix(31, net), graph_to_matrix(43, net), graph_to_matrix(52, net))],

        -1: [(graph_to_matrix(46, net), graph_to_matrix(37, net), graph_to_matrix(13, net), graph_to_matrix(1, net)),
             (graph_to_matrix(49, net), graph_to_matrix(40, net), graph_to_matrix(22, net), graph_to_matrix(4, net)),
             (graph_to_matrix(52, net), graph_to_matrix(43, net), graph_to_matrix(31, net), graph_to_matrix(7, net))],

        2: [(graph_to_matrix(7, net), graph_to_matrix(16, net), graph_to_matrix(39, net), graph_to_matrix(30, net)),
            (graph_to_matrix(8, net), graph_to_matrix(25, net), graph_to_matrix(38, net), graph_to_matrix(21, net)),
            (graph_to_matrix(9, net), graph_to_matrix(34, net), graph_to_matrix(37, net), graph_to_matrix(12, net))],

        -2: [(graph_to_matrix(30, net), graph_to_matrix(39, net), graph_to_matrix(16, net), graph_to_matrix(7, net)),
             (graph_to_matrix(21, net), graph_to_matrix(38, net), graph_to_matrix(25, net), graph_to_matrix(8, net)),
             (graph_to_matrix(12, net), graph_to_matrix(37, net), graph_to_matrix(34, net), graph_to_matrix(9, net))],

        -6: [(graph_to_matrix(3, net), graph_to_matrix(15, net), graph_to_matrix(39, net), graph_to_matrix(48, net)),
             (graph_to_matrix(6, net), graph_to_matrix(24, net), graph_to_matrix(42, net), graph_to_matrix(51, net)),
             (graph_to_matrix(9, net), graph_to_matrix(33, net), graph_to_matrix(45, net), graph_to_matrix(54, net))],

        0: [(graph_to_matrix(48, net), graph_to_matrix(39, net), graph_to_matrix(15, net), graph_to_matrix(3, net)),
            (graph_to_matrix(51, net), graph_to_matrix(42, net), graph_to_matrix(24, net), graph_to_matrix(6, net)),
            (graph_to_matrix(54, net), graph_to_matrix(45, net), graph_to_matrix(33, net), graph_to_matrix(9, net))],

        5: [(graph_to_matrix(28, net), graph_to_matrix(31, net), graph_to_matrix(34, net), graph_to_matrix(48, net)),
            (graph_to_matrix(29, net), graph_to_matrix(32, net), graph_to_matrix(35, net), graph_to_matrix(47, net)),
            (graph_to_matrix(30, net), graph_to_matrix(33, net), graph_to_matrix(36, net), graph_to_matrix(46, net))],

        -5: [(graph_to_matrix(48, net), graph_to_matrix(34, net), graph_to_matrix(31, net), graph_to_matrix(28, net)),
             (graph_to_matrix(47, net), graph_to_matrix(35, net), graph_to_matrix(32, net), graph_to_matrix(29, net)),
             (graph_to_matrix(46, net), graph_to_matrix(36, net), graph_to_matrix(33, net), graph_to_matrix(30, net))],

        3: [(graph_to_matrix(10, net), graph_to_matrix(43, net), graph_to_matrix(36, net), graph_to_matrix(3, net)),
            (graph_to_matrix(19, net), graph_to_matrix(44, net), graph_to_matrix(27, net), graph_to_matrix(2, net)),
            (graph_to_matrix(28, net), graph_to_matrix(45, net), graph_to_matrix(18, net), graph_to_matrix(1, net))],

        -3: [(graph_to_matrix(43, net), graph_to_matrix(10, net), graph_to_matrix(3, net), graph_to_matrix(36, net)),
             (graph_to_matrix(44, net), graph_to_matrix(19, net), graph_to_matrix(2, net), graph_to_matrix(27, net)),
             (graph_to_matrix(45, net), graph_to_matrix(28, net), graph_to_matrix(1, net), graph_to_matrix(18, net))]
    }
    for indices in adjacent_indices[face_color]:
        net[(indices[0][1] + indices[0][2] - 1) // 9][(indices[0][1] + indices[0][2] - 1) % 9], \
            net[(indices[1][1] + indices[1][2] - 1) // 9][(indices[1][1] + indices[1][2] - 1) % 9], \
            net[(indices[2][1] + indices[2][2] - 1) // 9][(indices[2][1] + indices[2][2] - 1) % 9], \
            net[(indices[3][1] + indices[3][2] - 1) // 9][(indices[3][1] + indices[3][2] - 1) % 9] \
            = net[(indices[3][1] + indices[3][2] - 1) // 9][(indices[3][1] + indices[3][2] - 1) % 9], \
            net[(indices[0][1] + indices[0][2] - 1) // 9][(indices[0][1] + indices[0][2] - 1) % 9], \
            net[(indices[1][1] + indices[1][2] - 1) // 9][(indices[1][1] + indices[1][2] - 1) % 9], \
            net[(indices[2][1] + indices[2][2] - 1) // 9][(indices[2][1] + indices[2][2] - 1) % 9]
    return net


def matrix_to_graph(net):
    blue = set()
    green = set()
    yellow = set()
    white = set()
    red = set()
    orange = set()
    nine_counter = 0
    for i in range(1, 108):
        color = net[i // 9][i % 9]
        if color == 9:
            nine_counter += 1
            continue
        if color == 0:
            blue.update({i - nine_counter})
        if color == 1:
            green.update({i - nine_counter})
        if color == 2:
            white.update({i - nine_counter})
        if color == 3:
            yellow.update({i - nine_counter})
        if color == 4:
            orange.update({i - nine_counter})
        if color == 5:
            red.update({i - nine_counter})
    blue.difference_update({26})
    green.difference_update({20})
    white.difference_update({23})
    yellow.difference_update({50})
    orange.difference_update({5})
    red.difference_update({41})
    return blue, green, white, yellow, orange, red


def calculate_white_cross_pair_per_color(white, pairs, net, color):
    temp = []
    for pair in pairs:
        intersection = pair.intersection(white)
        if intersection:
            other_node = pair.difference(intersection).pop()
            if graph_to_matrix(other_node, net)[0] != color:
                continue
            white_node = intersection.pop()
            temp.append((white_node, graph_to_matrix(other_node, net)[0]))
            break
    return temp[0]


def same_number_of_edges_condition(path, edges_list_1, edges_list_2):
    count_edges_list_1 = 0
    count_edges_list_2 = 0
    for i in range(len(path) - 1):
        if (path[i], path[i + 1]) in edges_list_1:
            count_edges_list_1 += 1
        if (path[i], path[i + 1]) in edges_list_2:
            count_edges_list_2 += 1
    return count_edges_list_1 % 4 == count_edges_list_2 % 4


def color_pair_to_appropriate_corner(color1, color2, corners):
    possible_stickers = []
    if color1 == 0 or color2 == 0:
        possible_stickers.extend([18, 36])
    if color1 == 5 or color2 == 5:
        possible_stickers.extend([43, 45])
    if color1 == 1 or color2 == 1:
        possible_stickers.extend([10, 28])
    if color1 == 4 or color2 == 4:
        possible_stickers.extend([1, 3])
    for corner in corners:
        for i, j in [(a, b) for idx, a in enumerate(possible_stickers) for b in possible_stickers[idx + 1:]]:
            if len({i, j}.intersection(corner)) == 2:
                return corner.difference({i, j}), i, j


def num_to_color(num):
    if num == 0:
        return "blue"
    if num == 1:
        return "green"
    if num == 2:
        return "white"
    if num == 3:
        return "yellow"
    if num == 4:
        return "orange"
    return "red"
