from turtle import color
from matplotlib import markers
import matplotlib.pyplot as graph
graph.ion()

class dinamicUpdate():
    min_x = 0
    max_x = 60

    def on_launch(self):

        self.figure, self.ax = graph.subplots()
        self.lines, = self.ax.plot([],[], ':', color = "r", label = "dT/dt")
        
        graph.xlabel("Tempo", color = "g")
        graph.ylabel("Temperatura(min)", color = "#FF00FF")
        graph.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
        graph.legend()
        graph.title("Lei do resfriamento de Newton", color = "#FF4500")


        self.ax.set_autoscaley_on(True)
        self.ax.set_xlim(self.min_x, self.max_x)

        #self.ax.grid()
        ...

    def on_running(self, xdata, ydata):

        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)

        self.ax.relim()
        self.ax.autoscale_view()

        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    def __call__(self):
        import numpy as np
        import time
        self.on_launch()
        xdata = []
        ydata = []
        for x in np.arange(1,60,0.5):
            xdata.append(x)
            ydata.append(50*np.exp(-4/3*x)+24) # Tamb + A*exp(-kt)
            self.on_running(xdata, ydata)
           # graph.scatter(xdata, ydata, marker = ",", color = "g")
            time.sleep(1)
        return xdata, ydata

grafico = dinamicUpdate()
grafico()
graph.show()

#aplicar o método racional de solução de exercícios
    #https://www.youtube.com/watch?v=z7p1GaYpvr0
    #https://www.youtube.com/watch?v=MtQ9EOV3fSE
