#Entrega para PythonPl

import random
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar sidos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
    "// Esto es un comentario",
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

contador = 0

questions_to_ask = random.choices(list(zip(questions,answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
for questions,answers, correct_answers_index in questions_to_ask:
# Se selecciona una pregunta aleatoria
# Se muestra la pregunta y las respuestas posibles
    print(questions)
    for i, answer in enumerate(answers):
        print(f"{i + 1}. {answer}")
# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = (input("Respuesta: "))
# Se verifica si la respuesta es correcta
        if user_answer.isdigit() and (int(user_answer) > 0) and (int(user_answer) <= 4):
            user_answer = int(user_answer)-1
        else:
            print("Respuesta no valida")
            exit(1)

        if user_answer ==correct_answers_index:
            print("Correcto")
            contador = contador + 1
            break        
    else:
        # Si el usuario no responde correctamente después de 2 intentos,             
        # se muestra la respuesta correcta
        print("Respuesta incorrecta.")
        contador = contador - 0.5
        print("La respuesta correcta es:")
        print(answers[correct_answers_index])
# Se imprime un blanco al final de la pregunta
print("El puntaje del jugador es:", contador )


print()