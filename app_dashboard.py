
import streamlit as st
import sqlite3
import pandas as pd

# Usuarios y claves simuladas
USUARIOS = {"frank": "clave123", "admin": "admin123"}

st.title("🔐 Login - Dashboard BI")

usuario = st.text_input("Usuario")
clave = st.text_input("Clave", type="password")

if usuario in USUARIOS and USUARIOS[usuario] == clave:
    st.success(f"Bienvenido, {usuario}")

    # Conexión a base de datos
    conn = sqlite3.connect("ventas_demo.db")
    df = pd.read_sql("SELECT * FROM ventas WHERE usuario = ?", conn, params=(usuario,))
    conn.close()

    st.subheader("📈 Ventas registradas")
    st.dataframe(df)

    st.metric("Total Vendido", f"${df['ventas'].sum():,.2f}")

    st.line_chart(df.set_index("fecha")["ventas"])

else:
    st.warning("Ingresa tus credenciales para continuar.")
