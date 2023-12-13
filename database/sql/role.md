# Crear Roles: 
usuarios para mejorar el control de nuestra base de datos

# \h CREATE ROLE

* \h CREATE ROLE; Monstrara una lista

where option can be:

      SUPERUSER | NOSUPERUSER
    | CREATEDB | NOCREATEDB
    | CREATEROLE | NOCREATEROLE
    | INHERIT | NOINHERIT
    | LOGIN | NOLOGIN
    | REPLICATION | NOREPLICATION
    | BYPASSRLS | NOBYPASSRLS
    | CONNECTION LIMIT connlimit
    | [ ENCRYPTED ] PASSWORD 'password' | PASSWORD NULL
    | VALID UNTIL 'timestamp'
    | IN ROLE role_name [, ...]
    | IN GROUP role_name [, ...]
    | ROLE role_name [, ...]
    | ADMIN role_name [, ...]
    | USER role_name [, ...]
    | SYSID uid

# CREATE NEW ROLE

CREATE ROLE usuario_role1;

# Create Role with Login

CREATE ROLE usuario_role1 with LOGIN;

* Permite tener acceso para logearse, o para revisar las tablas, los permistos van de acuerdo a que puede y que no puede hacer el usuario, pero debera poseer una contraseña

# Alter Role with password:

ALTER ROLE usuario_role1 WITH PASSWORD '1234admin';

* Va permitir que el usuario tenga contraseña

# Create Role with superuser

CREATE ROLE usurio_role1 WIRH SUPERUSER;

* Tiene todo los permiso, puede editar, eliminar y crear tablas.

user: user_consult 
pass:etc123

