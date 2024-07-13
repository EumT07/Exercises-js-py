# Official Link
Postgresql: https://www.tutorialkart.com/postgresql/psql-shell-commands/

# Course
https://www.youtube.com/watch?v=qw--VYLpxG4&list=LL&index=5&t=8423s

# Database Generated
https://mockaroo.com/


# Database

Place where we could save informations

* store
* manipulate
* retrieve

# SQL: Structured Query Language

Manage data held in a relational database
Easy to learn
Very powerful
Used all over the internet
Object relational database management system
Open source

data is store in tables

# Postgresql
Es una base de dato Open source utiliza el lenguaje sql desde hace mas de 40 años

Modelo de bases de datos relacionales, se relacionan las diferentes colummnas, se evita que haya duplicados de datos, existen dos tipos de llaves, llaves primarias y llaves Foraneas

Llave foraneas: es una llave primaria de otra tabla que se relaciona en una columna con otra tabla
 
Tipos de datos:
    Number:
            int: integer
            float: floating 
            bigint: It uses 8 bytes of storage.
            BIGSERIAL : 8 bytes
    String:
            varchar(mas characters)
            text
            char
    Date:
            date
            datetime
            time
            timestamp
    Others
    Blob(Binary Large Object): img, videos

    A Binary Large Object (blob) is a collection of data of an arbitrary size. Blobs do not have to follow a given format or have any metadata associated with them. They are a series of bytes, with each byte made up of 8 bits (a 1 or a 0, hence the "binary" descriptor). Any type of data can go in a blob.binary

Jerarquia:
    Null
    Number
    Special Characters
    letters
    Nulls Last: change null ordern

    https://www.postgresql.org/docs/current/datatype.html

# postgresql: CRUD Commands
* C: Create Tables
* R: Read Tables
* U: Update Tables
* D: Delete Tales

# CREATE

* Create Table 

CREATE TABLE person (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(150) NOT NULL,
	gender VARCHAR(7) NOT NULL,
	date_of_birth DATE NOT NULL,
	country_of_birth VARCHAR(50)
);

* Insert Data

INSERT INTO person (
    first_name,
    last_name,
    email,
    gender,
    date_of_birth,
    country_of_birth)
    values ('Angel', 'Lopex', 'angelito@gmail.com', 'male', '2023-03-27', 'Colombia');

* Delete Data

DROP DATABASE "name of the data"

# READ or Search

* ( * )

    SELECT * FROM person; -> Traera Toda la tabla con sus resultados

    ![SELECT * FROM person;](img/1.png)

* propiedades: first_name, last_name, email etc.

    - SELECT first_name, email FROM person LIMIT 20;
    
        ** LIMIT N° ** : Traea un limite de 20 resultados
        ( Traera el nombre y sus emails de todos los resultados )

    ![SELECT first_name, email FROM person LIMIT 20;](img/2.png)

    - SELECT first_name as name, email, country_of_birth as country FROM person LIMIT 5;

        ** AS **: Permite renombrar una propiedad
        ( Traera el first_name como name, y country_of_birth como country de todos los resultados )
    
    ![SELECT first_name as name, email, country_of_birth as country FROM person LIMIT 20;](img/3.png)

    -SELECT first_name || ' ' || last_name AS Fullname FROM person LIMIT 10;


* Where
    WHERE name = ?
    Where Lastname = ?
    ect

    - SELECT * FROM person where id = 233;

        (Traera el resultado que coincida con el id : 233)

    ![SELECT * FROM person where id = 233;](img/4.png)
    
    
# Operadores Matematicos
* >  : menor que
        SELECT * FROM person where id > 10 LIMIT 20;

        ![SELECT * FROM person where id > 10 LIMIT 20;](img/5.png)

* <  : mayor que
        SELECT * FROM person where id > 10 LIMIT 20;

        ![SELECT * FROM person where id > 10 LIMIT 20;](img/6.png)

* >= : mayor e igual
* <= : menor e igual
* != : distinto

# Operadores Logicos

* AND
    -SELECT * FROM person where id > 20 and id < 30;

    ![SELECT * FROM person where id > 20 and id < 30;](img/7.png)

    - SELECT first_name || ' ' || last_name AS Fullname, email FROM person WHERE gender = 'Female' AND country_of_birth = 'Argentina';

    ![SELECT first_name || ' ' || last_name AS Fullname, email FROM person WHERE gender = 'Female' AND country_of_birth = 'Argentina';](img/9.png)

* OR
    - SELECT * FROM person where name='Job' or name='Lucas';

    ![ SELECT * FROM person where name='Job' or name='Lucas';](img/7.png)

* Not: negamos las condiciones

* LIMIT: limitar la busqueda

# Between
    Permite buscar valores dentro de un rango que se establece

    - SELECT * FROM person WHERE date_of_birth BETWEEN DATE '2023-01-01' AND '2023-12-31';

    ![SELECT * FROM person WHERE date_of_birth BETWEEN DATE '2023-01-01' AND '2023-12-31';](img/between.png)


# Like

    like "%gmail%" (Similar al =)
    " caracter a buscar % ": principio
    " % caracter a buscar ": final
    " % caracter a buscar % ": dentro de toda la palabra
    "%R" : al final : caracter a buscar termine en r
    "F%" : al principio : caracter a buscar que comience en f
	"name___":  caracteres y luego una numeracion de caracteres
                ejemplo carlos: c_____  buscara name que comience con c y posean cierta cantidad de caracteres

    - SELECT first_name As Name FROM person where first_name LIKE '%an' LIMIT 5;

    ![SELECT first_name As Name FROM person where first_name LIKE '%an' LIMIT 5;](img/like_1.png)

    ILIKE is the sme but with lowercase and uppcercase

# Order by
    ASC: 1 2 3 4 5
    SELECT * FROM person ORDER BY country_of_birth ASC;

    DESC: 5 4 3 2 1
    SELECT * FROM person ORDER BY country_of_birth DESC;

    LIMIT
    -SELECT * FROM person ORDER BY country_of_birth LIMIT 50;

    ![SELECT * FROM person ORDER BY country_of_birth LIMIT 50;](img/orderby1.png)

# Distinct
    Permite seleccionar un solo valor cuando se encuentren muchos, ejemplos los paises, en este caso sirve si hay muchas personas de una pais, podemos identificar o traernos , los paises existentes, sin tener que repetirlos. 

    SELECT DISTINCT country_of_birth FROM person ORDER BY country_of_birth;

    ![SELECT DISTINCT country_of_birth FROM person ORDER BY country_of_birth;](img/distinct1.png)

# OFFSET
    Permite comenzar a buscar, en la casilla (row) que se le indique.

    -SELECT * FROM person OFFSET 10 LIMIT 5;
    *Comienza a buscar en la fila 10 y hasta un limite de 5 casillas

    ![SELECT * FROM person OFFSET 10 LIMIT 5;](img/offset1.png)

    
![](img/)
# IN

    Permite buscar varios parametros, similar al or, solo que podemos englobarlos 

    -SELECT * FROM person WHERE country_of_birth IN ('Brazil','Venezuela','France');

    ![-SELECT * FROM person WHERE country_of_birth IN ('Brazil','Venezuela','France');](img/in.png)

# Group By

* Functions

    1. Count()
        - - SELECT country_of_birth AS Country, COUNT(*) FROM person GROUP BY country_of_birth;
    
    2. ORDER BY
        - SELECT country_of_birth AS Country, COUNT(*) FROM person GROUP BY country_of_birth ORDER BY country_of_birth;

    3. Having: Between Group and Order

        - SELECT country_of_birth AS Country, COUNT(*) 
        FROM person 
        GROUP BY country_of_birth 
        HAVING COUNT(*) > 12 
        ORDER BY country_of_birth;


# Numbers / math metods

1. MAX()
        - SELECT make, model, MAX(price) FROM vehicle WHERE make = 'Honda' GROUP BY make, model;
2. MIN()
        - SELECT make, model, MIN(price) FROM vehicle WHERE make = 'Honda' GROUP BY make, model;
3. AVG()
4. Round()
5. SUM()
        SELECT make, SUM(price) FROM vehicle GROUP BY make;

# Alias

1. COALESCE(,"NEW VALUE")

    Permite asignar un valor a un dato vacio
    ejemplo 
    COALASE(,"No email"); -> si algun usuario no inserto email entonces en su casilla tendra ese valor. 

# stamp and date

        -SELECT first_name, country_of_birth, date_of_birth, AGE(NOW(), date_of_birth) AS age FROM person;

# Primary key
        CONSTRAINT: restricciones
        PK: Primary Key unique value to indentify person or any object

        ALTER TABLE person ADD PRIMARY KEY (id);


# Unique constraine

si deseamos tener solo un correo, o usuario podemos alterar la tabla y espesificar que seran valores unicos, asi no permitira usurios con el mismo correo o user

        ALTER TABLE person ADD CONSTRAINT unique_email_addres UNIQUE (email);

        Delete:
        ALTER TABLE person DROP CONSTRAINT unique_email_addres;

        ALTER TABLE person ADD UNIQUE (id); --> diferente a la otra

# Check

        ALTER TABLE person ADD CONSTRAINT gender_contraint CHECK (gender = 'Female' OR gender = 'Male');
        ** para poder controlar que solo se instroduzca una de las 2 opciones **

# Delete

        DELETE * FROM person: It will delete all table
        DELETE FROM person WHERE name = 'marshal?

# Update

        UPDATE person SET email = "email@gmail.com" WHERE id = 234;
        UPDATE person SET email = "email@gmail.com", fistn_name = 'newName' WHERE id = 234;

# ON CONFLIT 

        Permite modificar la tabla cuando hay llaves establecidad o valores unicos que puedan drlos conflicto

        Ejemplo si intentamos ingresa un nuevo registro igual a uno ya existente, dara error, pero si le aplicarmos : 
        ON CONFLIT (id) DO NOTHING; procedera a no dar errores en cuyo caso que nuestro nuevo registro posea el mismo id para que funcione debemos estar seguro que la columna que vamos a editar no sea unica, si no lo es ejemplo el first_name entonces no tendra efecto.

        Para editar valores hacer lo siguiente

        insert into person (id, first_name, last_name, email, gender, date_of_birth, country_of_birth) 
        
        values (926, 'eublan', 'Mata', 'eublanmatamedina@gmail.com', 'Male', '1992-04-07', 'Venezuela')

        ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email,
        last_name = EXCLUED.last_name;

# returning *

        RETURNING * | returning id: permite devolver el id o todo los campos, de cualquier dato que hayamos insertado en ese momento


# FOREIGN KEYS and JOINS

        Para establecer un valor a la tabla car_id, debe editar la tabla

        UPDATE person SET car_id = "id car" WHERE id = "id person";

        Joins: combina tablas  cuando la llave primaria y las llaves foraneas se encuentran en las tablas.

        SELECT * FROM person JOIN car ON person.car_id = car.id;

        ![ SELECT * FROM person JOIN car ON person.car_id = car.id;](img/Join.png)

        SELECT person.first_name, car.model FROM person JOIN car ON person.car_id = car.id;

        (Tomora referencia principal en la busqueda de la tabla de la izquierda.)
        Left Join: Permite traer una tabla completa trae todos los records que no tengan relacion entre si.

        SELECT * FROM drivers LEFT JOIN vehicles ON vehicles.id = drivers.id;

        SELECT * FROM drivers LEFT JOIN vehicles ON vehicles.id = drivers.id WHERE vehicles.* IS NULL;

        Tablas Pgadmin

        SELECT * FROM passenger
        LEFT JOIN travel ON (travel.id_person = passenger.id)
        WHERE travel.id IS NULL;


        /x :Expanded display is on

# Delete FOREIGN KEYS 

        Eleminar estilo cascade eliminando la tabla que contenga el forean key

        DELETE FROM WHERE id = ;

# Export cvs

        Exportara un archivo excel con nuestra tabla para poder tenerlas ordenada

        \copy (SELECT * FROM person LEFT JOIN car ON car.id = person.car_id) TO '/users/The Crow/Desktop/database/carid.csv' DELIMITER ',' CSV HEADER;

# UUid: Universally unique identifier

        Check if you hava or not the extension

        SELECT * FROM pg_available_extensions;

        To choose

        CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

        \df: too se all functions

        uuid_generate_v4 --> this is random

        SELECT * FROM personuid JOIN caruid USING (car_uuid);


# add Forean key from pgadmin4 

ALTER TABLE route ADD CONSTRAINT route_train_fkey FOREIGN KEY (id_train)
        REFERENCES public.train (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE;



# Partition on postgresql 4

INSERT INTO public.timetravel(
	id_travel, date)
	VALUES (1, '2010-01-01');
	
CREATE TABLE timetravel2010 PARTITION OF timetravel
FOR VALUES FROM ('2010-01-01') TO ('2019-01-31'); 

seria el mes de enero dentro de un rango de 10 años del 2010 al 2019

# Block conditional
        
        SELECT id, first_name, birth,
        CASE
        WHEN birth > '01-01-2010' THEN
        'younger'
        ELSE
        'older'
        END
	FROM passenger;

        


