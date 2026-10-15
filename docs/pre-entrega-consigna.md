# Consignas de Pre-Entrega de proyecto

El objetivo de la siguiente pre-entrega de proyecto es que apliques los conocimientos adquiridos hasta la Clase 8 del curso, demostrando tu capacidad para automatizar flujos básicos de navegación web utilizando Selenium WebDriver y Python. 

Este proyecto te permitirá poner en práctica lo aprendido sobre interacción con elementos web, estrategias de localización y validación de estados en una página. El sitio objetivo para esta automatización será sucedemo.com, una aplicación web demo especialmente diseñada para prácticas de testing.

> **Sitio Web a utilizar:** www.saucedemo.com

## Fecha de Entrega y Evaluación

- Fecha límite de entrega: 7 días a partir de la Clase 8.
- Formato de entrega: Codigo subido a Github

## Tecnologías requeridas

- `Python` como lenguaje principal
- `Pytest` para estructura de testing
- `Selenium WebDriver` para automatización
- `Git` y `GitHub` para control de versiones

## Estructura del proyecto

Organizar el código en mínimo 2 archivos separados (tests y funciones auxiliares). Incluir comentarios descriptivos y usar nomenclatura significativa para todos los elementos.

## Instrucciones generales

- Deberás completar las siguientes consignas basadas en cada una de las fases vistas.
- La entrega debe incluir código organizado y bien estructurados en un formato claro y profesional.
- Utilizá `README.md` para entender el código y asegurate de que los datos sean comprensibles y bien categorizados.

## Automatización de Login

- Navegar a la página de login de sucedemo.com
- Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
- Validar login exitoso verificando que se haya redirigido a la página de inventario

**Criterios mínimos:**

- Login automatizado con espera explicita y validación de /inventory.html y "Products/Swag Labs".

## Navegación y verificación del catálogo: (Clases 6 a 8)

**Caso de prueba de navegación:*

- Verificar que el título de la página de inventario sea correcto
- Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)
- Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)

**Criterios mínimos:**

- Valida título
- Valida presencia de productos
- Lista nombre/precio del primero.

## Interacción con productos: (Clase 8)

**Caso de prueba de carrito:**
- Añadir un producto al carrito haciendo clic en el botón correspondiente
- Verificar que el contador del carrito se incremente correctamente
- Navegar al carrito de compras
- Comprobar que el producto añadido aparezca correctamente en el carrito

**Criterios mínimos:**

- Agrega primer producto
- Verifica item en carrito.

## Repositorio en GitHub:

- Subí el proyecto a un repositorio en GitHub
- Realizá commits frecuentes y con mensajes descriptivos que muestren el progreso del proyecto

### README.md:

**Incluí un archivo README.md que explique:**
  
- El propósito del proyecto
- Las tecnologías utilizadas
- Cómo instalar las dependencias
- Cómo ejecutar las pruebas

### Generar reporte en HTML de las pruebas realizadas:

```bash
pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html
```

## Funcionalidad esperada:

- Los casos de prueba deben ejecutarse correctamente en el sitio saucedemo.com
- Las validaciones deben ser claras y específicas para cada paso
- El código debe ser legible y estar bien organizado
- Los tests deben ser independientes entre sí (la falla de uno no debe afectar a los demás)

---

## Entregables:

- Repositorio público en GitHub con todo el código del proyecto.
- Archivo `README.md` que incluya:
  - Propósito del proyecto
  - Tecnologías utilizadas
  - Instrucciones de instalación de dependencias
  - Comando para ejecutar las pruebas (por ejemplo: `pytest -v --html=reporte.html`)
- Reporte `HTML` generado por `Pytest` con resultados de la ejecución.
- Evidencias adicionales: capturas de pantalla automáticas en caso de fallos y logs de ejecución.

## Formato de entrega:

- **Nombre del repositorio:** `pre-entrega-automation-testing-[nombre-apellido]`.
- **Estructura mínima de carpetas:**
  - `tests/`
  - `utils/` (funciones auxiliares)
  - `datos/` (si aplica datos externos como CSV/JSON)
  - `reports/` (reportes HTML y capturas)
- Compartir **enlace** al repositorio antes de la fecha límite.
- **Commits** frecuentes y con mensajes descriptivos que reflejen el progreso.
- README.md completo y claro.

