# Talento Tech - Automatización QA

## Propósito del Proyecto

El propósito de este proyecto es aplicar técnicas de automatización de pruebas utilizando Python, Pytest y Selenium Web Driver.

El sitio bajo prueba es [SauceDemo](https://www.saucedemo.com), una aplicación web demo especialmente diseñada para prácticas de testing.

## Tecnologías Utilizadas

- `Python` como lenguaje principal
- `Pytest` para estructura de testing
- `Selenium WebDriver` para automatización
- `Git` y `GitHub` para control de versiones

## Instrucciones para utilizar este repositorio

### Clonar repositorio

```bash
git clone https://github.com/matias-ac/talento-tech-automation-testing.git
```

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar el entorno virtual

**Windows:**
```bash
.\venv\Scripts\activate
```

**MacOS/Linux:**
```bash
source venv/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

## Comandos para ejecución de pruebas

- `pytest -v`: ejecuta los tests con mayor verbosidad (nivel de detalle) 
- `pytest -v -m smoke`: solo ejecuta tests críticos
- `pytest -v -m exception`: solo ejecuta tests que validan errores 
- `pytest --html=reports/report.html --self-contained-html`

## Estructura del Proyecto

```
talento-tech-automation-testing/
|-- data                    # datos externos como CSV/JSON 
|-- docs                    # consigna, links útiles, guías, etc.
|-- reports                 # reportes HTML y capturas
|-- tests                   # archivos de tests 
|-- utils                   # funciones auxiliares
.gitignore                  
README.md
pytest.ini
requirements.txt
```
