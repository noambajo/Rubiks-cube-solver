import networkx as nx
import HelperFunctions as Help

# https://rubikscu.be/
'''
0-b, 1-g, 2-w, 3-y, 4-o, 5-r, 9-blank
0 o 0
g w b
0 r 0
0 y 0
'''
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
G = nx.DiGraph()
nine_counter = 0
for i in range(1, 55):
    G.add_node(i - nine_counter)
blue, green, white, yellow, orange, red = Help.matrix_to_graph(CUBE_NET)
pairs = [{2, 53}, {44, 47}, {32, 38}, {24, 25}, {21, 22}, {8, 14}, {4, 11}, {6, 17}, {35, 42}, {29, 40}, {51, 27}, {19, 49}]
corners = [{7, 13, 12}, {9, 15, 16}, {33, 34, 39}, {30, 31, 37}, {3, 18, 54}, {1, 10, 52}, {28, 43, 46}, {36, 45, 48}]
F = [(22, 14), (14, 24), (24, 32), (32, 22), (13, 15), (15, 33), (33, 31), (31, 13), (16, 39), (39, 30), (30, 7), (7, 16), (37, 12), (12, 9), (9, 34), (34, 37), (38, 21), (21, 8), (8, 25), (25, 38)]
F_inv = [(14, 22), (22, 32), (32, 24), (24, 14), (13, 31), (31, 33), (33, 15), (15, 13), (12, 37), (37, 34), (34, 9), (9, 12), (21, 38), (38, 25), (25, 8), (8, 21), (30, 39), (39, 16), (16, 7), (7, 30)]
R_inv = [(25, 17), (17, 27), (27, 35), (35, 25), (16, 18), (18, 36), (36, 34), (34, 16), (3, 15), (15, 39), (39, 48), (48, 3), (6, 24), (24, 42), (42, 51), (51, 6), (9, 33), (33, 45), (45, 54), (54, 9)]
R = [(18, 16), (16, 34), (34, 36), (36, 18), (17, 25), (25, 35), (35, 27), (27, 17), (3, 48), (48, 39), (39, 15), (15, 3), (6, 51), (51, 42), (42, 24), (24, 6), (9, 54), (54, 45), (45, 33), (33, 9)]
L = [(10, 12), (12, 30), (30, 28), (28, 10), (19, 11), (11, 21), (21, 29), (29, 19), (1, 13), (13, 37), (37, 46), (46, 1), (4, 22), (22, 40), (40, 49), (49, 4), (7, 31), (31, 43), (43, 52), (52, 7)]
L_inv = [(10, 28), (28, 30), (30, 12), (12, 10), (11, 19), (19, 29), (29, 21), (21, 11), (1, 46), (46, 37), (37, 13), (13, 1), (4, 49), (49, 40), (40, 22), (22, 4), (7, 52), (52, 43), (43, 31), (31, 7)]
D = [(37, 39), (39, 45), (45, 43), (43, 37), (40, 38), (38, 42), (42, 44), (44, 40), (28, 31), (31, 34), (34, 48), (48, 28), (29, 32), (32, 35), (35, 47), (47, 29), (30, 33), (33, 36), (36, 46), (46, 30)]
D_inv = [(37, 43), (43, 45), (45, 39), (39, 37), (40, 44), (44, 42), (42, 38), (38, 40), (28, 48), (48, 34), (34, 31), (31, 28), (29, 47), (47, 35), (35, 32), (32, 29), (30, 46), (46, 36), (36, 33), (33, 30)]
U = [(1, 3), (3, 9), (9, 7), (7, 1), (2, 6), (6, 8), (8, 4), (4, 2), (18, 15), (15, 12), (12, 54), (54, 18), (17, 14), (14, 11), (11, 53), (53, 17), (16, 13), (13, 10), (10, 52), (52, 16)]
U_inv = [(1, 7), (7, 9), (9, 3), (3, 1), (2, 4), (4, 8), (8, 6), (6, 2), (10, 13), (13, 16), (16, 52), (52, 10), (11, 14), (14, 17), (17, 53), (53, 11), (12, 15), (15, 18), (18, 54), (54, 12)]
B = [(46, 48), (48, 54), (54, 52), (52, 46), (49, 47), (47, 51), (51, 53), (53, 49), (1, 28), (28, 45), (45, 18), (18, 1), (2, 19), (19, 44), (44, 27), (27, 2), (3, 10), (10, 43), (43, 36), (36, 3)]
B_inv = [(46, 52), (52, 54), (54, 48), (48, 46), (49, 53), (53, 51), (51, 47), (47, 49), (10, 3), (3, 36), (36, 43), (43, 10), (19, 2), (2, 27), (27, 44), (44, 19), (28, 1), (1, 18), (18, 45), (45, 28)]
G.add_edges_from(F, move='F')
G.add_edges_from(F_inv, move='F_inv')
G.add_edges_from(R, move='R')
G.add_edges_from(R_inv, move='R_inv')
G.add_edges_from(L, move='L')
G.add_edges_from(L_inv, move='L_inv')
G.add_edges_from(D, move='D')
G.add_edges_from(D_inv, move='D_inv')
G.add_edges_from(U, move='U')
G.add_edges_from(U_inv, move='U_inv')
G.add_edges_from(B, move='B')
G.add_edges_from(B_inv, move='B_inv')
# white cross
pair = Help.calculate_white_cross_pair_per_color(white, pairs, CUBE_NET, 4)
print("orange")
P = nx.shortest_path(G, pair[0], 14)
for i in range(len(P) - 1):
    rotation = G.edges[P[i], P[i + 1]]['move']
    CUBE_NET = Help.rotate_entre_face(CUBE_NET, Help.rotation_to_color(rotation))
    print(rotation)
blue, green, white, yellow, orange, red = Help.matrix_to_graph(CUBE_NET)
G.remove_edges_from(F)
G.remove_edges_from(F_inv)
pair = Help.calculate_white_cross_pair_per_color(white, pairs, CUBE_NET, 1)
print("green")
all_paths = list(nx.all_simple_paths(G, pair[0], 22))
filtered_path = [path for path in all_paths if Help.same_number_of_edges_condition(path, U, U_inv)]
P = min(filtered_path, key=len)
for i in range(len(P) - 1):
    rotation = G.edges[P[i], P[i + 1]]['move']
    CUBE_NET = Help.rotate_entre_face(CUBE_NET, Help.rotation_to_color(rotation))
    print(rotation)
blue, green, white, yellow, orange, red = Help.matrix_to_graph(CUBE_NET)
pair = Help.calculate_white_cross_pair_per_color(white, pairs, CUBE_NET, 5)
print("red")
all_paths = list(nx.all_simple_paths(G, pair[0], 32))
filtered_path = [path for path in all_paths if Help.same_number_of_edges_condition(path, U, U_inv) and Help.same_number_of_edges_condition(path, L, L_inv)]
P = min(filtered_path, key=len)
for i in range(len(P) - 1):
    rotation = G.edges[P[i], P[i + 1]]['move']
    CUBE_NET = Help.rotate_entre_face(CUBE_NET, Help.rotation_to_color(rotation))
    print(rotation)
blue, green, white, yellow, orange, red = Help.matrix_to_graph(CUBE_NET)
pair = Help.calculate_white_cross_pair_per_color(white, pairs, CUBE_NET, 0)
print("blue")
all_paths = list(nx.all_simple_paths(G, pair[0], 24))
filtered_path = [path for path in all_paths if Help.same_number_of_edges_condition(path, U, U_inv) and Help.same_number_of_edges_condition(path, L, L_inv) and Help.same_number_of_edges_condition(path, D, D_inv)]
P = min(filtered_path, key=len)
for i in range(len(P) - 1):
    rotation = G.edges[P[i], P[i + 1]]['move']
    CUBE_NET = Help.rotate_entre_face(CUBE_NET, Help.rotation_to_color(rotation))
    print(rotation)
blue, green, white, yellow, orange, red = Help.matrix_to_graph(CUBE_NET)
