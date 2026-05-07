from fastapi import FastAPI, Body
import openai
import os

app = FastAPI()

# Esto permite que Railway use tu llave secreta de forma segura
openai.api_key = os.getenv("OPENAI_API_KEY")

KNOWLEDGE_BASE = """
Eres Víctor, asesor experto en Derco Center Roberts Arequipa. 
Vendes JAC (JS2, JS3, JS4, JS6, T8, T9) y Changan (Alsvin, CS15, CS35 Max, X7 Plus, UNI-T).
Precios base referenciales: JAC JS2 desde $11,990. GLP tiene recargo extra.
Financiamiento: Trabajamos con Fonbienes Perú.
Siempre sé amable y busca cerrar una cita en la tienda.
"""

@app.post("/chat")
async def chat_handler(data: dict = Body(...)):
    user_message = data.get("content", "")
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": KNOWLEDGE_BASE},
            {"role": "user", "content": user_message}
        ]
    )
    
    bot_reply = response.choices[0].message.content
    
    return {
        "version": "v2",
        "content": {
            "messages": [
                {"type": "text", "text": bot_reply}
            ]
        }
    }
Después de pegar esto, dale al botón verde "Commit changes..." en la esquina superior derecha.

2. Crea el archivo requirements.txt
Este archivo le dice al servidor qué programas instalar.

Haz clic de nuevo en "Add file" -> "Create new file".

Nombre: requirements.txt

Contenido (copia y pega solo estas 3 líneas):

Plaintext
fastapi
uvicorn
openai==0.28
Dale a "Commit changes...".

3. Crea el archivo Procfile (Muy importante)
Es el que le dice a Railway cómo encender el motor.

Add file -> Create new file.

Nombre: Procfile (Ojo: la "P" es mayúscula y no lleva extensión .txt).

Contenido:

Plaintext
web: uvicorn main:app --host 0.0.0.0 --port $PORT
