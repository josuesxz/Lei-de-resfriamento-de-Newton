import matplotlib.pyplot as graph
import matplotlib.lines
import numpy as np
graph.ion()
import time

class dinamicUpdate():
    min_x = 0
    max_x = 10

    def on_launch(self):
        self.figure, self.ax = graph.subplots()
        self.lines, = self.ax.plot([], [], "--")
        
        self.ax.set_autoscaley_on(True)
        self.ax.set_xlim(self.min_x, self.max_x)

        self.ax.grid()

    def on_running(self, xdata, ydata):
        self.lines.set_xdata(xdata)
        self.lines.set_ydadta(ydata)

        self.ax.relim()
        self.ax.autoscale_view()

        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    def __call__(self):
        self.on_launch()
        xdata = []
        ydata = []

        for x in np.arange(0, 10, 0.5):
            xdata.append(x)
            ydata.append(np.exp(x**2))
            self.on_running(xdata, ydata)
            time.sleep(10)
        return xdata, ydata

grafico = dinamicUpdate()
grafico()
graph.show()