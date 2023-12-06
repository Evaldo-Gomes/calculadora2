import PySimpleGUI as psg
import calc2
from calc2 import soma

layout = [
            [psg.Text('Informe N1: '), psg.InputText(key='Num1')],
            [psg.Text('Informe N2: '), psg.InputText(key='Num2')],
            [psg.Text('Operações'), psg.Button(' + '), psg.Button(' - '), psg.Button(' * '), psg.Button(' / '), psg.Button(' Rad '),psg.Text('Somente N1!')],
            [psg.Text('*******'), psg.Text('', key='total'), psg.Text('*******')],
            #[psg.Button('Calcular'), psg.Button('Limpar')]
            [psg.Button('Limpar')]
            ]

janela = psg.Window('Calculadora Simples', layout)

while True:
    evento, valores = janela.read()
    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'Limpar':
        janela['Num1'].update('')
        janela['Num2'].update('')
        janela['total'].update('')
        janela['Num1'].set_focus()
    elif evento == ' + ':
        num1 = int(valores['Num1'])
        num2 = int(valores['Num2'])
        janela['total'].update(calc2.soma(num1, num2))
    elif evento == ' - ':
        num1 = int(valores['Num1'])
        num2 = int(valores['Num2'])
        janela['total'].update(calc2.sub(num1, num2))
    elif evento == ' * ':
        num1 = int(valores['Num1'])
        num2 = int(valores['Num2'])
        janela['total'].update(calc2.mult(num1, num2))
    elif evento == ' / ':
        num1 = int(valores['Num1'])
        num2 = int(valores['Num2'])
        janela['total'].update(calc2.div(num1, num2))
    elif evento == ' Rad ':
        num1 = int(valores['Num1'])
        janela['total'].update(calc2.rad(num1))
janela.close()

