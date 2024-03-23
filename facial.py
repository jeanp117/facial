import cv2

def select_camera():
    # Enumerar las cámaras disponibles
    index = 0
    cameras = []
    while True:
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        if not cap.isOpened():
            break
        cameras.append(index)
        cap.release()
        index += 1

    print("Cámaras disponibles:")
    for i, cam in enumerate(cameras):
        print(f"{i}: Cámara {cam}")

    # Permitir al usuario seleccionar una cámara
    while True:
        choice = input("Seleccione el número de la cámara que desea utilizar: ")
        try:
            choice = int(choice)
            if choice in cameras:
                return choice
            else:
                print("Selección no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Introduzca un número válido.")

def main():
    # Seleccionar la cámara
    camera_index = select_camera()

    # Inicializar la cámara seleccionada
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

    # Cargar el modelo pre-entrenado para detección de caras
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    while True:
        # Capturar fotograma por fotograma
        ret, frame = cap.read()

        # Convertir a escala de grises para la detección de rostros
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar caras en la imagen
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Dibujar rectángulos alrededor de las caras detectadas
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        # Mostrar la imagen resultante
        cv2.imshow('frame',frame)

        # Romper el bucle si se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la cámara y cerrar todas las ventanas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
