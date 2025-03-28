import socket
import time

def cliente_interactivo():
    """Modo interactivo para pruebas manuales"""
    HOST = 'localhost'
    PORT = 5000
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print(f"🔗 Conectado al servidor {HOST}:{PORT}")
            print("📝 Escribe mensajes (o 'DESCONEXION' para terminar el servidor):")
            
            while True:
                mensaje = input("> ")
                s.sendall(mensaje.encode('utf-8'))
                
                if mensaje == "DESCONEXION":
                    print("🛑 Solicitando apagado del servidor...")
                    break
                    
                respuesta = s.recv(1024)
                print(f"📨 Respuesta: {respuesta.decode('utf-8')}")
                
        except ConnectionRefusedError:
            print("❌ No se pudo conectar al servidor")
        except Exception as e:
            print(f"❌ Error: {e}")

def pruebas_automaticas():
    """Ejecuta una secuencia de pruebas automáticas"""
    pruebas = [
        ("TEST1", "Mensaje normal de prueba"),
        ("TEST2", ""),  # Mensaje vacío
        ("TEST3", "X" * 1024),  # Mensaje largo
        ("TEST4", "DESCONEXION")  # Comando de apagado
    ]
    
    HOST = 'localhost'
    PORT = 5000
    
    for nombre_prueba, mensaje in pruebas:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                print(f"\n🚀 Ejecutando prueba {nombre_prueba}: {mensaje[:20]}...")
                s.connect((HOST, PORT))
                s.sendall(mensaje.encode('utf-8'))
                
                if mensaje.lower() != "DESCONEXION":
                    respuesta = s.recv(1024)
                    print(f"✅ Resultado: {respuesta.decode('utf-8')}")
                else:
                    print("🛑 Prueba de apagado enviada")
                    
                time.sleep(1)  # Pequeña pausa entre pruebas
                
            except Exception as e:
                print(f"❌ Falló prueba {nombre_prueba}: {e}")

if __name__ == "__main__":
    print("Seleccione modo de prueba:")
    print("1. Modo interactivo")
    print("2. Pruebas automáticas")
    
    opcion = input("Opción (1/2): ")
    
    if opcion == "1":
        cliente_interactivo()
    elif opcion == "2":
        pruebas_automaticas()
    else:
        print("❌ Opción no válida")

