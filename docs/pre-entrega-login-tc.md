# Casos de prueba para el login

---

## login con credenciales válidas

datos de prueba:
- username: 'standard_user'
- password: 'secret_sauce'

pasos:
- abrir navegador
- tipear en la barra de navegación la URL de SauceDemo
- ingresar usuario válido en el campo "Username"
- ingresar password válida en el campo "Password"
- hacer click en el botón "Login"
- verificar redirección a la URL "/inventory.html"
- verificar que la sección "Products" está visible

---

## login con credenciales inválidas

datos de prueba:
- username: 'usuario_incorrecto'
- password: 'password_incorrecta'

pasos:
- abrir navegador
- tipear en la barra de navegación la URL de SauceDemo
- ingresar usuario inválido en el campo "Username"
- ingresar password inválida en el campo "Password"
- hacer click en el botón "Login"
- observar la aparición del elemento <h3> con atributo data-test="error"
- observar mensaje de error "Epic sadface: Username and password do not match any user in this service"

---

## login sin ingresar "Password"

datos de prueba:
- username: 'standard_user'
- password: ''

pasos:
- abrir navegador
- tipear en la barra de navegación la URL de SauceDemo
- ingresar usuario válido en el campo "Username"
- no ingresar nada y dejar en blanco el campo "Password"
- hacer click en el botón "Login"
- observar la aparición del elemento <h3> con atributo data-test="error"
- observar mensaje de error "Epic sadface: Password is required"
