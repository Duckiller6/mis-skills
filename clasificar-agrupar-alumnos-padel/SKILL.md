# Clasificar / agrupar alumnos de pádel

## Objetivo
Buscar candidatos para completar o formar grupos de pádel de Fairplay según día, hora, nivel y compatibilidad real, usando como fuente de candidatos el Google Sheet oficial del trimestre.

## Fuente obligatoria
Usar **únicamente** este Google Sheet para sacar los datos de candidatos:

- Archivo: **Formulario Trimestre SEPTIEMBRE - DIC 2026 (respuestas)**
- Spreadsheet ID: `1YG4kENEhSpfU_CJuER_vrhL-Dp1m-wdRrJDzSQHfehU`
- Pestaña: **Respuestas de formulario 1**

No usar como fuente de candidatos `Trimestre Escuelas SEPTIEMBRE 2026.xlsx`, hojas históricas, memoria ni otros archivos, salvo que Pato lo pida expresamente.

## Columnas principales del formulario
- A: Marca temporal
- C: Nombre y apellidos y edad (jugador 1)
- D: Teléfono (jugador 1)
- E: Disponibilidad horaria
- F: Nivel de juego (jugador 1)
- H: Comentarios
- I: Nombre jugador 2
- J: Teléfono jugador 2
- K: Nivel jugador 2
- L: Nombre jugador 3
- M: Teléfono jugador 3
- N: Nivel jugador 3

Si hay jugador 2 o jugador 3 en la misma respuesta, tratarlo como candidato independiente y conservar siempre la fila original del formulario. La disponibilidad indicada en E corresponde a la respuesta presentada y debe interpretarse con prudencia para los jugadores adicionales.

## Método de búsqueda
1. Resolver exactamente el pedido: día, hora, nivel, cantidad de plazas y, si corresponde, adulto/menor.
2. Leer el Sheet en vivo antes de responder. No basarse en datos recordados de búsquedas anteriores.
3. Buscar candidatos cuya disponibilidad incluya realmente el día y la hora solicitados.
4. Priorizar nivel exacto.
5. Si no hay coincidencia exacta, mostrar alternativas cercanas solo si pueden ser útiles y marcarlas claramente como **alternativas**, sin hacer pasar una aproximación por coincidencia exacta.
6. No mezclar menores con adultos salvo que Pato lo pida o el grupo sea específicamente de menores.
7. Tener en cuenta comentarios relevantes de la fila cuando afecten la compatibilidad.
8. No inventar disponibilidad. Expresiones como “a partir de las 18” incluyen las 18:00; “18:30 en adelante” no incluye las 18:00.
9. Si una disponibilidad es ambigua, indicarlo y no presentarla como coincidencia segura.

## Nivel
Tomar el nivel declarado en el formulario del candidato correspondiente (F, K o N). Cuando el texto contiene una categoría y un número, usar el número como referencia principal, por ejemplo `Iniciación Intermedio (1,5)` = nivel 1.5.

No cambiar ni reinterpretar el nivel por información de otros archivos salvo instrucción expresa de Pato.

## Salida obligatoria
Por **cada candidato** devolver siempre, sin omitir ninguno de estos datos:

- Nombre y edad, si figura
- Teléfono
- Nivel
- Disponibilidad relevante
- Compatibilidad con el horario pedido: exacta / alternativa / dudosa
- **Fila exacta del Google Sheet**
- **Celdas exactas** de nombre, teléfono, disponibilidad y nivel
- Comentario relevante, si existe

Ejemplo para jugador 1 en fila 39:
- Fila: **39**
- Nombre: **C39**
- Teléfono: **D39**
- Disponibilidad: **E39**
- Nivel: **F39**

Para jugador 2 o 3, indicar sus celdas reales (I/J/K o L/M/N) y mantener E como celda de disponibilidad.

## Regla crítica de fila
El número de fila que se devuelve debe ser el **número real visible del Google Sheet**, no un índice de dataframe, no una fila de un Excel exportado y no un número inferido de texto parseado.

Antes de dar la respuesta final, verificar que el resultado de búsqueda del conector muestre explícitamente `Row` o leer el rango correspondiente para confirmar la fila.

## Formato recomendado
Presentar primero los candidatos exactos, ordenados de mejor a peor. Si no hay exactos, decirlo claramente y luego mostrar alternativas.

Formato breve:

**1. Nombre — nivel X**
- Teléfono: ...
- Disponibilidad: ...
- Compatibilidad: ✅ exacta / ⚠️ alternativa / ❓ dudosa
- Fila: **NN**
- Celdas: nombre Cnn · teléfono Dnn · disponibilidad Enn · nivel Fnn
- Comentario: ...

## Restricciones
- No modificar el Sheet ni ningún archivo salvo pedido explícito de Pato.
- No completar huecos con suposiciones.
- No usar otro archivo como fuente de candidatos por comodidad.
- No omitir la fila ni las celdas exactas aunque el usuario no las vuelva a mencionar: forman parte obligatoria de esta skill.
- Si no hay candidato compatible, decir **“No encontré coincidencia exacta”** y explicar qué criterio falla.
