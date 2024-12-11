from gemini import Asistente

def main():
    asistente = Asistente()
    user_message = ""
    asistente.iniciar_sesion()
    while user_message != "exit":
        user_message = input("🧑: ")
        response = asistente.send_message(user_message)
        print("🤖:", response)

if __name__ == "__main__":
    main()
