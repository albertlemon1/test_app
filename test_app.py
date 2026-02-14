import streamlit as st

# Título simple
st.title("🛠️ Prueba de Diagnóstico")

# Mensaje de estado
st.write("Si estás viendo esto, el servidor de Streamlit está funcionando correctamente.")

# Botón interactivo
if st.button("Presionar para probar interactividad"):
    st.success("¡El sistema interactivo está vivo!")

# Verificación de entorno
st.info(f"Versión de Streamlit: {st.__version__}")
