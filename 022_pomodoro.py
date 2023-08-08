import time

def cuenta_regresiva(minutos):
    segundos = minutos * 60
    while segundos:
        mins, secs = divmod(segundos, 60)
        formato_tiempo = '{:02d} : {:02d}'.format(mins, secs)
        print(formato_tiempo, end='\r')
        time.sleep(1)
        segundos -= 1
        #print('Se acabo el tiempo')

def temporizador_pomodoro(tiempo_trabajo, tiempo_descanso, ciclos):
    for ciclo in range(ciclos):
        print(f'Ciclo {ciclo + 1}: Trabajo')
        cuenta_regresiva(tiempo_trabajo)
        print('Tiempo descanso')
        cuenta_regresiva(tiempo_descanso)

        if ciclo < ciclos - 1:
            print('vuelva al trabajo')

if __name__ == '__main__':
    duracion_trabajo = 1
    duracion_descanso = 1
    cantidad_ciclos = 2

temporizador_pomodoro(duracion_trabajo, duracion_descanso, cantidad_ciclos)
