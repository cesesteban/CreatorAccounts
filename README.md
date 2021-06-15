# CreatorAccounts

El creatorAccounts se encarga de crear cuentas de usuarios en el sitio "https://es.chaturbate.com/accounts/register/" de manera automatica. 
Al ejecutarlo se debe especificar en la cosola el numero de cuentas que se desea crear.
Cuando termina de crear un usuario la web se reinicia y elige al azar uno entre diez proxys, esto lo hace mas real. 
El nombre de usuario se crea con los datos que provee la API "namey", de esta manera se logra un nombre diferente por cada usuario que se crea, al mismo tiempo la aplicacion inserta al final de la concatenacion del nombre y el apellido alguno digitos para que exitan menos probabilidades de que el nombre de usuario exista en la db.
Antes de iniciar el main.py se debe especificar la correcta ruta del chrome driver que se encuentra dentro de la carpeta utils, linea 30 del archivo main.py.
Al finalizar el programa contaremos con un file.txt que nos dara un registro de los datos de los usuarios creados.

The creatorAccounts is responsible for creating user accounts on the site "https://es.chaturbate.com/accounts/register/" automatically.
When executing it, the number of accounts to be created must be specified in the console.
When you finish creating a user, the web restarts and randomly chooses one of ten proxies, this makes it more real.
The user name is created with the data provided by the "namey" API, in this way a different name is achieved for each user that is created, at the same time the application inserts at the end of the concatenation of the name and surname some digits so that the username is less likely to exist in the db.
Before starting the main.py, the correct path of the chrome driver must be specified, which is found in the utils folder, line 30 of the main.py file.
At the end of the program we will have a file.txt that will give us a record of the data of the created users.



--*cesesteban.
