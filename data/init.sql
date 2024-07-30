CREATE DATABASE demobahasa;
ALTER DATABASE demobahasa CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use demobahasa;

CREATE TABLE sense (
    id INT NOT NULL AUTO_INCREMENT,
    pos VARCHAR(30),
    definition VARCHAR(30)
);

CREATE TABLE lexicon (
    id INT NOT NULL AUTO_INCREMENT,
    written_form NVARCHAR(30),
    origin NVARCHAR(30),
    surface_ipa NVARCHAR(50),
    senses ????????,
    surface_simple NVARCHAR(30)
);

