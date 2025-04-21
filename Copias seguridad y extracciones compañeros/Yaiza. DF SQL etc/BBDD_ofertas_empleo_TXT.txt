CREATE DATABASE ofertas_empleo;
USE ofertas_empleo;

CREATE TABLE empresa (
	id_empresa INT AUTO_INCREMENT PRIMARY KEY,
	empresa VARCHAR(256)
);

CREATE TABLE ubicacion (
	id_ubicacion INT AUTO_INCREMENT PRIMARY KEY,
    ubicacion VARCHAR(256)
);

CREATE TABLE skills (
	id_skills INT AUTO_INCREMENT PRIMARY KEY,
    skills VARCHAR(256)
);

CREATE TABLE tecnologias_aptitudes (
	id_tecnologias INT AUTO_INCREMENT PRIMARY KEY,
    tecnologias_aptitudes VARCHAR(256)
);

CREATE TABLE idiomas (
	id_idiomas INT AUTO_INCREMENT PRIMARY KEY,
    idiomas VARCHAR(10)
);

CREATE TABLE beneficios (
	id_beneficios INT AUTO_INCREMENT PRIMARY KEY,
	beneficios VARCHAR(256)
);

CREATE TABLE modalidad (
	id_modalidad INT AUTO_INCREMENT PRIMARY KEY,
    modalidad VARCHAR(10)
);

CREATE TABLE jornada (
	id_jornada INT AUTO_INCREMENT PRIMARY KEY,
    jornada VARCHAR(10)
);

CREATE TABLE contrato (
	id_contrato INT AUTO_INCREMENT PRIMARY KEY,
    contrato VARCHAR(10)
);

CREATE TABLE portal_empleo (
	id_portal_empleo INT AUTO_INCREMENT PRIMARY KEY,
	portal_empleo VARCHAR(256)
);

CREATE TABLE ofertas (
    id_urls VARCHAR(200) PRIMARY KEY,
    fecha DATE,
    oferta VARCHAR(256),
    id_empresa INT,
    funcion VARCHAR(256),
    salario_min FLOAT,
    salario_max FLOAT,
    estudios VARCHAR(256),
    experiencia INT,
    id_ubicacion INT,
    id_modalidad INT,
    id_jornada INT,
    id_contrato INT,
    vacaciones INT,
    id_portal_empleo INT,
    descripcion VARCHAR(1000),
    FOREIGN KEY (id_empresa) REFERENCES empresa (id_empresa),
    FOREIGN KEY (id_ubicacion) REFERENCES ubicacion (id_ubicacion),
    FOREIGN KEY (id_modalidad) REFERENCES modalidad (id_modalidad),
    FOREIGN KEY (id_jornada) REFERENCES jornada (id_jornada),
    FOREIGN KEY (id_contrato) REFERENCES contrato (id_contrato),
	FOREIGN KEY (id_portal_empleo) REFERENCES portal_empleo (id_portal_empleo)
);

CREATE TABLE oferta_tecnologia (
	id_urls VARCHAR(200),
	id_tecnologias INT,
    PRIMARY KEY (id_urls, id_tecnologias),
    FOREIGN KEY (id_urls) REFERENCES ofertas (id_urls),
    FOREIGN KEY (id_tecnologias) REFERENCES tecnologias_aptitudes (id_tecnologias)
);

CREATE TABLE oferta_skill (
    id_urls VARCHAR(200),
    id_skills INT,
    PRIMARY KEY (id_urls, id_skills),
    FOREIGN KEY (id_urls) REFERENCES ofertas (id_urls),
    FOREIGN KEY (id_skills) REFERENCES skills (id_skills)
);

CREATE TABLE oferta_idioma (
    id_urls VARCHAR(200),
    id_idiomas INT,
    PRIMARY KEY (id_urls, id_idiomas),
    FOREIGN KEY (id_urls) REFERENCES ofertas (id_urls),
    FOREIGN KEY (id_idiomas) REFERENCES idiomas (id_idiomas)
);

CREATE TABLE oferta_beneficio (
    id_urls VARCHAR(200),
    id_beneficios INT,	
    PRIMARY KEY (id_urls, id_beneficios),
    FOREIGN KEY (id_urls) REFERENCES ofertas (id_urls),
    FOREIGN KEY (id_beneficios) REFERENCES beneficios (id_beneficios)
);

