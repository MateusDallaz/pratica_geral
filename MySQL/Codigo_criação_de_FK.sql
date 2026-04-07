CREATE TABLE estado(
id_estado INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(45) NOT NULL,
sigla VARCHAR(5),
região VARCHAR(45),
populacao INT,
area_km2 FLOAT,
CONSTRAINT fkid_pais FOREIGN KEY
(id_pais) REFERENCES pais(id_pais)
);

DESCRIBE pais