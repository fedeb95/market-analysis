import tkinter
from tkinter import Button

from sizer import Sizer

def main():
    win = tkinter.Tk()
    win.update_idletasks()

    print(win.winfo_width())
    sizer = Sizer(win)
    (win_width, win_height) = sizer.size_scr(0.7)

    # calculate centered position
    (center_x, center_y) = sizer.size_scr(0.5)
    x_position = int(center_x - win_width/2)
    y_position = int(center_y - win_height/2)

    win.title('Insider')
    geometry = f'{win_width}x{win_height}+{x_position}+{y_position}'
    win.geometry(geometry)

    (btn_w, btn_h) = sizer.size_win(0, 0.01)
    btn = Button(win, width=btn_w, height=btn_h, text='Download Data')
    btn.place(x=0, y=0)

    win.mainloop()

if __name__=='__main__':
    main()
