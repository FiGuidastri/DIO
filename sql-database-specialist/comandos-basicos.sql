SHOW DATABASES;

CREATE DATABASE firstExample;

USE firstExample;

CREATE TABLE periodicos
(
    id INT
    AUTO_INCREMENT,
    nome_periodico VARCHAR
    (120),
    issn INT,
    id_editora INT,
    PRIMARY KEY
    (id)
);

SHOW TABLES;

CREATE TABLE editora
    (
        id INT
        AUTO_INCREMENT,
    nome_editora VARCHAR
        (120),
    pais INT,
    PRIMARY KEY
        (id)
);

ALTER TABLE
    periodicos
ADD
    CONSTRAINT fk_editora_periodico FOREIGN KEY (id_editora) REFERENCES editora (id);

ALTER Table
    editora
MODIFY
    COLUMN pais VARCHAR(120);

INSERT INTO
    editora
            (nome_editora, pais)
        VALUES
            ('IEEE', 'EUA'),
            ('DataScienceMagazine', 'EUA');

SELECT
    *
FROM
    editora;

 INSERT INTO
    periodicos
            (
            nome_periodico,
            issn,
            id_editora
            )
        VALUES
            (
                'Special Issue',
                '12345678',
                '1'
    );

SELECT
    *
FROM
    periodicos;