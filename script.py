from turtle import *

print("Aviso legal, las coordenadas no son colocadas en la funcion debido a la pereza del programador al que no le guste que no lo use :) ")

def texto(text, font_letter, color2):
    color(color2)
    write(text, font = ('arial', font_letter, 'normal'))

color2 = input("Que color quieres (ingles): ")
text = input("Que texto quieres escribir: ")
letrita = int(input("Font: "))
texto(text, letrita, color2)

hideturtle()
exitonclick()
