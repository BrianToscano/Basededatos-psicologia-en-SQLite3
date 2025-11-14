import sqlite3
import os

# 1. Definición de la base de datos y la tabla
DB_NAME = 'psico.db'
TABLE_NAME = 'palabras_psicologia'

# Los datos que quieres insertar
datos_psicologia = [
    ('Cognición', 95.5, 'pensamiento, comprensión, conocimiento'),
    ('Conducta', 90.0, 'comportamiento, actitud, acción'),
    ('Emoción', 92.3, 'sentimiento, afecto, ánimo'),
    ('Motivación', 87.2, 'impulso, deseo, incentivo'),
    ('Percepción', 85.6, 'sensación, interpretación, apreciación'),
    ('Aprendizaje', 98.0, 'educación, conocimiento, adquisición'),
    ('Memoria', 94.1, 'recuerdo, retención, evocación'),
    ('Atención', 89.5, 'concentración, enfoque, observación'),
    ('Personalidad', 91.2, 'carácter, temperamento, identidad'),
    ('Trauma', 88.4, 'herida emocional, impacto, shock'),
    ('Depresión', 97.8, 'tristeza, desánimo, melancolía'),
    ('Ansiedad', 96.5, 'nerviosismo, preocupación, tensión'),
    ('Terapia', 93.7, 'tratamiento, intervención, ayuda'),
    ('Inteligencia', 90.9, 'razonamiento, comprensión, habilidad'),
    ('Bienestar', 89.0, 'salud mental, equilibrio, satisfacción'),
]

def crear_y_cargar_db():
    """Conecta, crea la tabla e inserta los datos."""
    try:
        # La función connect() crea el archivo DB si no existe
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        print(f"Conexión exitosa a la base de datos: {DB_NAME}")

        # 2. Crear la tabla
        # Usamos IF NOT EXISTS para que no dé error si la ejecutas varias veces
        # Añadimos UNIQUE a 'palabra' para evitar duplicados en la inserción
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                palabra TEXT NOT NULL UNIQUE,
                porcentaje_identidad REAL NOT NULL,
                sinonimos TEXT
            )
        """)
        print(f"Tabla '{TABLE_NAME}' creada o ya existe.")

        # 3. Insertar los datos
        # La sentencia INSERT OR IGNORE previene duplicados usando la restricción UNIQUE en 'palabra'
        insert_sql = f"""
            INSERT OR IGNORE INTO {TABLE_NAME} (palabra, porcentaje_identidad, sinonimos)
            VALUES (?, ?, ?)
        """
        
        # Ejecutar la inserción para todos los datos a la vez
        cursor.executemany(insert_sql, datos_psicologia)
        
        # Confirmar los cambios
        conn.commit()
        print(f"Se intentaron insertar {len(datos_psicologia)} registros. Cambios guardados.")
        
    except sqlite3.Error as e:
        print(f"Ocurrió un error de SQLite: {e}")
    finally:
        # 4. Cerrar la conexión
        if conn:
            conn.close()
            print("Conexión a la DB cerrada.")

def verificar_datos():
    """Verifica si los datos se insertaron correctamente."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM {TABLE_NAME} LIMIT 5")
        filas = cursor.fetchall()
        
        print("\n--- Verificación de Datos (Primeras 5 filas) ---")
        if filas:
            for fila in filas:
                print(fila)
        else:
            print("No se encontraron datos en la tabla.")
            
    except sqlite3.Error as e:
        print(f"Ocurrió un error al leer la base de datos: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    crear_y_cargar_db()
    verificar_datos()
