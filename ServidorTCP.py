import socket

def servidor_tcp_persistente():
    # Configuración del servidor
    host = 'localhost'  # Escucha en todas las interfaces
    port = 5000      # Puerto arbitrario
    
    # Crear socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Permitir reusar la dirección si el servidor se cierra abruptamente
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Enlace del socket al puerto
        s.bind((host, port))
        print(f"Servidor iniciado en {host}:{port}. Esperando conexiones...")
        
        # Escuchar conexiones entrantes
        s.listen(5)  # Permitir hasta 5 conexiones en cola
        print("Esperando conexiones...")
        
        while True:  # Bucle principal para aceptar múltiples clientes
            try:
                # Aceptar conexión
                conn, addr = s.accept()
                print(f"\nConexión establecida desde {addr}")
                
                with conn:
                    while True:  # Bucle para manejar mensajes del cliente actual
                        # Recibir datos del cliente
                        data = conn.recv(1024)
                        if not data:
                            print(f"Conexión cerrada por {addr}")
                            break  # Este cliente se desconectó
                        
                        mensaje = data.decode('utf-8').strip()
                        print(f"Cliente {addr}: {mensaje}")
                        
                        # Verificar si es el mensaje de desconexión
                        if mensaje == "DESCONEXION":
                            print("Recibido comando de desconexión. Cerrando servidor...")
                            conn.sendall("Servidor se desconecta. Adiós!".encode('utf-8'))
                            return  # Salir completamente del servidor
                        
                        # Enviar respuesta al cliente
                        respuesta = mensaje.upper()
                        conn.sendall(respuesta.encode('utf-8'))
            
            except KeyboardInterrupt:
                print("\nServidor detenido por el usuario.")
                return
            except Exception as e:
                print(f"Error con cliente {addr}: {e}")
                continue  # Continúa con el siguiente cliente

if __name__ == "__main__":
    servidor_tcp_persistente()
    print("Servidor cerrado correctamente.")