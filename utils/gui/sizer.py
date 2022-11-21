
class Sizer:
    def __init__(self, win):
        self.win = win 

    def size(self, to_w, to_h, perc_w, perc_h=None):
        if not perc_h:
            perc_h = perc_w
        return (int(to_w * perc_w), int(to_h * perc_h))

    def size_scr(self, perc_w, perc_h=None):
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        return self.size(width, height, perc_w, perc_h)

    def size_win(self, perc_w, perc_h=None):
        width = self.win.winfo_width()
        height = self.win.winfo_height()
        return self.size(width, height, perc_w, perc_h)
        

