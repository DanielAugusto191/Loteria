from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb
import controlEstatisticas

# Classe para plot da estatistica do numero de acertou do usuario;
class janelaEstatistica:
    def __init__(self, window, id):
        window.resizable(0, 0)
        window.title("Estatisticas")
        self.Lf_generalStatistics = LabelFrame(window, text="Geral")
        self.Lf_generalStatistics.grid(row=0, column=0)
        self.Lf_userStatistics = LabelFrame(window, text="Usuario")
        self.Lf_userStatistics.grid(row=0, column=1)

        # Gerais
        self.Lb_mostPlayedNumber = Label(self.Lf_generalStatistics, text="Número mais jogado: ")
        self.Lb_mostPlayedNumber.grid(row=0, column=0)
        self.mostPlayedNumber = Label(self.Lf_generalStatistics, text=controlEstatisticas.mostPlayedNumber())
        self.mostPlayedNumber.grid(row=0, column=1)

        self.Lb_mostDrawnNumber = Label(self.Lf_generalStatistics, text="Número mais sorteado: ")
        self.Lb_mostDrawnNumber.grid(row=1, column=0)
        self.mostDrawnNumber = Label(self.Lf_generalStatistics, text=controlEstatisticas.mostDrawNumber())
        self.mostDrawnNumber.grid(row=1, column=1)

        self.Lb_timesPlayX = Label(self.Lf_generalStatistics, text="Quantas vezes o numero foi Jogado: ")
        self.Lb_timesPlayX.grid(row=2, column=0)
        self.timesPlayX = Entry(self.Lf_generalStatistics)
        self.timesPlayX.grid(row=2, column=1)
        self.Btn_timePlayX = Button(self.Lf_generalStatistics, text="ver", command=lambda: controlEstatisticas.timePlayX(self.timesPlayX.get()))
        self.Btn_timePlayX.grid(row=2, column=2)

        self.Lb_timesDrawX = Label(self.Lf_generalStatistics, text="Quantas vezes o numero foi sorteado: ")
        self.Lb_timesDrawX.grid(row=3, column=0)
        self.timesDrawX = Entry(self.Lf_generalStatistics)
        self.timesDrawX.grid(row=3, column=1)
        self.Btn_timesDrawX = Button(self.Lf_generalStatistics, text="ver", command=lambda: mb.showinfo("Loteria", controlEstatisticas.timeDrawX(self.timesDrawX.get())))
        self.Btn_timesDrawX.grid(row=3, column=2)

        self.Btn_percentageTotalHits = Button(self.Lf_generalStatistics, text="Porcentagem de acertos totais", command=lambda: controlEstatisticas.percentageTotalHits())
        self.Btn_percentageTotalHits.grid(row=4, column=0, columnspan=3)
        
        # User

        self.Lb_userMostPlayedNumber = Label(self.Lf_userStatistics, text="Número mais jogado por você: ")
        self.Lb_userMostPlayedNumber.grid(row=0, column=0)
        self.userMostPlayedNumber = Label(self.Lf_userStatistics, text=controlEstatisticas.userMostPlayedNumber(id))
        self.userMostPlayedNumber.grid(row=0, column=1)
        
        self.Lb_userMostDrawnNumber = Label(self.Lf_userStatistics, text="Número mais sorteado por você: ")
        self.Lb_userMostDrawnNumber.grid(row=1, column=0)
        self.userMostDrawnNumber = Label(self.Lf_userStatistics, text=controlEstatisticas.userMostDrawNumber(id))
        self.userMostDrawnNumber.grid(row=1, column=1)

        self.Lb_userTimesPlayX = Label(self.Lf_userStatistics, text="Quantas vezes o numero foi jogado por você: ")
        self.Lb_userTimesPlayX.grid(row=2, column=0)
        self.userTimesPlayX = Entry(self.Lf_userStatistics)
        self.userTimesPlayX.grid(row=2, column=1)
        self.Btn_userTimesPlayX = Button(self.Lf_userStatistics, text="Ver", command=lambda: mb.showinfo("Loteria", controlEstatisticas.userTimePlayX(self.userTimesPlayX.get(), id)))
        self.Btn_userTimesPlayX.grid(row=2, column=2)

        self.Lb_userTimesDrawX = Label(self.Lf_userStatistics, text="Quantas vezes o numero foi sorteado por você: ")
        self.Lb_userTimesDrawX.grid(row=3, column=0)
        self.userTimesDrawX = Entry(self.Lf_userStatistics)
        self.userTimesDrawX.grid(row=3, column=1)
        self.Btn_userTimesDrawX = Button(self.Lf_userStatistics, text="Ver", command=lambda: mb.showinfo("Loteria", controlEstatisticas.userDrawPlayX(self.userTimesDrawX.get(), id)))
        self.Btn_userTimesDrawX.grid(row=3, column=2)

        self.Btn_userPercentagemTotalHits = Button(self.Lf_userStatistics, text="Porcentagem de seus acertos", command=lambda: controlEstatisticas.userPercentageTotalHits(id))
        self.Btn_userPercentagemTotalHits.grid(row=4, column=0, columnspan=3)

# Caso seja preciso chama-la por outro arquivo, sem criar objetos.
def chamaEstatisticas(id):
    root = Tk()
    janelaEstatistica(root, id)
    root.mainloop()
