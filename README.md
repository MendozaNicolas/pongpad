# Pongpad

![Preview](/preview.png)
<br>
<br>

**Juego creado** en **Python** usando la libreria **Pygame**! 


## Tabla de contenidos

- [Pongpad](#pongpad)
  - [Tabla de contenidos](#tabla-de-contenidos)
  - [Descripción](#descripción)
  - [Sobre el proyecto](#sobre-el-proyecto)
  - [Instalación](#instalación)
  - [Controles](#controles)
  - [Librerias](#librerias)

## Descripción


Esta es la implementacion sencilla del juego pong en Python utilizando la libreria Pygame. El juego es basico, marca puntos enfrentandote contra el bot.

## Sobre el proyecto

El proyecto cuenta con el directorio Assets donde estan alojadas todas las imagenes para que el juego funcione correctamente. 
En el archivo pong.py es donde el juego cuenta con todas las funcionalidades para funcionar, 
Primero importo las librerias, luego los assets. 
El script cuenta con varias clases que en el juego cuenta como una "entidad", la clase **Paddle** es donde  estan las funciones del jugador, como la de subir y bajar.
Este proyecto lo realice en mis tiempos libres, y lo voy a ir actualizando cuando tenga mas ratos libres.

## Instalación
Requerimientos: Necesitas tener python instalado

1. Clona el repositorio
2. Abre la terminal, navega al directorio donde el repositorio fue clonado, e.g., `C:\Users\Nico\pythonProyectos\pongpad`
3. Instala la libreria:
    ```bash
    pip install pygame 
    ```
4. Ejecuta el juego utilizando el siguiente comando:
    ```bash
    python pong.py
    ```

## Controles
- Usa W para subir.
- Usa S para bajar.

## Librerias

- [pygame](https://www.pygame.org/news): Pygame is a cross-platform set of Python modules designed for writing video games.