import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

# Título de la aplicación
st.title("Emisor de tarjetas para miembros platino del círculo sagrado de TTD26")

# Cargar la imagen desde el mismo folder (asegúrate de que el archivo 'card.png' exista)
image_path = "TTD26.png"
if os.path.exists(image_path):
    img = Image.open(image_path).convert("RGBA")
else:
    st.error("El archivo 'card.png' no se encuentra en el mismo folder. Por favor, asegúrate de que exista.")
    st.stop()

# Input para el nombre de usuario
username = st.text_input("Ingrese su nombre de usuario de X/Twitter (ej. @usuario)", value="@")

if username:
    draw = ImageDraw.Draw(img)

    try:
        # Intentar cargar una fuente específica (asegúrate de incluir arial.ttf en el folder si lo usas)
        font_path = "arial.ttf"  # Cambia esto a la ruta de tu fuente si la incluyes
        font_size = 40
        try:
            font = ImageFont.truetype(font_path, font_size)
        except:
            # Fallback a una fuente genérica si no se encuentra la especificada
            font = ImageFont.load_default()
            st.warning("No se encontró la fuente especificada. Se usará una fuente predeterminada.")

        # Definir posición y estilo del texto (ajusta según el diseño de la imagen)
        text_position = (360, 580)  # Posición aproximada para el nombre de usuario
        text_color = (255, 255, 255)  # Color blanco
        outline_color = (0, 0, 0)  # Contorno negro

        # Añadir efecto de contorno (simulando el aspecto grabado)
        for offset in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            draw.text((text_position[0] + offset[0], text_position[1] + offset[1]), username, font=font, fill=outline_color)

        # Añadir el texto principal
        draw.text(text_position, username, font=font, fill=text_color)

        # Mostrar la imagen modificada
        st.image(img, caption="Tarjeta de miembro generada", use_column_width=True)

        # Opción para descargar la imagen
        img_byte_arr = img.tobytes()
        st.download_button(
            label="Descargar Imagen",
            data=img_byte_arr,
            file_name="tarjeta_miembro.png",
            mime="image/png"
        )

    except Exception as e:
        st.error(f"Error al procesar la imagen: {e}")

# Nota: Para una coincidencia más precisa de la fuente, puedes incluir una fuente como "Times New Roman" o "Georgia" en el folder y especificar su ruta.
