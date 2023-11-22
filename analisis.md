# Proyecto Tamagotchi: Carlito

## Descripcion general
El sistema gestionara una mascota virtual con solo 3 atributos: "Hambre", "Salud" y "Diversion"

## Analisis de requisitos
- Una vez transcurren 30 dias reales desde el nacimiento de la mascota, esta muere
- El atributo "Hambre" mide la necesidad de comer, con 0 unidades equivalentes a no tener hambre y 100 unidades equivalentes a tener mucha hambre
- El atributo "Salud" mide el bienestar de la mascota, con 0 unidades equivalentes a estar muy enfermo y 100 unidades a estar completamente sano
- El atributo "Diversion" mide el humor de la mascota, con 0 unidades equivalentes a estar muy triste y 100 unidades a estar muy feliz
- Si se realiza una accion que disminuye el hambre, pero el valor de disminucion es mayor que el valor de hambre actual, el hambre queda en 0 y el resto de unidades se pierden
- Si se realiza una accion que aumenta la salud, pero el valor de aumento mas el valor actual es mayor a 100, la salud queda en 100 y el resto de unidades se pierden
- La mascota puede comer un "Carlito", percibido como comida chatarra. Este disminuye el hambre en 5 unidades, pero aumenta la felicidad en 20
- La mascota puede comer "Brocoli", percibido como comida saludable. Este disminuye el hambre en 10 unidades, pero aumenta la felicidad en 10
- Se le puede dar "Ibuprofeno", que aumenta su salud en 25/50 unidades
- Se le puede dar "Viagra", que disminuye la salud en 50 unidades pero aumenta la diversion en 50 unidades
- Se le puede dar "Laxante", que aumenta la salud en 20 unidades pero aumenta el hambre en 50 unidades
- Puede usar "Feetfinder", que aumenta la diversion en 20 unidades pero disminuye la salud 5 unidades

## Requisitos
- Como maximo va a haber 5 botones
- Un boton destinado a funciones referidos a sacar el hambre
- Un boton destinado a funciones referidas a la higiene
- Un boton destinado a ver las estadisticas
- El sistema va a tener gestion de usuarios, un usuario va a tener una mascota y las mascotas van a únicas para cada usuario
- El sistema va a pedir iniciar sesion para cargar la mascota de un usuario
- El sistema va a tener una opcion de guardado para salir del mismo y actualizar los datos de la mascota en servidor

## Diagrama de actividades

Comer:
| Usuario | Interfaz |
|---------|----------|
| 1. Entra a la opcion comer ||
|| 2. Presenta opciones de alimento|
| 3. Elige una opcion||
|| 4. Actualizar los atributos|
|| 5. Vuelve al menu|

Salud: Similar a Comer

Diversion: Similar a Comer

Inicio de sesion:
| Usuario | Interfaz | Servidor |
|---------|----------|----------|
| 1. Ingresa las credenciales de inicio|||
| 2. Toca el boton de ingreso|||
|| 3. Envia al servidor una peticion de autentificacion ||
||| 4. Recibe las credenciales de inicio |
||| 5. Valida las credenciales de inicio |
||| 6. Devuelve el resultado de la validacion |
|| 7. Recibe el resultado de validacion ||
|| 8. Ejecuta la funcion asociada al resultado ||

Salir:
| Usuario | Interfaz | Servidor |
|---------|----------|----------|
| 1. Toca el boton de salir |||
|| 2. Envia la peticion de guardado ||
||| 3. Recibe la peticion |
||| 4. Guarda los datos de la peticion y devuelve el estado |
|| 5. Recibe la respuesta y la muestra al usuario ||

Tablas:
Usuario(Nombre, **_ID_**, Contraseña, _id-mascota_)
Mascota(Nombre, **_ID_**, Salud, Hambre, Diversion, _id-usuario_)

Tickets:
- Diseñar el login; Dificultad: Baja; Prioridad: Alta; Encargado: Tomimg
- Diseñar las peticiones de login; Dificultad: Media; Prioridad: Alta; Encargado: Indefinido
- Diseñar la pagina de la mascota; Dificultad: Media; Prioridad: Baja/Media; Encargado: Roman
- Modelar la base de datos; Dificultad: Media; Prioridad: Alta; Encargado: Indefinido
- Gestion de tiempo; Dificultad: Media; Prioridad: Media; Encargado: Indefinido
- Enrutamiento y responses; Dificultad: Media/Alta; Prioridad: Alta; Encargado: Jedi

## Diagrama de clases
|Mascota|
|---------|
|+hambre|
|+salud|
|+diversion|
|+textura|
|--------|
|setHambre()|
|setSalud()|
|setDiversion()|
|setTextura()|

|Usuario|
|------|
|+nombre|
|+mascota|
|+contraseña| 