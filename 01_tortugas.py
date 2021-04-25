import turtle
import random

class Circuito():
    corredores = []
    __posStartY = (-45, -15, 15, 45)
    __colorTurtle = ("red","blue","green","orange")
    
    def __init__(self,width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightgray")
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20
        self.__createRunner()
        
    def __createRunner(self):
        #Esta loop crea los corredores y los incluye en la lista corredores.
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape("turtle")
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            
            self.corredores.append(new_turtle)
            
    def competir(self):
        hayGanador = False
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6)
                tortuga.fd(avance)
            
                if tortuga.xcor() >= self.__finishLine:
                    hayGanador = True
                    print("La tortuga de color {} ha ganado".format(tortuga.color()[0]))
                    break
                
        
if __name__ ==  "__main__":
    circuito = Circuito(640, 480)
    circuito.competir()