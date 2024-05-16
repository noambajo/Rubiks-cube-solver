import os
import ReturnFaceMatrix
import HelperFunctions as Help

combined_net = [[9 for x in range(9)] for x in range(12)]
text = "hello"


def run_scripts(color, rotations, callback):
    os.system('python "CubeFaceDetector.py"')
    os.system('python "ReturnFaceMatrix.py"')
    copy_face_matrix(color, rotations, callback)


def copy_face_matrix(color, rotations, callback):
    face = ReturnFaceMatrix.FINAL_ARRAY
    color_check = face[1][1]
    if color != color_check:
        text = "You have scanned an incorrect face, please scan the correct one."
    for h in range(rotations):
        for i in range(3):
            for j in range(3):
                face[i][j] = face[2 - j][i]
    start_x, start_y = Help.start_coordinate_finder(color)
    for i in range(3):
        for j in range(3):
            combined_net[i+start_y][j+start_x] = face[i][j]


def main(callback):
    text = "Please show the camera the white face of the cube such that the orange face is facing the top"
    callback(text)
    run_scripts(2, 1, callback)

    text = "Please show the camera the orange face by rotating the cube towards the camera"
    callback(text)
    run_scripts(4, 0, callback)

    text = "Please show the camera the yellow face by rotating the cube towards the camera"
    callback(text)
    run_scripts(3, 0, callback)

    text = "Please show the camera the red face by rotating the cube towards the camera"
    callback(text)
    run_scripts(5, 0, callback)

    text = "Please show the camera the green face by rotating the cube to the left along the white face"
    callback(text)
    run_scripts(1, 1, callback)


if __name__ == "__main__":
    main()
