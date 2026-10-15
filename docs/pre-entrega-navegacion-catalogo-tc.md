# Casos de prueba para navegación y verificación del catálogo

---

## Verificar que el título de la página de inventario sea correcto

precondiciones:
- usuario autenticado en SauceDemo con credenciales válidas
- navegador situado en la página del catálogo (`/inventory.html`)

pasos:
- obtener el elemento contenedor del título del header (`.app_logo`)
- verificar que el texto del título del header sea "Swag Labs"
- obtener el elemento contenedor de productos (`data-test="title"`)
- verificar que el título del catálogo sea "Products"

---

## Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)

precondiciones:
- usuario autenticado en SauceDemo con credenciales válidas
- navegador situado en la página del catálogo (`/inventory.html`)

datos de prueba esperados (primer producto):
- nombre: "Sauce Labs Backpack"
- precio: "$29.99"

pasos:
- obtener la lista de elementos de todos los productos visibles usando el selector de clase `.inventory_item`
- verificar que la cantidad de productos obtenidos sea mayor a cero
- capturar el primer producto de la lista (índice 0)
- obtener el elemento contenedor del nombre del primer producto (`data-test="inventory-item-name"`)
- verificar que el nombre del primer producto obtenido es "Sauce Labs Backpack" 
- obtener el elemento contenedor del precio del primer producto (`data-test="inventory-item-price"`)
- verificar que el precio del primer producto obtenido es "$29.99"

---

## Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)

precondiciones:
- usuario autenticado en SauceDemo con credenciales válidas
- navegador situado en la página del catálogo (`/inventory.html`)

pasos:
- obtener el elemento botón del menú hamburguesa (ID: `react-burger-menu-btn`)
- verificar que el botón del menú hamburguesa esté visible
- obtener el elemento de filtro de productos (`data-test="product-sort-container"`)
- verificar que el elemento de filtro esté visible 
- obtener el elemento del carrito de compras (`data-test="shopping-cart-link"`)
- verificar que el elemento del carrito de comrpas esté visible
