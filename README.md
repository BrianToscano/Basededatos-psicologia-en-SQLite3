Proyecto Psico DB (SQLite3)



Contenido de la Base de Datos



### Estructura de la Tabla `palabras_psicologia`

 Columna | Tipo de Dato | Descripción |
 :--- | :--- | :--- |
 `id` | `INTEGER` | Clave Primaria (Autoincremental) |
`palabra` | `TEXT` | Término psicológico clave (Único) |
 `porcentaje_identidad` | `REAL` | Valor numérico asociado al término |
`sinonimos` | `TEXT` | Lista de sinónimos del término |
Ejemplos de Datos Incluidos

 Palabra | Porcentaje Identidad | Sinónimos |
 :--- | :--- | :--- |
 `Cognición` | 95.5 | pensamiento, comprensión, conocimiento |
 `Depresión` | 97.8 | tristeza, desánimo, melancolía |
 `Terapia` | 93.7 | tratamiento, intervención, ayuda |



