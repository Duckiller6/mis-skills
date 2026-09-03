---
name: analizador-subastas-aeat-boe
description: Analiza subastas de la AEAT y del BOE, especialmente inmuebles, garajes y participaciones, revisando qué se subasta, porcentaje de propiedad, cargas, valoración, depósito, ubicación, riesgos, alquiler potencial, rentabilidad y precio máximo orientativo. Úsala para evaluar una subasta concreta o comparar varias oportunidades.
---

# Objetivo
Convertir la información dispersa de una subasta AEAT/BOE en una ficha de inversión clara, verificable y accionable, con riesgos explícitos y un veredicto final.

# Regla esencial
Nunca confundir:
- valor de tasación,
- tipo de subasta,
- puja mínima,
- depósito,
- deuda reclamada,
- cargas anteriores,
- cargas que se cancelan,
- precio real de mercado.

Si un dato no aparece o no puede verificarse, escribir **“No consta / no verificado”**. No inventarlo.

# Fuentes
Cuando la subasta sea actual o exista un enlace público:
- Consultar la ficha oficial de la subasta.
- Priorizar BOE, Portal de Subastas, AEAT, Catastro/Registro cuando haya datos públicos utilizables y documentos oficiales asociados.
- Para mercado de venta o alquiler, usar fuentes inmobiliarias recientes y comparables razonables.
- Indicar claramente qué datos son oficiales y cuáles son estimaciones de mercado.

# Flujo de análisis

## 1. Identificar exactamente qué se subasta
Determinar:
- tipo de bien,
- dirección o localización,
- referencia catastral si consta,
- finca registral si consta,
- porcentaje de pleno dominio,
- nuda propiedad/usufructo u otro derecho,
- anexos incluidos,
- si se subasta una plaza completa o una cuota indivisa.

Este punto debe aparecer al principio porque puede cambiar por completo la inversión.

## 2. Datos económicos oficiales
Extraer, cuando consten:
- valoración/tasación,
- tipo de subasta,
- importe del depósito,
- puja mínima si existe,
- tramos de puja,
- deuda o responsabilidad reclamada si es relevante,
- fecha de inicio y cierre.

## 3. Cargas y situación jurídica
Separar en una tabla o lista:
- cargas anteriores/preferentes,
- cargas posteriores,
- hipotecas,
- embargos,
- afecciones fiscales,
- servidumbres,
- arrendamientos u ocupantes si constan,
- deudas de comunidad/IBI si hay información,
- cualquier limitación de uso o transmisión.

No afirmar que una carga se cancela solo por aparecer como posterior. Explicar qué puede deducirse con seguridad y qué requiere nota simple, certificación registral o asesoramiento profesional.

## 4. Posesión y ocupación
Indicar:
- si consta libre u ocupado,
- si existe arrendatario,
- si se desconoce,
- coste/riesgo potencial de obtener posesión.

Si no hay evidencia, decir “situación posesoria no verificada”.

## 5. Mercado
Estimar por separado:
- valor de venta razonable,
- alquiler mensual razonable,
- rango conservador y rango probable,
- comparables utilizados cuando sea posible.

No usar un único anuncio como referencia suficiente. Preferir varios comparables cercanos y similares.

## 6. Costes de adquisición
Contemplar según el caso:
- importe de adjudicación,
- impuestos,
- Registro/Notaría si proceden,
- cargas que deba asumir el adjudicatario,
- deuda de comunidad/IBI potencial,
- gastos de posesión/desalojo,
- reforma o puesta a punto,
- comisión/intermediación si existiera.

Si no se puede calcular con precisión, usar escenarios y explicar supuestos.

## 7. Rentabilidad
Calcular cuando haya datos suficientes:
- rentabilidad bruta anual = alquiler anual / coste total estimado,
- rentabilidad neta aproximada si pueden estimarse gastos,
- descuento frente a mercado,
- margen potencial de reventa.

No presentar una rentabilidad como exacta si depende de supuestos.

## 8. Precio máximo orientativo
Proponer un **precio máximo de puja** solo si hay información suficiente.
Debe surgir de:
- valor de mercado conservador,
- costes adicionales,
- riesgos,
- margen mínimo deseado.

Mostrar la lógica del cálculo. Si faltan cargas, porcentaje de propiedad o situación posesoria, no dar un precio máximo cerrado; dar un límite condicionado.

# Semáforo de riesgo
Clasificar cada área:
- 🟢 Bajo
- 🟡 Medio
- 🔴 Alto

Áreas mínimas:
- propiedad/derecho subastado,
- cargas,
- ocupación,
- documentación,
- precio frente a mercado,
- liquidez/alquiler.

# Veredicto final
Cerrar siempre con uno de estos:
- **INTERESANTE**: riesgo razonable y descuento suficiente.
- **DUDOSA**: puede tener sentido, pero faltan datos o el margen es ajustado.
- **DESCARTAR**: riesgo, cargas, porcentaje de propiedad o precio hacen poco atractiva la operación.

Añadir en una línea el motivo principal.

# Formato de salida por defecto

## Resumen
- Bien:
- Ubicación:
- Derecho/porcentaje subastado:
- Valoración oficial:
- Depósito:
- Cierre:

## Lo más importante
Explicar en 2-5 puntos qué puede hacer ganar o perder dinero en esta subasta.

## Cargas y riesgos
Tabla con concepto, estado, impacto y nivel de riesgo.

## Mercado y rentabilidad
Tabla con venta estimada, alquiler estimado, coste total, rentabilidad y descuento.

## Precio máximo orientativo
Mostrar cálculo y supuestos.

## Antes de pujar
Lista concreta de comprobaciones pendientes.

## Veredicto
**INTERESANTE / DUDOSA / DESCARTAR** — razón principal.

# Comparación de varias subastas
Cuando haya varias:
- aplicar exactamente los mismos criterios a todas,
- hacer una tabla comparativa,
- ordenar de mejor a peor oportunidad,
- explicar en una frase por qué cada una ocupa esa posición,
- penalizar fuertemente cuotas indivisas, cargas inciertas y ocupación no resuelta.

# Límites
Esto es análisis de inversión, no una certificación registral ni asesoramiento jurídico. Cuando una conclusión dependa de información no pública o registral, indicar qué documento hace falta para cerrarla.
