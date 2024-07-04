CREATE DATABASE plataforma_educativa;

USE plataforma_educativa;

CREATE TABLE usuarios_basico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    documento VARCHAR(255) NOT NULL
);

CREATE TABLE usuarios_completo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    documento VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    localidad VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    cursos TEXT NOT NULL
);
