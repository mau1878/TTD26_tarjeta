import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os
import numpy as np

# Título de la aplicación
st.title("Emisor de tarjetas para miembros platino del Círculo Sagrado de Empomados por BioX")

# Cargar la imagen proporcionada
image_path = "BIOX.png"
if os.path.exists(image_path):
    img = Image.open(image_path).convert("RGBA")
else:
    st.error("El archivo 'BIOX.png' no se encuentra en el mismo folder. Por favor, asegúrate de que exista.")
    st.stop()

# Input para el nombre de usuario
username = st.text_input("Ingrese su nombre de usuario (ej. BIOX-TECLA000)", value="@")

if username:
    draw = ImageDraw.Draw(img)

    try:
        # Intentar cargar una fuente específica
        font_path = "arial.ttf"  # Asegúrate de incluir esta fuente en el folder si la usas
        font_size = 40
        try:
            font = ImageFont.truetype(font_path, font_size)
        except:
            font = ImageFont.load_default()
            st.warning("No se encontró la fuente especificada. Se usará una fuente predeterminada.")

        # Definir posición y estilo del texto
        text_position = (550, 400)  # Posición aproximada para el nombre
        base_color = (139, 0, 0)  # Color base (dorado oscuro)
        outline_color = (128, 128, 128)  # Contorno gris

        # Crear una textura simple con ruido
        text_width, text_height = draw.textsize(username, font=font)
        noise = np.random.randint(0, 30, (text_height, text_width, 3), dtype=np.uint8)  # Suave ruido
        textured_color = np.clip(base_color + noise - 15, 0, 255).astype(np.uint8)

        # Añadir efecto de contorno
        for offset in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            draw.text((text_position[0] + offset[0], text_position[1] + offset[1]), username, font=font, fill=outline_color)

        # Añadir texto con textura (simplificado a un color base por limitación de draw.text)
        draw.text(text_position, username, font=font, fill=tuple(base_color))

        # Mostrar la imagen modificada
        st.image(img, caption="Tarjeta de miembro generada", use_column_width=True)

        # Opción para descargar la imagen
        img_byte_arr = img.tobytes()
        st.download_button(
            label="Descargar Imagen",
            data=img_byte_arr,
            file_name="tarjeta_miembro_biox.png",
            mime="image/png"
        )

    except Exception as e:
        st.error(f"Error al procesar la imagen: {e}")
