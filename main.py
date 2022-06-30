from tkinter import *
from tkinter import ttk, messagebox
from urllib.request import urlopen
import json

class Dolar:
    __resultado = None

    def __init__(self):
        self.__resultado = None

    def run(self):
        url = "https://www.dolarsi.com/api/api.php?type=dolar"
        response = urlopen(url)
        self.__resultado = json.loads(response.read().decode())

    def getResultado(self):
        return self.__resultado

    def getPrecio(self):
        precio=float(self.__resultado[0]['casa']['venta'].replace(',','.'))
        return precio

class Aplicacion:
    __ventana = None
    __Peso = None
    __Dolar = None

    def __init__(self):
        dolar = Dolar()
        dolar.run()
        self.__ventana = Tk()
        self.__ventana.geometry('290x100')
        self.__ventana.title('Conversor de moneda')
        self.__ventana.resizable(0, 0)

        self.__Peso = StringVar()
        self.__Dolar = StringVar()
        self.__Dolar.trace('w',self.CalcularPeso)

        mainframe = ttk.Frame(self.__ventana)
        mainframe.grid(column=0, row=1, columnspan=2)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe["borderwidth"]=2
        mainframe["relief"]="groove"

        ttk.Label(mainframe, text="dolares").grid(column=3, row=0)
        self.dolarEntry=ttk.Entry(mainframe, width=7, textvariable=self.__Dolar)
        self.dolarEntry.grid(column=2,row=0,sticky=(W, E))

        ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=1)
        ttk.Label(mainframe, textvariable=self.__Peso).grid(column=2,row=1,sticky=(W, E))
        ttk.Label(mainframe, text="pesos").grid(column=3, row=1)

        ttk.Button(mainframe, text='Salir',command=self.__ventana.destroy).grid(column=3,row=3)

        self.dolarEntry.focus()
        self.__ventana.mainloop()

    def CalcularPeso(self,*args):
        if self.dolarEntry.get() != '':
            try:
                valorD=float(self.dolarEntry.get())
                self.__Peso.set(valorD*dolar.getPrecio())
            except ValueError:
                messagebox.showerror(er='Error de tipo', message='Solo ingresar numeros')
        else:
            self.__Peso.set('')


if __name__ == '__main__':
    miApp=Aplicacion()