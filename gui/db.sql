create database uniqode;

create table alumno (
	no_cuenta int not null,
    nombre varchar(40),
    paterno varchar(25),
    materno varchar(25),
    primary key (no_cuenta)
);

create table bitacora (
	id int not null auto_increment, 
    nombre_al varchar(60), 
    nocuenta_al int not null,
    aula varchar(25),
    materia varchar(25),
    fecha varchar(12),
    foreign key (nocuenta_al) references alumno(no_cuenta),
    primary key(id)
);
