import tkinter as tk
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from utils.source import DataSource
from utils.display import Plot
from utils.transform import *
from utils.compose import *

from sizer import Sizer

class Download(DropNa):
    def __str__(self):
        return 'Download'
        
class Pipeline(Compose):
    def __str__(self):
        return '->'.join([ str(t) for t in self.transforms ])

def plot(plot, canvas, asset_entry, pipeline):
    plot.clear()
    print(pipeline.transforms)

    assets = [ a.strip() for a in asset_entry.get().split(',') ]
    data = DataSource().get_data(assets)
    data = pipeline.apply(data)
    Plot(plot).apply(data)
    canvas.draw()

def clear(pipeline, label):
    label.config(text='Download->')
    pipeline.clear().then(Download())

def add_to_pipeline(pipeline, transform, label, plt, canvas, asset_entry):
    pipeline.then(transform)
    label.config(text=str(pipeline)) 
    plot(plt, canvas, asset_entry, pipeline)
    
def main():
    win = tk.Tk()

    sizer = Sizer(win)
    (win_width, win_height) = sizer.size_scr(0.7)

    # calculate centered position
    (center_x, center_y) = sizer.size_scr(0.5)
    x_position = int(center_x - win_width/2)
    y_position = int(center_y - win_height/2)

    win.title('Insider')
    geometry = f'{win_width}x{win_height}+{x_position}+{y_position}'
    win.geometry(geometry)

    px = 1/matplotlib.rcParams['figure.dpi'] 
    fig_w, fig_h = sizer.size_win(1, 0.8)
    fig = Figure(figsize = ( int(fig_w*px), int(fig_h*px) ))
    pipe_plot = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master = win)  

    Label(win, text='Asset')
    entry = Entry(win) 
    entry.pack()

    pipeline = Pipeline().then(Download())

    pipe_label = Label(win,text='Download->')
    pipe_label.pack()

    (btn_w, btn_h) = sizer.size_win(0, 0)

    transforms = [ 
                    LogDiff(),
                    Pipeline().then(Rolling(250)).then(Mean()),
                    Pipeline().then(Rolling(250)).then(Variance()),
                    Pipeline().then(Rolling(250)).then(StandardDeviation()),
                ]
    funs = [ (t, lambda e=t: add_to_pipeline(pipeline, e, pipe_label, pipe_plot, canvas, entry)) for t in transforms ]
    frame = Frame(win)
    count = 0
    for f in funs:
        t, fun = f
        b = Button(frame, width=btn_w, height=btn_h, text=str(t), command=fun)
        b.grid(row=0,column=count)
        count += 1
    frame.pack()

    ctrl_frame = Frame(win)
    clear_btn = Button(ctrl_frame, width=btn_w, height=btn_h, text="Clear pipeline", command=lambda: clear(pipeline, pipe_label))
    clear_btn.grid(row=0, column=0)

    btn = Button(ctrl_frame, width=btn_w, height=btn_h, text='PLOT', command=lambda: plot(pipe_plot, canvas, entry, pipeline))
    btn.grid(row=0, column=1)
    ctrl_frame.pack()

    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, win)
    toolbar.update()
    canvas.get_tk_widget().pack()

    win.mainloop()

if __name__=='__main__':
    main()
