import networkx as nx

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
blue = set()
green = set()
white = set()
yellow = set()
orange = set()
red = set()
nine_counter = 0
for i in range(1, 108):
    color = CUBE_NET[i // 9][i % 9]
    if color == 9:
        nine_counter += 1
        continue
    G.add_node(i - nine_counter, color=color)
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
pairs = [{2, 53}, {44, 47}, {32, 38}, {24, 25}, {21, 22}, {8, 14}, {4, 11}, {6, 17}, {35, 42}, {29, 40}, {51, 27}, {19, 49}]
corners = [{7, 13, 12}, {9, 15, 16}, {33, 34, 39}, {30, 31, 37}, {3, 18, 54}, {1, 10, 52}, {28, 43, 46}, {36, 45, 48}]
F = [(22, 14), (14, 24), (24, 32), (32, 22), (13, 15), (15, 33), (33, 31), (31, 13), (16, 39), (39, 30), (30, 7), (7, 16), (37, 12), (12, 9), (9, 34), (34, 37), (38, 21), (21, 8), (8, 25), (25, 34)]
F_inv = [(14, 22), (24, 14), (32, 24), (22, 32), (15, 13), (33, 15), (31, 33), (31, 13), (39, 16), (30, 39), (7, 30), (16, 7), (12, 37), (9, 12), (34, 9), (37, 34), (21, 38), (8, 21), (25, 8), (34, 25)]
R = [(25, 17), (17, 27), (27, 35), (35, 25), (16, 18), (18, 36), (36, 34), (34, 16), (3, 15), (15, 39), (39, 48), (48, 3), (6, 24), (24, 42), (42, 51), (51, 6), (9, 33), (33, 45), (45, 54), (54, 9)]
R_inv = [(17, 25), (27, 17), (35, 27), (25, 35), (18, 16), (36, 18), (34, 36), (16, 34), (15, 3), (39, 15), (48, 39), (3, 48), (24, 6), (42, 24), (51, 42), (6, 51), (33, 9), (45, 33), (54, 45), (9, 54)]
L = [(10, 12), (12, 30), (30, 28), (28, 10), (19, 11), (11, 21), (21, 29), (29, 19), (1, 13), (13, 37), (37, 46), (46, 1), (4, 22), (22, 40), (40, 49), (49, 4), (7, 31), (31, 43), (43, 52), (52, 7)]
L_inv = [(12, 10), (30, 12), (28, 30), (10, 28), (11, 19), (21, 11), (21, 29), (19, 29), (13, 1), (37, 13), (46, 37), (1, 46), (22, 4), (40, 22), (49, 40), (4, 49), (31, 7), (43, 31), (52, 43), (7, 52)]
D = [(37, 39), (39, 45), (45, 43), (43, 37), (40, 38), (38, 42), (42, 44), (44, 40), (28, 31), (31, 34), (34, 48), (48, 28), (29, 32), (32, 35), (35, 47), (47, 28), (30, 33), (33, 36), (36, 46), (46, 30)]
D_inv = [(39, 37), (45, 39), (43, 45), (37, 43), (38, 40), (42, 38), (44, 42), (40, 44), (31, 28), (34, 31), (48, 34), (28, 48), (32, 29), (35, 32), (47, 35), (28, 47), (33, 30), (36, 33), (46, 36), (30, 46)]
U = [(1, 3), (3, 9), (9, 7), (7, 1), (2, 6), (6, 8), (8, 4), (4, 2), (10, 13), (13, 16), (16, 54), (54, 10), (11, 14), (14, 17), (17, 53), (53, 11), (12, 15), (15, 18), (18, 52), (52, 12)]
U_inv = [(3, 1), (9, 3), (7, 9), (1, 7), (6, 2), (8, 6), (4, 8), (2, 4), (13, 10), (16, 13), (54, 16), (10, 54), (14, 11), (17, 14), (52, 17), (11, 53), (15, 12), (18, 15), (52, 18), (12, 52)]
B = [(46, 48), (48, 54), (54, 52), (52, 46), (49, 47), (47, 51), (51, 53), (53, 49), (43, 10), (10, 3), (3, 36), (36, 43), (44, 19), (19, 2), (2, 27), (27, 44), (45, 28), (28, 1), (1, 18), (18, 45)]
B_inv = [(48, 46), (54, 48), (52, 54), (46, 52), (47, 49), (51, 47), (53, 51), (49, 53), (10, 43), (3, 10), (36, 3), (43, 36), (19, 44), (2, 19), (27, 2), (44, 27), (28, 45), (1, 28), (18, 1), (45, 18)]
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
white_targetColor_pairs = []
for pair in pairs:
    nine_counter = 0
    node = 0
    intersection = pair.intersection(white)
    if intersection:
        other_node = pair.difference(intersection).pop()
        white_node = intersection.pop()
        while node-nine_counter < other_node:
            if CUBE_NET[node // 9][node % 9] == 9:
                nine_counter += 1
            node += 1
        white_targetColor_pairs.append((white_node, CUBE_NET[(other_node + nine_counter - 1) // 9][(other_node + nine_counter - 1) % 9]))
for color in white_targetColor_pairs:
    if color[1] == 4:
        P = nx.shortest_path(G, color[0], 14)
        print("orange")
        for i in range(len(P)-1):
            print(G.edges[P[i], P[i+1]]['move'])
        G.remove_edges_from(U)
        G.remove_edges_from(U_inv)
    if color[1] == 1:
        print("green")
        P = nx.shortest_path(G, color[0], 22)
        for i in range(len(P)-1):
            print(G.edges[P[i], P[i+1]]['move'])
        G.remove_edges_from(L)
        G.remove_edges_from(L_inv)
    if color[1] == 5:
        print("red")
        P = nx.shortest_path(G, color[0], 32)
        for i in range(len(P)-1):
            print(G.edges[P[i], P[i+1]]['move'])
        G.remove_edges_from(D)
        G.remove_edges_from(D_inv)
    if color[1] == 0:
        print("blue")
        P = nx.shortest_path(G, color[0], 24)
        for i in range(len(P)-1):
            print(G.edges[P[i], P[i+1]]['move'])
        G.remove_edges_from(R)
        G.remove_edges_from(R_inv)
    print("----")
