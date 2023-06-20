import PySimpleGUI as sg

layout = [
    [sg.Input('', key='-DISPLAY-',size=(10,1))],
    [sg.B('7'),sg.B('8'),sg.B('9'),sg.B('/')],
    [sg.B('4'),sg.B('5'),sg.B('6'),sg.B('*')],
    [sg.B('1'),sg.B('2'),sg.B('3'),sg.B('-')],
    [sg.B('.'),sg.B('0'),sg.B('='),sg.B('+')],
]

janela = sg.Window('Calc 3ia', layout=layout, font="monospace 30",)

while True:
  event, values = janela.read()
  
  class App():
    def _init_(self):
      self.result = 0 
      self.oper = ''
      self.window.read(timeout=1) #é o tempo para reler o layout
  
  def resulter(self):
    if self.oper == '+':
      return float(self.result) + float(sg.B['-DISPLAY-'])
    if self.oper == '-':
      return float(self.result) - float(sg.B['-DISPLAY-'])
    if self.oper == '*':
      return float(self.result) * float(sg.B['-DISPLAY-'])
    if self.oper == '/':
      return float(self.result) / float(sg.B['-DISPLAY-'])
  
  if event == sg.WIN_CLOSED:
    break
