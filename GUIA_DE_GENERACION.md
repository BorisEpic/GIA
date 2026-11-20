# Guía de generación de imágenes

## Prompt de ejecución

> Procesa `Data/NOMBRE.docx` según `GUIA_DE_GENERACION.md`. Genera y verifica todas las parejas alumno–profesor. Entrega el ZIP final en `Comprimidos`.

## Fuentes y organización

- Usar los archivos de `Data` como fuente de las actividades y las imágenes de `Data/IMG_Referencia` como referencia visual.
- Inventariar los contenidos y comprobar que cada uno tenga sus 60 actividades en orden. Agruparlas de cinco en cinco, sin omitir ni duplicar ninguna. El resultado por contenido debe ser de 12 páginas de alumno y 12 de profesor.
- Preparar los enunciados, materiales y soluciones antes de maquetar. Si el archivo no trae un texto, una cuadrícula u otro material necesario, completarlo de forma coherente con el ejercicio y usarlo en ambas versiones. Registrar las correcciones del original que cambien una consigna o respuesta. Si un error es ambiguo y no se puede resolver con el contexto, señalar el bloque afectado y continuar con los demás.
- Guardar las imágenes en `Generadas`, en una carpeta con el nombre del archivo de contenido, organizadas por contenido y por destinatario.
- Una vez terminadas y verificadas las imágenes, comprimir cada carpeta de banco en un archivo ZIP con el mismo nombre de la carpeta y guardarlo en `Comprimidos`. No incluir versiones anteriores ni archivos ajenos al banco.

## Correspondencia entre alumno y profesor

- Maquetar primero la página del alumno y reservar un margen derecho para las guías del profesor. Crear el solucionario con la misma base, colocando los cambios como capas en posiciones fijas. Usar el generador de imágenes para las ilustraciones cuando haga falta y componer el texto, las cuadrículas y las soluciones con una plantilla. No volver a pasar la página completa por el generador para crear la versión del profesor, ya que puede redibujarla.
- Conservar también los mismos ejercicios, textos, datos, opciones, orden y distribución. En particular, las cuadrículas y demás elementos necesarios para resolver los ejercicios deben coincidir exactamente.
- La versión del profesor debe mostrar los ejercicios resueltos, con las respuestas y marcas en rojo. En actividades abiertas o de respuesta personal, mostrar un ejemplo válido e identificarlo como tal; aceptar otras respuestas correctas cuando corresponda.
- Las únicas diferencias permitidas en la versión del profesor son las respuestas y marcas de solución en rojo, una guía didáctica a la derecha por actividad, los títulos de las actividades en rojo y el rótulo «Versión Profesor · Solucionario».
- Mantener el marco, el encabezado y el estilo visual coherentes con las referencias y entre todas las páginas.

## Validación

- Verificar las cinco actividades y sus soluciones contra la fuente y la página del alumno. Comprobar que fuera de las zonas autorizadas de edición ambas imágenes coincidan píxel por píxel.
- Revisar la legibilidad, la ortografía, la numeración y la fidelidad al archivo de contenido. Corregir las discrepancias antes de entregar la pareja como definitiva.
- Las imágenes generadas antes de aplicar estas reglas requieren revisión y, si no cumplen, corrección.
- Antes de comprimir, comprobar que haya un solo PNG por bloque y destinatario y que el ZIP contenga todas las páginas verificadas.
- Nombrar los PNG verificados como `actividades_01-05.png`, `actividades_06-10.png` y así sucesivamente, dentro de `Contenido N/Alumno` o `Contenido N/Profesor`. Usar `python3 gia.py comprimir "Data/NOMBRE.docx" --contenidos N` con todos los números de contenido.
