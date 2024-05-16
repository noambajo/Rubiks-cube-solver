import queue
from tkinter import *
from tkinter import ttk
import FaceMatrixCombiner as Combiner
import threading


def update_label(label, q):
    while True:
        try:
            # print("updating")
            label.config(text=q.get_nowait())
        except queue.Empty:
            pass
        root.update()


def open_camera(q):
    Combiner.main(callback=lambda new_text: q.put(new_text))
    '''Combiner.main()
    new = Combiner.text
    print("new: ", new)
    q.put(new)'''


'''def open_cam_update():
    camera_thread = Thread(target=open_camera())
    camera_thread.start()'''


root = Tk()
root.geometry("500x500")
frm = ttk.Frame(root, padding=10)
frm.grid()

root.title("Rubik's cube solver")
Label(frm, text="Welcome to my project").grid(column=0, row=0)
Label(frm, text="Let's solve a rubik's cube together!").grid(column=0, row=1)

instructions = Label(frm, text="")
instructions.grid(column=3, row=3)
q = queue.Queue()
update_thread = threading.Thread(target=update_label, args=(instructions, q))
update_thread.daemon = True
update_thread.start()
Button(root, text="Open the camera", command=lambda: threading.Thread(target=open_camera, args=(q, )).start()).grid(column=0, row=2)
Button(frm, text="Exit", command=root.destroy).grid(column=1, row=2)
root.mainloop()
