import pandas
from tkinter import *


bg = '#011F26'
button_bg = '#024073'


def buscar():
    top2 = Tk()
    top2.geometry('600x300')
    top2.title('Busca')
    top2.config(bg=bg)

    busqar = Label(top2, text='PROCURAR PLACA', bg=bg, fg='#FFFFFF').place(x=220, y=10+60)
    PLACA = Label(top2, text='Placa ', bg=bg, fg='#FFFFFF').place(x=170, y=50+60)
    Placa = Entry(top2, width=30)
    Placa.place(x=220, y=50+60)

    def procurar():
        global portaria
        placa = Placa.get()
        for c in range(0, len(portaria['Placa'])):
            if placa == portaria['Placa'][c]:
                HORA = Label(top2, text='Saída ', bg=bg, fg='#FFFFFF').place(x=170, y=110+60)
                Hora = Entry(top2, width=30)
                Hora.place(x=220, y=110+60)

                def mudasaida():
                    hora = Hora.get()
                    portaria['Saída'][c] = hora
                    portaria.to_excel(r'C:\Users\User\Desktop\portaria.xlsx')

                sair = Button(top2, text='Registrar saída', command=mudasaida)
                portaria.to_excel(r'C:\Users\User\Desktop\portaria.xlsx')
                sair.place(x=220, y=140+60)

        portaria.to_excel(r'C:\Users\User\Desktop\portaria.xlsx')

    buscador = Button(top2, text='Buscar', command=procurar)
    buscador.place(x=220, y=80+60)


def anotar():
    top1 = Tk()
    top1.title('Anotar')
    top1.geometry('1000x500')
    top1.config(bg='#011F26')

    xl = 350
    xe = 420

    anota = Label(top1, text='ANOTAR VISITANTES', bg=bg, fg='#FFFFFF').place(x=450, y=40)
    motorista = Label(top1, text='MOTORISTA', bg=bg, fg='#FFFFFF').place(x=xl, y=20+70)
    NOME = Label(top1, text='Nome ', bg='#011F26', fg='#FFFFFF').place(x=xl, y=50+70)
    nome = Entry(top1, width=30)
    nome.place(x=xe, y=50+70)

    CPF = Label(top1, text='Identidade ', bg='#011F26', fg='#FFFFFF').place(x=xl, y=80+70)
    cpf = Entry(top1, width=30)
    cpf.place(x=xe, y=80+70)

    PLACA = Label(top1, text='Placa ', bg='#011F26', fg='#FFFFFF').place(x=xl, y=110+70)
    placa = Entry(top1, width=30)
    placa.place(x=xe, y=110+70)

    DESTINO = Label(top1, text='Destino ', bg='#011F26', fg='#FFFFFF').place(x=xl, y=140+70)
    destino = Entry(top1, width=30)
    destino.place(x=xe, y=140+70)

    ENTRADA = Label(top1, text='Entrada ', bg='#011F26', fg='#FFFFFF').place(x=xl, y=170+70)
    entrada = Entry(top1, width=30)
    entrada.place(x=xe, y=170+70)


    def cadastra():
        global portaria
        Nome = nome.get()
        Cpf = cpf.get()
        Placa = placa.get()
        Destino = destino.get()
        Entrada = entrada.get()

        new_person = [Nome, Cpf, Placa, Destino, Entrada, '-']
        portaria.loc[len(portaria)] = new_person
        portaria.to_excel(r'C:\Users\User\Desktop\portaria.xlsx')

    def passageiros():
        NAME = Label(top1, text='Nome ', bg=bg, fg='#FFFFFF').place(x=xl, y=290+70)
        name = Entry(top1, width=30)
        name.place(x=xe, y=290+70)


        def registra():
            global portaria
            Name = name.get()
            Cpf = '-'
            Placa = placa.get()
            Destino = destino.get()
            Entrada = entrada.get()

            new_person = [Name, Cpf, Placa, Destino, Entrada, '-']
            portaria.loc[len(portaria)] = new_person
            portaria.to_excel(r'C:\Users\User\Desktop\portaria.xlsx')
            passageiros()


        cadastraP = Button(top1, text='Cadastrar', command=registra)
        cadastraP.place(x=xe, y=390)


    visita = Label(top1, text='PASSAGEIROS', bg='#011F26', fg='#FFFFFF').place(x=xl, y=260+70)
    passageiros()

    cadastrar = Button(top1, text='Cadastrar motorista', command=cadastra)
    cadastrar.place(x=xe, y=200+70)


if __name__ == '__main__':
    portaria = pandas.DataFrame(columns=['Nome', 'Identidade', 'Placa', 'Motivo/Destino', 'Entrada', 'Saída'])

    tp = Tk()
    tp.title('Opções')

    largura = 600
    altura = 330
    bg = '#011F26'
    button_bg = '#024073'

    tp.geometry(f'{largura}x{altura}')
    tp.config(bg=bg)

    apresentar = Label(text='PORTARIA ELETRÔNICA', bg=bg, fg='#FFFFFF').place(x=largura/4, y=int(altura/100*7.5), width=300)

    op1 = Button(tp, text='Anotar', command=anotar)
    op1.place(x=150, y=100, width=300, height=70)
    op1.config(bg=button_bg, fg='#FFFFFF')

    op2 = Button(tp, text='Buscar', command=buscar)
    op2.place(x=150, y=180, width=300, height=70)
    op2.config(bg='#024073', fg='#FFFFFF')

    portaria.to_excel(r'C:\Users\User\Desktop\portaria.xlsx')
    tp.mainloop()
