from tkinter import *

preto = '#000000'
branco = '#ffffff'
cinza_e = '#333333'
cinza_c = '#696969'
laranja = '#ad8328'

expressao = ""

def executar_logica(tecla):
    global expressao
    
    if tecla == 'AC':
        expressao = ""
    elif tecla == '⌫':
        expressao = expressao[:-1]
    elif tecla == '=':
        try:
            conta = expressao.replace('X', '*').replace('÷', '/')
            resultado = eval(conta)
            expressao = str(resultado)
        except:
            expressao = "Erro"
    else:
        if len(expressao) < 12:
            expressao += str(tecla)

    tela.config(text=expressao)

display = Tk()
display.title('Calculadora')
display.geometry('480x640')
display.config(bg=preto)
display.resizable(False, False)

pixel = PhotoImage(width = 1, height = 1)

area_conta = Frame(display, width = 480, height = 140, bg = preto)
area_conta.grid(row = 0, column = 0)
area_conta.grid_propagate(False)

area_botoes = Frame(display, width = 480, height = 500, bg = preto)
area_botoes.grid(row = 1, column = 0)
area_botoes.grid_propagate(False)

tela = Label(area_conta, text = '', image = pixel, compound = 'center', width = 460, height = 140, bg = preto, fg = branco, font = ('SF Pro Display', 45), anchor = 'e')
tela.place(x = 0, y = 0)

def criar_botao(texto, x, y, cor, largura=116, comando = None):
    btn  =  Button(area_botoes, text = texto, image = pixel, compound = "center", width = largura, height = 96, font = ('SF Pro Display', 30, 'bold'), bg = cor, fg = branco, relief = RIDGE, command = comando)
    btn.place(x = x, y = y)
    return btn

criar_botao('⌫', 0, 0, cinza_c, comando = lambda: executar_logica('⌫'))
criar_botao('AC', 120, 0, cinza_c, comando = lambda: executar_logica('AC'))
criar_botao('%', 240, 0, cinza_c, comando = lambda: executar_logica('%'))
criar_botao('÷', 360, 0, laranja, comando = lambda: executar_logica('÷'))

criar_botao('7', 0, 100, cinza_e, comando = lambda: executar_logica('7'))
criar_botao('8', 120, 100, cinza_e, comando = lambda: executar_logica('8'))
criar_botao('9', 240, 100, cinza_e, comando = lambda: executar_logica('9'))
criar_botao('X', 360, 100, laranja, comando = lambda: executar_logica('X'))

criar_botao('4', 0, 200, cinza_e, comando = lambda: executar_logica('4'))
criar_botao('5', 120, 200, cinza_e, comando = lambda: executar_logica('5'))
criar_botao('6', 240, 200, cinza_e, comando = lambda: executar_logica('6'))
criar_botao('-', 360, 200, laranja, comando = lambda: executar_logica('-'))

criar_botao('1', 0, 300, cinza_e, comando = lambda: executar_logica('1'))
criar_botao('2', 120, 300, cinza_e, comando = lambda: executar_logica('2'))
criar_botao('3', 240, 300, cinza_e, comando = lambda: executar_logica('3'))
criar_botao('+', 360, 300, laranja, comando = lambda: executar_logica('+'))

criar_botao('0', 0, 400, cinza_e, largura = 236, comando = lambda: executar_logica('0'))
criar_botao('.', 240, 400, cinza_e, comando = lambda: executar_logica('.'))
criar_botao('=', 360, 400, laranja, comando = lambda: executar_logica('='))

display.mainloop()