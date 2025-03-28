# Servidor y Cliente TCP/IP con Control de Desconexión

Servidor TCP/IP persistente que maneja múltiples conexiones cliente secuencialmente y se cierra al recibir el comando "Desconeccion" desde cualquier cliente.


## Requisitos
- Python 3.7 o superior
- Sistema operativo compatible con sockets (Windows/Linux/macOS)

## Instalación
1. Clona el repositorio:
```bash
git clone https://github.com/JorgeRFM/Server-Client-TCP
cd Server-Client-TCP
```
### Ejecutar el Servidor y cliente
2. Guarda el código del servidor en un archivo `ServidorTCP.py`
3. Guarda el código del servidor en un archivo `ClienteTCP.py`
4. Ejecuta el servidor con:
   ```bash
   python ServidorTCP.py
   ```
5. Ejecuta el cliente con:
   ```bash
   python ClienteTCP.py
6. En caso de pruebas manuales presionar 1 y escribir con letras lo que se desea probar