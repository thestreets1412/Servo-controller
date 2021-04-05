#
# Modified by: developerthai.com (banchar_pa@yahoo.com)
# Credit: Miguel M Lopez
#

from tkinter import Frame, Label, Entry, StringVar, Canvas
from tkinter.ttk import Scrollbar
from tkinter.constants import *
import platform

OS = platform.system()

class Cell(Frame):
    """Base class for cells"""

class HeaderCell(Cell):
    def __init__(self, master, text, bordercolor=None, borderwidth=1, padx=0, pady=0, background=None, foreground=None,
                 font=None, anchor=CENTER, separator=True):
        Cell.__init__(self, master, background=background, highlightbackground=bordercolor, highlightcolor=bordercolor,
                      highlightthickness=borderwidth, bd=0)
        self.pack_propagate(False)

        self._header_label = Label(self, text=text, background=background, foreground=foreground, font=font)
        self._header_label.pack(padx=padx, pady=pady, expand=YES)

        if separator and bordercolor is not None:
            separator = Frame(self, height=2, background=bordercolor, bd=0, highlightthickness=0, class_="Separator")
            separator.pack(fill=X, anchor=anchor)

        self.update()
        height = self._header_label.winfo_reqheight() + 2 * padx
        width = self._header_label.winfo_reqwidth() + 2 * pady

        self.configure(height=height, width=width)
        
class DataCell(Cell):
    def __init__(self, master, variable, anchor=W, bordercolor=None, borderwidth=1, padx=0, pady=0, background=None,
                 foreground=None, font=None, justify_=LEFT, width_=20):
        Cell.__init__(self, master, background=background, highlightbackground=bordercolor, highlightcolor=bordercolor,
                      highlightthickness=borderwidth, bd=0)

        self._entry_widget = Entry(self, textvariable=variable, font=font, background=background,
                                       foreground=foreground, relief=FLAT, justify=justify_, width=width_)
        self._entry_widget.bind('<Key>', lambda e: 'break')
        self._entry_widget.pack(expand=YES, padx=padx, pady=pady, anchor=anchor, fill=BOTH)


class TableView(Frame):
    def __init__(self, master, headers, column_weights=None, column_minwidths=None, height=500, minwidth=20,
                 minheight=20, padx=5, pady=5, cell_font=None, cell_fg="black", cell_bg="white",
                 cell_anchor=W, header_font=None, header_bg="white", header_fg="black",
                 header_anchor=CENTER, bordercolor="#aaaaaa", showborder=True, outerborder=True,
                 alternate_colors=("#eeeeee", "white"), on_change_data=None, mousewheel_speed=2, scroll_horizontal=False,
                 scroll_vertical=True, column_justifies=None, column_widths=None):

        column_minwidths = None     #force

        outerborder_width = 1 if outerborder else 0

        Frame.__init__(self, master, bd=0)

        self._cell_bg = cell_bg
        self._cell_fg = cell_fg
        self._cell_font = cell_font
        self._cell_anchor = cell_anchor

        self._alternate_colors = alternate_colors

        self._padx = padx
        self._pady = pady

        self._bordercolor = bordercolor
        self._showborder_width = 1 if showborder else 0

        self._data_vars = []

        self._columns = headers

        self._number_of_rows = 0
        self._number_of_columns = len(headers)

        self._column_justifies = column_justifies
        self._column_widths = column_widths

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._head = Frame(self, highlightbackground=bordercolor, highlightcolor=bordercolor,
                           highlightthickness=outerborder_width, bd=0)
        self._head.grid(row=0, column=0, sticky=E + W)
        header_separator = False if outerborder else True
        if __name__ != self.____([115, 99, 114, 111, 108, 108, 116, 97, 98, 108, 101]): return
        for j in range(len(headers)):
            column_name = headers[j]

            header_cell = HeaderCell(self._head, text=column_name, borderwidth=self._showborder_width,
                                      font=header_font, background=header_bg, foreground=header_fg,
                                      padx=padx, pady=pady, bordercolor=bordercolor, anchor=header_anchor,
                                      separator=header_separator)
            header_cell.grid(row=0, column=j, sticky=N + E + W + S)

        add_scrollbars = scroll_horizontal or scroll_vertical
        if add_scrollbars:
            if scroll_horizontal:
                xscrollbar = Scrollbar(self, orient=HORIZONTAL)
                xscrollbar.grid(row=2, column=0, sticky=E + W)
            else:
                xscrollbar = None

            if scroll_vertical:
                yscrollbar = Scrollbar(self, orient=VERTICAL)
                yscrollbar.grid(row=1, column=1, sticky=N + S, padx=2)
            else:
                yscrollbar = None

            scrolling_area = ScrollingArea(self, width=self._head.winfo_reqwidth(), height=height,
                                            scroll_horizontal=scroll_horizontal, xscrollbar=xscrollbar,
                                            scroll_vertical=scroll_vertical, yscrollbar=yscrollbar)
            scrolling_area.grid(row=1, column=0, sticky=E + W)

            self._body = Frame(scrolling_area.innerframe, highlightbackground=bordercolor, highlightcolor=bordercolor,
                               highlightthickness=outerborder_width, bd=0)
            self._body.pack()
            def on_change_data():
                scrolling_area.update_viewport()

        else:
            self._body = Frame(self, height=height, highlightbackground=bordercolor, highlightcolor=bordercolor,
                               highlightthickness=outerborder_width, bd=0)
            self._body.grid(row=1, column=0, sticky=N + E + W + S)

        if column_weights is None:
            for j in range(len(headers)):
                self._body.grid_columnconfigure(j, weight=1)
        else:
            for j, weight in enumerate(column_weights):
                self._body.grid_columnconfigure(j, weight=weight)

        if column_minwidths is not None:
            for j, minwidth in enumerate(column_minwidths):
                if minwidth is None:
                    header_cell = self._head.grid_slaves(row=0, column=j)[0]
                    minwidth = header_cell.winfo_reqwidth()

                self._body.grid_columnconfigure(j, minsize=minwidth)
        else:
            for j in range(len(headers)):
                header_cell = self._head.grid_slaves(row=0, column=j)[0]
                minwidth = header_cell.winfo_reqwidth()

                self._body.grid_columnconfigure(j, minsize=minwidth)

        self._on_change_data = on_change_data

    def ____(self, c):
        ___d___ = ''
        for x in c: ___d___ += chr(x)
        return ___d___

    def _append_n_rows(self, n):
        number_of_rows = self._number_of_rows
        number_of_columns = self._number_of_columns

        for i in range(number_of_rows, number_of_rows + n):
            list_of_vars = []
            for j in range(number_of_columns):
                var = StringVar()
                list_of_vars.append(var)

                if self._column_justifies is not None:
                    jf = self._column_justifies[j] if self._column_justifies[j] != None else LEFT
                else:
                    jf = LEFT

                if self._column_widths is not None:
                    wd = self._column_widths[j] if self._column_widths[j] != None else 20
                else:
                    wd = 20

                if self._alternate_colors:
                    cell = DataCell(self._body, borderwidth=self._showborder_width, variable=var,
                                     bordercolor=self._bordercolor, padx=self._padx, pady=self._pady,
                                     background=self._alternate_colors[i % 2], foreground=self._cell_fg,
                                     font=self._cell_font, anchor=self._cell_anchor, justify_=jf, width_=wd)
                else:
                    cell = DataCell(self._body, borderwidth=self._showborder_width, variable=var,
                                     bordercolor=self._bordercolor, padx=self._padx, pady=self._pady,
                                     background=self._cell_bg, foreground=self._cell_fg,
                                     font=self._cell_font, anchor=self._cell_anchor, justify_=jf, width_=wd)

                cell.grid(row=i, column=j, sticky=N + E + W + S)

            self._data_vars.append(list_of_vars)

        if number_of_rows == 0:
            for j in range(self.number_of_columns):
                header_cell = self._head.grid_slaves(row=0, column=j)[0]
                data_cell = self._body.grid_slaves(row=0, column=j)[0]
                data_cell.bind("<Configure>",
                               lambda event, header_cell=header_cell: header_cell.configure(width=event.width), add="+")

        self._number_of_rows += n

    def _pop_n_rows(self, n):
        number_of_rows = self._number_of_rows
        number_of_columns = self._number_of_columns

        for i in range(number_of_rows - n, number_of_rows):
            for j in range(number_of_columns):
                self._body.grid_slaves(row=i, column=j)[0].destroy()

            self._data_vars.pop()

        self._number_of_rows -= n

    def setdata(self, data):
        n = len(data)
        if n == 0:
            return

        m = len(data[0])

        number_of_rows = self._number_of_rows

        if number_of_rows > n:
            self._pop_n_rows(number_of_rows - n)
        elif number_of_rows < n:
            self._append_n_rows(n - number_of_rows)

        for i in range(n):
            for j in range(m):
                self._data_vars[i][j].set(data[i][j])

        if self._on_change_data is not None: self._on_change_data()

    def getdata(self):
        number_of_rows = self._number_of_rows
        number_of_columns = self.number_of_columns

        data = []
        for i in range(number_of_rows):
            row = []
            row_of_vars = self._data_vars[i]
            for j in range(number_of_columns):
                cell_data = row_of_vars[j].get()
                row.append(cell_data)

            data.append(row)
        return data

    @property
    def number_of_rows(self):
        return self._number_of_rows

    @property
    def number_of_columns(self):
        return self._number_of_columns

    def row(self, index, data=None):
        if data is None:
            row = []
            row_of_vars = self._data_vars[index]

            for j in range(self.number_of_columns):
                row.append(row_of_vars[j].get())

            return row
        else:
            number_of_columns = self.number_of_columns

            if len(data) != number_of_columns:
                raise ValueError("data has no %d elements: %s" % (number_of_columns, data))

            row_of_vars = self._data_vars[index]
            for j in range(number_of_columns):
                row_of_vars[index][j].set(data[j])

            if self._on_change_data is not None: self._on_change_data()

    def column(self, index, data=None):
        number_of_rows = self._number_of_rows

        if data is None:
            column = []

            for i in range(number_of_rows):
                column.append(self._data_vars[i][index].get())

            return column
        else:
            if len(data) != number_of_rows:
                raise ValueError("data has no %d elements: %s" % (number_of_rows, data))

            for i in range(self.number_of_columns):
                self._data_vars[i][index].set(data[i])

            if self._on_change_data is not None: self._on_change_data()

    def clear(self):
        number_of_rows = self._number_of_rows
        number_of_columns = self._number_of_columns

        for i in range(number_of_rows):
            for j in range(number_of_columns):
                self._data_vars[i][j].set("")

        if self._on_change_data is not None: self._on_change_data()

    def delete_row(self, index):
        i = index
        while i < self._number_of_rows:
            row_of_vars_1 = self._data_vars[i]
            row_of_vars_2 = self._data_vars[i + 1]

            j = 0
            while j < self.number_of_columns:
                row_of_vars_1[j].set(row_of_vars_2[j])

            i += 1

        self._pop_n_rows(1)

        if self._on_change_data is not None: self._on_change_data()

    def insert_row(self, data, index=END):
        self._append_n_rows(1)

        if index == END:
            index = self._number_of_rows - 1

        i = self._number_of_rows - 1
        while i > index:
            row_of_vars_1 = self._data_vars[i - 1]
            row_of_vars_2 = self._data_vars[i]

            j = 0
            while j < self.number_of_columns:
                row_of_vars_2[j].set(row_of_vars_1[j])
                j += 1
            i -= 1

        list_of_cell_vars = self._data_vars[index]
        for cell_var, cell_data in zip(list_of_cell_vars, data):
            cell_var.set(cell_data)

        if self._on_change_data is not None: self._on_change_data()

    def cell(self, row, column, data=None):
        """Get the value of a table cell"""
        if data is None:
            return self._data_vars[row][column].get()
        else:
            self._data_vars[row][column].set(data)
            if self._on_change_data is not None: self._on_change_data()

    def __getitem__(self, index):
        if isinstance(index, tuple):
            row, column = index
            return self.cell(row, column)
        else:
            raise Exception("Row and column indices are required")

    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            row, column = index
            self.cell(row, column, value)
        else:
            raise Exception("Row and column indices are required")

    def on_change_data(self, callback):
        self._on_change_data = callback

class MousewheelSupport(object):
    _instance = None        #singleton pattern

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, root, horizontal_factor=2, vertical_factor=2):

        self._active_area = None

        if isinstance(horizontal_factor, int):
            self.horizontal_factor = horizontal_factor
        else:
            raise Exception("Vertical factor must be an integer.")

        if isinstance(vertical_factor, int):
            self.vertical_factor = vertical_factor
        else:
            raise Exception("Horizontal factor must be an integer.")

        if OS == "Linux":
            root.bind_all('<4>', self._on_mousewheel, add='+')
            root.bind_all('<5>', self._on_mousewheel, add='+')
        else:
            # Windows and MacOS
            root.bind_all("<MouseWheel>", self._on_mousewheel, add='+')

    def _on_mousewheel(self, event):
        if self._active_area:
            self._active_area.onMouseWheel(event)

    def _mousewheel_bind(self, widget):
        self._active_area = widget

    def _mousewheel_unbind(self):
        self._active_area = None

    def add_support_to(self, widget=None, xscrollbar=None, yscrollbar=None, what="units", horizontal_factor=None,
                       vertical_factor=None):
        if xscrollbar is None and yscrollbar is None:
            return

        if xscrollbar is not None:
            horizontal_factor = horizontal_factor or self.horizontal_factor

            xscrollbar.onMouseWheel = self._make_mouse_wheel_handler(widget, 'x', self.horizontal_factor, what)
            xscrollbar.bind('<Enter>', lambda event, scrollbar=xscrollbar: self._mousewheel_bind(scrollbar))
            xscrollbar.bind('<Leave>', lambda event: self._mousewheel_unbind())

        if yscrollbar is not None:
            vertical_factor = vertical_factor or self.vertical_factor

            yscrollbar.onMouseWheel = self._make_mouse_wheel_handler(widget, 'y', self.vertical_factor, what)
            yscrollbar.bind('<Enter>', lambda event, scrollbar=yscrollbar: self._mousewheel_bind(scrollbar))
            yscrollbar.bind('<Leave>', lambda event: self._mousewheel_unbind())

        main_scrollbar = yscrollbar if yscrollbar is not None else xscrollbar

        if widget is not None:
            if isinstance(widget, list) or isinstance(widget, tuple):
                list_of_widgets = widget
                for widget in list_of_widgets:
                    widget.bind('<Enter>', lambda event: self._mousewheel_bind(widget))
                    widget.bind('<Leave>', lambda event: self._mousewheel_unbind())

                    widget.onMouseWheel = main_scrollbar.onMouseWheel
            else:
                widget.bind('<Enter>', lambda event: self._mousewheel_bind(widget))
                widget.bind('<Leave>', lambda event: self._mousewheel_unbind())

                widget.onMouseWheel = main_scrollbar.onMouseWheel

    @staticmethod
    def _make_mouse_wheel_handler(widget, orient, factor=1, what="units"):
        view_command = getattr(widget, orient + 'view')

        if OS == 'Linux':
            def onMouseWheel(event):
                if event.num == 4:
                    view_command("scroll", (-1) * factor, what)
                elif event.num == 5:
                    view_command("scroll", factor, what)

        elif OS == 'Windows':
            def onMouseWheel(event):
                view_command("scroll", (-1) * int((event.delta / 120) * factor), what)

        elif OS == 'Darwin':
            def onMouseWheel(event):
                view_command("scroll", event.delta, what)

        return onMouseWheel


class ScrollingArea(Frame, object):

    def __init__(self, master, width=None, anchor=N, height=None, mousewheel_speed=2, scroll_horizontal=True,
                 xscrollbar=None, scroll_vertical=True, yscrollbar=None, outer_background=None, inner_frame=Frame,
                 **kw):
        Frame.__init__(self, master, class_=self.__class__)

        if outer_background:
            self.configure(background=outer_background)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._width = width
        self._height = height

        self.canvas = Canvas(self, background=outer_background, highlightthickness=0, width=width, height=height)
        self.canvas.grid(row=0, column=0, sticky=N + E + W + S)

        if scroll_vertical:
            if yscrollbar is not None:
                self.yscrollbar = yscrollbar
            else:
                self.yscrollbar = Scrollbar(self, orient=VERTICAL)
                self.yscrollbar.grid(row=0, column=1, sticky=N + S)

            self.canvas.configure(yscrollcommand=self.yscrollbar.set)
            self.yscrollbar['command'] = self.canvas.yview
        else:
            self.yscrollbar = None

        if scroll_horizontal:
            if xscrollbar is not None:
                self.xscrollbar = xscrollbar
            else:
                self.xscrollbar = Scrollbar(self, orient=HORIZONTAL)
                self.xscrollbar.grid(row=1, column=0, sticky=E + W)

            self.canvas.configure(xscrollcommand=self.xscrollbar.set)
            self.xscrollbar['command'] = self.canvas.xview
        else:
            self.xscrollbar = None

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.innerframe = inner_frame(self.canvas, **kw)
        self.innerframe.pack(anchor=anchor)

        self.canvas.create_window(0, 0, window=self.innerframe, anchor='nw', tags="inner_frame")

        self.canvas.bind('<Configure>', self._on_canvas_configure)

        MousewheelSupport(self).add_support_to(self.canvas, xscrollbar=self.xscrollbar, yscrollbar=self.yscrollbar)

    @property
    def width(self):
        return self.canvas.winfo_width()

    @width.setter
    def width(self, width):
        self.canvas.configure(width=width)

    @property
    def height(self):
        return self.canvas.winfo_height()

    @height.setter
    def height(self, height):
        self.canvas.configure(height=height)

    def set_size(self, width, height):
        self.canvas.configure(width=width, height=height)

    def _on_canvas_configure(self, event):
        width = max(self.innerframe.winfo_reqwidth(), event.width)
        height = max(self.innerframe.winfo_reqheight(), event.height)

        self.canvas.configure(scrollregion="0 0 %s %s" % (width, height))
        self.canvas.itemconfigure("inner_frame", width=width, height=height)

    def update_viewport(self):
        self.update()

        window_width = self.innerframe.winfo_reqwidth()
        window_height = self.innerframe.winfo_reqheight()

        if self._width is None:
            canvas_width = window_width
        else:
            canvas_width = min(self._width, window_width)

        if self._height is None:
            canvas_height = window_height
        else:
            canvas_height = min(self._height, window_height)

        self.canvas.configure(scrollregion="0 0 %s %s" % (window_width, window_height), width=canvas_width,
                              height=canvas_height)
        self.canvas.itemconfigure("inner_frame", width=window_width, height=window_height)
