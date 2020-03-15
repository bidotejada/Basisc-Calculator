
import tkinter as tk
from math import pi as π, sqrt, degrees, radians, sin, cos, tan, log10 as Log


def SIN(x):
    return eval(f'{sin(radians(x)):.3f}')


def COS(x):
    return eval(f'{cos(radians(x)):.3f}')


def TAN(x):
    return eval(f'{tan(radians(x)):.3f}')


'''add degre/radian radial button later for added complexity'''


class Calc:
    '''equals for button with handled execptions'''

    def equals_(self):
        self.historyadd = ''
        try:
            if self.hisotryDisplay.get() == '':
                pass
            else:
                self.historyadd = self.hisotryDisplay.get()

            if self.entry.get() == '':
                pass
            elif self.historyadd == '':
                self.expressionDisplay.set(self.entry.get())
                self.hisotryDisplay.set(
                    f'{self.entry.get()} : {eval(self.expressionDisplay.get())}')
            else:
                self.hisotryDisplay.set(
                    f'{self.hisotryDisplay.get()}\n{self.entry.get()} : {eval(self.entry.get())}')
                # self.hisotryDisplay.set(f'{self.expressionDisplay.get()}: {self.outputDisplay.get()}')
            self.expressionDisplay.set(self.entry.get())
            self.outputDisplay.set(f'{eval(self.entry.get())}')

        except ZeroDivisionError:
            self.expressionDisplay.set('Cannot divide by zero')
        except SyntaxError:
            if self.entry.get() == '':
                pass
            else:
                self.expressionDisplay.set(SyntaxError.__name__)
        except NameError:
            self.expressionDisplay.set('ValueError')
        '''new history to add to new line function'''

    def clear(self):
        self.expressionDisplay.set('')
        self.entry.delete(0, 'end')

    def reset(self):
        self.master_window.after(0000)  # millisecond
        self.expressionDisplay.set('')
        self.outputDisplay.set('')
        self.hisotryDisplay.set('')

    def __init__(self):
        self.master_window = tk.Tk()  # create main window widget
        self.master_window.geometry('300x300')
        self.master_window.title('Calculator')

        self.expressionDisplay = tk.StringVar()  # shows input on label field
        self.outputDisplay = tk.StringVar()  # shows results on entry field
        self.hisotryDisplay = tk.StringVar()
        '''history frame and contents'''
        tk.Button(self.master_window, text='reset',
                  command=lambda: eval(f'{self.reset()}')).pack()
        self.historyframe = tk.Frame(self.master_window)
        self.historyframe.pack(side='left')
        self.historylabel = tk.Label(
            self.historyframe, text='History').pack(side='top')
        self.historycontent = tk.Label(
            self.historyframe, textvariable=self.hisotryDisplay).pack(side='bottom')
        # self.hisotryDisplay.set('hello world')
        '''creating frames'''

        self.expressionframe = tk.Frame(self.master_window)
        self.label = tk.Label(
            self.expressionframe, justify='right', textvariable=self.expressionDisplay)
        self.label.pack()  # padx=10,pady=10
        self.expressionframe.pack()

        self.entryframe = tk.Frame(self.master_window)
        self.entry = tk.Entry(self.entryframe, justify='right',
                              textvariable=self.outputDisplay)
        self.entry.pack()
        self.entryframe.pack()

        self.frame2 = tk.Frame(self.master_window)
        self.C = tk.Button(
            self.frame2, text='C', command=lambda: self.clear(), width=16).pack(side='left')
        self.plus = tk.Button(
            self.frame2, text='+', command=lambda: self.entry.insert('end', '+'), width=5).pack(side='left')
        self.frame2.pack()

        self.frame3 = tk.Frame(self.master_window)
        self.but7 = tk.Button(self.frame3, text='7', command=lambda: self.entry.insert(
            'end', '7'), width=5).pack(side='left')

        self.but8 = tk.Button(self.frame3, text='8', command=lambda: self.entry.insert(
            'end', '8'), width=5).pack(side='left')

        self.but9 = tk.Button(self.frame3, text='9', command=lambda: self.entry.insert(
            'end', '9'), width=5).pack(side='left')
        self.minus = tk.Button(
            self.frame3, text='-', command=lambda: self.entry.insert('end', '-'), width=5).pack(side='left')
        self.frame3.pack()

        self.frame4 = tk.Frame(self.master_window)
        self.but4 = tk.Button(self.frame4, text='4', command=lambda: self.entry.insert(
            'end', '4'), width=5).pack(side='left')

        self.but5 = tk.Button(self.frame4, text='5', command=lambda: self.entry.insert(
            'end', '5'), width=5).pack(side='left')

        self.but6 = tk.Button(self.frame4, text='6', command=lambda: self.entry.insert(
            'end', '6'), width=5).pack(side='left')

        self.multi = tk.Button(self.frame4, text='x', command=lambda: self.entry.insert(
            'end', '*'), width=5).pack(side='left')
        self.frame4.pack()

        self.frame5 = tk.Frame(self.master_window)
        self.but1 = tk.Button(self.frame5, text='1', command=lambda: self.entry.insert(
            'end', '1'), width=5).pack(side='left')

        self.but2 = tk.Button(self.frame5, text='2', command=lambda: self.entry.insert(
            'end', '2'), width=5).pack(side='left')

        self.but3 = tk.Button(self.frame5, text='3', command=lambda: self.entry.insert(
            'end', '3'), width=5).pack(side='left')

        self.div = tk.Button(self.frame5, text='÷', command=lambda: self.entry.insert(
            'end', '/'), width=5).pack(side='left')
        self.frame5.pack()

        self.frame6 = tk.Frame(self.master_window)
        self.but0 = tk.Button(self.frame6, text='0', command=lambda: self.entry.insert(
            'end', '0'), width=5).pack(side='left')

        self.deci = tk.Button(self.frame6, text='.', command=lambda: self.entry.insert(
            'end', '.'), width=5).pack(side='left')

        self.equal = tk.Button(
            self.frame6, text='=', command=lambda: self.equals_(), width=11).pack(side='left')
        self.frame6.pack()

        self.frame7 = tk.Frame(self.master_window)
        self.startPar = tk.Button(self.frame7, text='(', command=lambda: self.entry.insert(
            'end', '('), width=4).pack(side='left')

        self.endPar = tk.Button(self.frame7, text=')', command=lambda: self.entry.insert(
            'end', ')'), width=4).pack(side='left')

        self.expo = tk.Button(self.frame7, text='x^', command=lambda: self.entry.insert(
            'end', '**'), width=4).pack(side='left')

        self.sqroot = tk.Button(self.frame7, text='√', command=lambda: self.entry.insert(
            'end', 'sqrt('), width=4).pack(side='left')

        self.Pi = tk.Button(self.frame7, text='π', command=lambda: self.entry.insert(
            'end', 'π'), width=4).pack(side='left')
        self.frame7.pack()
        '''end frames'''
        self.frame8 = tk.Frame(self.master_window)
        self.sine = tk.Button(self.frame8, text='SIN', width=4, command=lambda: self.entry.insert(
            'end', 'SIN(')).pack(side='left')
        self.cosine = tk.Button(self.frame8, text='COS', width=4, command=lambda: self.entry.insert(
            'end', 'COS(')).pack(side='left')
        self.tangent = tk.Button(self.frame8, text='TAN', width=4, command=lambda: self.entry.insert(
            'end', 'TAN(')).pack(side='left')
        self.absValue = tk.Button(self.frame8, text='|x|', width=4, command=lambda: self.entry.insert(
            'end', 'abs(')).pack(side='left')
        self.log_ = tk.Button(self.frame8, text='LOG', width=4, command=lambda: self.entry.insert(
            'end', 'Log(')).pack(side='left')
        self.frame8.pack()

        self.master_window.mainloop()  # enter tkinter mainloop


calc = Calc()
#
