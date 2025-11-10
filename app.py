import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EcoAprende",
    page_icon="🌱",
    layout="wide"
)


if 'pagina' not in st.session_state:
    st.session_state['pagina'] = 'dashboard'


if 'progreso' not in st.session_state:
    st.session_state['progreso'] = {
      
        "Solar": {"completado": False, "puntaje": 0}, 
        "Eolica": {"completado": False, "puntaje": 0},
        "Hidraulica": {"completado": False, "puntaje": 0},
        "Biomasa": {"completado": False, "puntaje": 0},
    }



def calcular_resumen():
    """Calcula y devuelve las métricas del dashboard leyendo desde st.session_state."""
    progreso_actual = st.session_state['progreso']
    total_lecciones = len(progreso_actual)
    lecciones_completadas = sum(1 for data in progreso_actual.values() if data["completado"])
    insignias = lecciones_completadas
    return total_lecciones, lecciones_completadas, insignias, progreso_actual




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

    
    with cols1[1]:
        color = "green" if progreso["Eolica"]["completado"] else "blue"
        st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid {color};">
            <h4>💨 Energía Eólica</h4>
            <p>Aprovecha la fuerza del viento. Puntaje: {progreso["Eolica"]["puntaje"]}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button('Iniciar Lección', key='eolica_btn', use_container_width=True): 
            st.session_state['pagina'] = 'eolica'
            st.rerun()

    
    with cols2[0]:
        color = "green" if progreso["Hidraulica"]["completado"] else "cyan"
        st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid {color};">
            <h4>💧 Energía Hidráulica</h4>
            <p>La potencia del agua en movimiento. Puntaje: {progreso["Hidraulica"]["puntaje"]}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button('Iniciar Lección', key='hidraulica_btn', use_container_width=True): 
            st.session_state['pagina'] = 'hidraulica'
            st.rerun()

    
    with cols2[1]:
        st.markdown(f"""
        <div style="background-color: #e0e0e0; padding: 20px; border-radius: 10px; border-left: 5px solid purple;">
            <h4>🎮 Mini Juegos</h4>
            <p>¡Pon a prueba lo aprendido! (Desbloquea una insignia)</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button('Jugar Ahora', key='juegos_btn', use_container_width=True): 
            st.session_state['pagina'] = 'minijuegos'
            st.rerun()
        
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
        
        
        with st.expander("❓ Cuestionario Rápido: Energía Solar"):
            st.write("¡Responde para ganar 10 Puntos Ecológicos!")
            
            
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
                
               
                if respuesta1 == 'Solar Fotovoltaica':
                    puntaje += 5
                if respuesta2 == 'Reduce las emisiones de CO2':
                    puntaje += 5
                    
                
                st.session_state['solar_completado'] = True
                st.session_state['solar_puntaje'] = puntaje
                
                
                st.session_state['pagina'] = 'dashboard_update' 
                st.rerun()

    with col_imagen:
        st.image("https://images.unsplash.com/photo-1509391007205-d143c7b80b2a", 
                 caption="Paneles Solares Fotovoltaicos", use_column_width=True)
        
    if st.button("⬅️ Volver al Dashboard", key='back_solar'):
        st.session_state['pagina'] = 'dashboard'
        st.rerun()



def mostrar_leccion_eolica():
    """Contenido placeholder para la Lección de Energía Eólica."""
    st.title("💨 Energía Eólica: El Poder del Viento")
    st.info("💡 **Definición:** La energía eólica se obtiene del viento, utilizando aerogeneradores que transforman la energía cinética en electricidad.")
    
    st.subheader("¿Cómo funciona?")
    st.markdown("""
    1.  **Captura:** Las palas del aerogenerador capturan la fuerza del viento.
    2.  **Conversión:** Las palas giran un rotor conectado a un generador.
    3.  **Generación:** El generador produce electricidad.
    
    Es una de las energías más limpias y con mayor crecimiento global.
    """)
    
    st.image("https://images.unsplash.com/photo-1582216675035-ab3916298642", 
             caption="Aerogeneradores eólicos", use_column_width=True)
    
    if st.button("⬅️ Volver al Dashboard", key='back_eolica'):
        st.session_state['pagina'] = 'dashboard'
        st.rerun()

def mostrar_leccion_hidraulica():
    """Contenido placeholder para la Lección de Energía Hidráulica."""
    st.title("💧 Energía Hidráulica: La Potencia del Agua")
    st.info("💡 **Definición:** La energía hidráulica se genera aprovechando la caída o el flujo del agua en ríos y embalses para mover turbinas.")
    
    st.subheader("Aplicaciones y Tipos")
    st.markdown("""
    * **Grandes Centrales:** Utilizan presas y embalses para almacenar agua y liberarla cuando se necesita (mayor escala).
    * **Pequeñas Centrales (Minicentrales):** Usan el flujo natural de un río sin grandes modificaciones.
    
    Es una fuente estable, pero su construcción puede tener un alto impacto ambiental en los ecosistemas locales.
    """)
    st.image("https://images.unsplash.com/photo-1549414578-f71694f42f36", 
             caption="Central Hidroeléctrica", use_column_width=True)
    
    if st.button("⬅️ Volver al Dashboard", key='back_hidraulica'):
        st.session_state['pagina'] = 'dashboard'
        st.rerun()
        

def mostrar_mini_juegos():
    """Juego de Asociación de Iconos y Energías."""
    st.title("🎮 Mini Juego: Empareja la Energía")
    st.info("Asocia cada icono con su fuente de energía correcta. ¡Gana 10 Puntos de Bonificación!")
    
    
    opciones = ['--- Seleccionar ---', 'Solar', 'Eólica', 'Hidráulica']
    
    st.markdown("---")
    
    
    with st.form("mini_juego_form"):
        col_iconos, col_selects = st.columns(2)

       
        with col_iconos:
            st.markdown("## ☀️")
            st.markdown("## 💨")
            st.markdown("## 💧")
        
        
        with col_selects:
            r_sol = st.selectbox("Icono del Sol ☀️", opciones, key='j_r_sol')
            r_viento = st.selectbox("Icono del Viento 💨", opciones, key='j_r_viento')
            r_agua = st.selectbox("Icono del Agua 💧", opciones, key='j_r_agua')
        
        submitted = st.form_submit_button("Verificar Respuestas", type="primary")

        if submitted:
            puntaje_juego = 0
            feedback = []
            
            
            if r_sol == 'Solar':
                puntaje_juego += 3
                feedback.append("✅ Sol ☀️: Correcto (Solar)")
            else:
                feedback.append("❌ Sol ☀️: Incorrecto. Debe ser Solar.")
                
            if r_viento == 'Eólica':
                puntaje_juego += 3
                feedback.append("✅ Viento 💨: Correcto (Eólica)")
            else:
                feedback.append("❌ Viento 💨: Incorrecto. Debe ser Eólica.")

            if r_agua == 'Hidráulica':
                puntaje_juego += 4
                feedback.append("✅ Agua 💧: Correcto (Hidráulica)")
            else:
                feedback.append("❌ Agua 💧: Incorrecto. Debe ser Hidráulica.")
            
            
            st.markdown("---")
            st.subheader(f"Resultado Final: {puntaje_juego}/10 Puntos")
            for item in feedback:
                st.markdown(item)
            
           
            if puntaje_juego == 10:
                st.session_state['progreso']['Biomasa']['completado'] = True
                st.session_state['progreso']['Biomasa']['puntaje'] = 10
                st.success("¡Felicidades! Completaste el juego y ganaste una insignia de Bonificación (Biomasa) y 10 Puntos.")
                st.balloons()
            else:
                st.warning("Puedes intentarlo de nuevo para conseguir la insignia de bonificación.")


    st.markdown("---")
    if st.button("⬅️ Volver al Dashboard", key='back_juegos'):
        st.session_state['pagina'] = 'dashboard'
        st.rerun()
# --------------------------------------------------------------------------

def mostrar_dashboard_update():
    """Lógica de actualización de progreso después de completar una lección."""
    
    
    progreso = st.session_state['progreso']

    
    if st.session_state.get('solar_completado'):
        
        puntaje_obtenido = st.session_state.get('solar_puntaje', 0)
        
        progreso["Solar"]["completado"] = True
        progreso["Solar"]["puntaje"] = puntaje_obtenido
        
        
        st.success(f"¡Cuestionario completado! Ganaste **{progreso['Solar']['puntaje']}** Puntos Ecológicos.")
        st.balloons()
        
        
        if st.button("Continuar al Dashboard"):
            
            if 'solar_completado' in st.session_state:
                del st.session_state['solar_completado']
            if 'solar_puntaje' in st.session_state:
                del st.session_state['solar_puntaje']
                
            st.session_state['pagina'] = 'dashboard'
            st.rerun()
            
    else:
        
        st.warning("No se completó la lección. Volviendo al dashboard...")
        st.button("Volver al Dashboard", on_click=lambda: st.session_state.update(pagina='dashboard'))


if st.session_state['pagina'] == 'dashboard':
    mostrar_dashboard()

elif st.session_state['pagina'] == 'solar':
    mostrar_leccion_solar()

elif st.session_state['pagina'] == 'eolica': 
    mostrar_leccion_eolica()

elif st.session_state['pagina'] == 'hidraulica': 
    mostrar_leccion_hidraulica()

elif st.session_state['pagina'] == 'minijuegos': 
    mostrar_mini_juegos()
    
elif st.session_state['pagina'] == 'dashboard_update':
    mostrar_dashboard_update()
    
else:
    st.session_state['pagina'] = 'dashboard'
    st.rerun()
