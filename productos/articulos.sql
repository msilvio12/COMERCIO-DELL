CREATE TABLE PRODUCTOS (
NOMBRE VARCHAR(100) PRIMARY KEY,
PRECIO INT PRIMARY KEY,
VENCIMIENTO INT NOT NULL
CANTIDAD REAL NOT NULL,
);

CREATE TABLE USUARIO (
NOMBRE VARCHAR(50) PRIMARY KEY,
APELLIDO VARCHAR(50) PRIMARY KEY,
EDAD INT NOT NULL,
DOMICILIO VARCHAR(70) NOT NULL,

);

CREATE TABLE CARRITO(
id PRODUCTOS BIGINT(50),
CARRO INT(30) NOT NULL,

);