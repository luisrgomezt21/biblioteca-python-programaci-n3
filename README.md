# 📚 Sistema de Gestión de Biblioteca - LP3 2026-II

## Integrantes del Grupo
- [Jorge Morales] (GitHub: @jorgedavidmorales1701-cmyk)
- [Luis Gómez] (GitHub: @luisrgomezt21)
- [Anthony Castillo] (GitHub: @Anthony709C )
- [Cristian Cerezo] (GitHub: @cristhiancerezo044-ux )

## Descripción del Proyecto
Sistema de gestión por consola desarrollado en Python para administrar el inventario de una biblioteca. Permite registrar, listar, buscar, modificar y eliminar libros, además de generar un reporte de libros prestados.

## Opción de Persistencia Elegida
**JSON**. Se eligió esta opción por su facilidad para trabajar con estructuras de datos nativas de Python (listas y diccionarios) y su legibilidad para la depuración.

## Estructura del Proyecto
```
biblioteca-lp3/
├── datos/
│   └── libros.json        # Datos persistentes
├── main.py                # Menú principal y ciclo del programa
├── logica.py              # Funciones de negocio (registrar, buscar, reportes)
├── persistencia.py        # Funciones para leer y guardar en JSON
└── README.md              # Este archivo
```

## Cómo ejecutar el programa
1. Asegúrese de tener Python 3.x instalado.
2. Clone este repositorio:
```bash
   git clone https://github.com/USUARIO/biblioteca-lp3.git
```
3. Entre a la carpeta del proyecto:
```bash
   cd biblioteca-lp3
```
4. Ejecute el archivo principal desde la terminal:
```bash
   python main.py
```

## Declaración de Uso de Inteligencia Artificial
Este proyecto fue desarrollado con el apoyo de herramientas de IA (Qwen) bajo las condiciones permitidas por el docente. La IA se utilizó exclusivamente para:
- Explicar conceptos de manejo de archivos JSON y estructura modular.
- Revisar y corregir errores de sintaxis o lógica (ej. manejo de `try/except`).
- Sugerir buenas prácticas de organización del código.

Todo el código fue probado, comprendido y adaptado por todos los integrantes del grupo, quienes están en capacidad de explicarlo y modificarlo en vivo durante la defensa.
