import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EcoAprende",
    page_icon="🌱",
    layout="wide"
)

# --- INICIALIZACIÓN DE ESTADO (CRÍTICO: Guarda la persistencia de datos) ---

# 1. Inicializa la página por defecto
if 'pagina' not in st.session_state:
    st.session_state['pagina'] = 'dashboard'

# 2. Inicializa la estructura de progreso en el estado de sesión
if 'progreso' not in st.session_state:
    st.session_state['progreso'] = {
        # Nota: Cambiado a False y 0 para que el usuario pueda ganar puntos
        "Solar": {"completado": False, "puntaje": 0}, 
        "Eolica": {"completado": False, "puntaje": 0},
        "Hidraulica": {"completado": False, "puntaje": 0},
        "Biomasa": {"completado": False, "puntaje": 0},
    }

# --- FUNCIONES DE APOYO ---

def calcular_resumen():
    """Calcula y devuelve las métricas del dashboard leyendo desde st.session_state."""
    progreso_actual = st.session_state['progreso']
    total_lecciones = len(progreso_actual)
    lecciones_completadas = sum(1 for data in progreso_actual.values() if data["completado"])
    insignias = lecciones_completadas
    return total_lecciones, lecciones_completadas, insignias, progreso_actual


# --- PÁGINAS DE LA APLICACIÓN ---

def mostrar_dashboard():
    """Pantalla Principal: Dashboard del Estudiante."""
    
    total_lecciones, lecciones_completadas, insignias, progreso = calcular_resumen()

    st.header("🌱 EcoAprende: Tu Aventura Ecológica")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        st.metric(label="Insignias Obtenidas", value=f"{insignias}/{total_lecciones}", delta="¡Sigue así!")
    with col2:
        st.progress(lecciones_completadas / total_lecciones, text=f"Progreso General: {lecciones_completadas}/{total_lecciones} Lecciones")

    st.markdown("---")
    st.subheader("Selecciona una Lección para empezar a aprender:")
    

    cols1 = st.columns(2)
    cols2 = st.columns(2)
    
    # Lección Solar
    with cols1[0]:
        color = "green" if progreso["Solar"]["completado"] else "orange"
        st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid {color};">
            <h4>🌞 Energía Solar</h4>
            <p>Aprende sobre la energía del sol. Puntaje: {progreso["Solar"]["puntaje"]}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button('Iniciar Lección', key='solar_btn', use_container_width=True):
            st.session_state['pagina'] = 'solar'
            st.rerun()

    # Lección Eólica
    with cols1[1]:
        color = "green" if progreso["Eolica"]["completado"] else "blue"
        st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid {color};">
            <h4>💨 Energía Eólica</h4>
            <p>Aprovecha la fuerza del viento. Puntaje: {progreso["Eolica"]["puntaje"]}</p>
        </div>
        """, unsafe_allow_html=True)
        st.button('Iniciar Lección', key='eolica_btn', use_container_width=True, disabled=True) # Deshabilitado

    # Lección Hidráulica
    with cols2[0]:
        color = "green" if progreso["Hidraulica"]["completado"] else "cyan"
        st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid {color};">
            <h4>💧 Energía Hidráulica</h4>
            <p>La potencia del agua en movimiento. Puntaje: {progreso["Hidraulica"]["puntaje"]}</p>
        </div>
        """, unsafe_allow_html=True)
        st.button('Iniciar Lección', key='hidraulica_btn', use_container_width=True, disabled=True) # Deshabilitado

    # Mini Juegos
    with cols2[1]:
        st.markdown(f"""
        <div style="background-color: #e0e0e0; padding: 20px; border-radius: 10px; border-left: 5px solid purple;">
            <h4>🎮 Mini Juegos</h4>
            <p>¡Pon a prueba lo aprendido! (Desbloquea una insignia)</p>
        </div>
        """, unsafe_allow_html=True)
        st.button('Jugar Ahora', key='juegos_btn', use_container_width=True, disabled=True) # Deshabilitado
        
    st.markdown("---")


def mostrar_leccion_solar():
    """Contenido de la Lección de Energía Solar con cuestionario."""
    st.title("🌞 Energía Solar: Aprovechando la Luz")
    
    st.info("💡 **Definición:** La energía solar aprovecha la radiación del sol para generar electricidad o calor.")
    
    col_texto, col_imagen = st.columns(2)
    
    with col_texto:
        st.subheader("Características Principales")
        st.markdown("""
        * **Fuente Inagotable:** Es un recurso que se renueva continuamente.
        * **Bajo Impacto Ambiental:** No produce emisiones de CO2 en su generación.
        * **Aplicación:** Se usa en paneles fotovoltaicos (electricidad) y calentadores solares (calor).
        """)
        
        st.subheader("Beneficios para Chihuahua")
        st.markdown("""
        Chihuahua, con su alto índice de días soleados, tiene un **potencial solar enorme**. 
        Grandes proyectos como parques solares aprovechan esta ventaja para la generación a gran escala.
        """)
        
        # --- CUESTIONARIO ---
        with st.expander("❓ Cuestionario Rápido: Energía Solar"):
            st.write("¡Responde para ganar 10 Puntos Ecológicos!")
            
            # CRÍTICO: Usar keys para guardar las respuestas en st.session_state
            respuesta1 = st.radio(
                "1. ¿Qué tipo de energía solar genera electricidad directamente?",
                ('Solar Térmica', 'Solar Fotovoltaica', 'Solar Geotérmica'),
                key='r1_solar' 
            )
            
            respuesta2 = st.radio(
                "2. ¿Cuál es uno de los principales beneficios ambientales?",
                ('Genera pocos residuos', 'Reduce las emisiones de CO2', 'Funciona solo de noche'),
                key='r2_solar'
            )
            
            if st.button("Enviar Respuestas", key='quiz_solar'):
                puntaje = 0
                
                # CRÍTICO: Acceder a las respuestas desde st.session_state (aunque st.radio lo hace automáticamente)
                # La lógica de Streamlit asegura que estas variables mantengan su valor al hacer click en el botón.
                if respuesta1 == 'Solar Fotovoltaica':
                    puntaje += 5
                if respuesta2 == 'Reduce las emisiones de CO2':
                    puntaje += 5
                    
                # Guardar el puntaje en el estado de la sesión
                st.session_state['solar_completado'] = True
                st.session_state['solar_puntaje'] = puntaje
                
                # Transicionar a la página de actualización
                st.session_state['pagina'] = 'dashboard_update' 
                st.rerun()

    with col_imagen:
        st.image("https://images.unsplash.com/photo-1509391007205-d143c7b80b2a", 
                 caption="Paneles Solares Fotovoltaicos", use_column_width=True)
        
    if st.button("⬅️ Volver al Dashboard", key='back_solar'):
        st.session_state['pagina'] = 'dashboard'
        st.rerun()


def mostrar_dashboard_update():
    """Lógica de actualización de progreso después de completar una lección."""
    
    # CRÍTICO: Leer el diccionario de progreso desde el estado de sesión
    progreso = st.session_state['progreso']

    if st.session_state.get('solar_completado'):
        # 1. Actualizar el progreso PERSISTENTE
        puntaje_obtenido = st.session_state.get('solar_puntaje', 0)
        
        progreso["Solar"]["completado"] = True
        progreso["Solar"]["puntaje"] = puntaje_obtenido
        
        # 2. Mensaje de éxito
        st.success(f"¡Cuestionario completado! Ganaste **{progreso['Solar']['puntaje']}** Puntos Ecológicos.")
        st.balloons()
        
        # 3. Mostrar botón para continuar
        if st.button("Continuar al Dashboard"):
            st.session_state['pagina'] = 'dashboard'
            st.rerun()
            
    else:
        # En caso de que se llegue aquí por error
        st.warning("No se completó la lección solar.")
        st.button("Volver al Dashboard", on_click=lambda: st.session_state.update(pagina='dashboard'))


# --- LÓGICA DE NAVEGACIÓN PRINCIPAL (Corregida) ---

# Usamos una cadena if/elif para asegurar que solo una página se renderice a la vez
if st.session_state['pagina'] == 'dashboard':
    mostrar_dashboard()

elif st.session_state['pagina'] == 'solar':
    # La página 'solar' llama a la función que contiene el contenido y el cuestionario
    mostrar_leccion_solar()
    
elif st.session_state['pagina'] == 'dashboard_update':
    # La página de actualización maneja la lógica de resultados
    mostrar_dashboard_update()
    
# Cualquier otro estado (como 'inicio' que estaba vacío) se ignorará o se manejará con un 'else'
else:
    st.session_state['pagina'] = 'dashboard'
    st.rerun()
