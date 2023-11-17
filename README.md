# Teoría de Lenguajes: Taller de PLY (Python Lex-Yacc)

Este código corresponde al taller de PLY de la materia Teoría de Lenguajes
del Departamento de Computación, FCEyN, UBA.

## Requerimientos

El único requisito para ejecutar este taller es poseer instalado Python 3.
La única dependencia, [PLY](http://www.dabeaz.com/ply/), está incluida dentro
del proyecto, ya que la versión de la misma distribuida a través de `pip` no
está actualizada (ver la documentación de PLY para más detalles).

## Forma de ejecución

Para ejecutar el programa, utilizar el comando

```
python3 main.py
```

El mismo recibe por entrada estándar la cadena a parsear.
Además, acepta como opciones:

- `-h`, `--help`: mostrar un texto de ayuda.
- `-i`, `--interactive`: ejecutar en modo interactivo, permite ingresar más
  de una cadena sin finalizar la ejecución.
- `-l`, `--lexer`: ejecuta solo el analizador léxico e imprime la secuencia
  de tokens generada.

