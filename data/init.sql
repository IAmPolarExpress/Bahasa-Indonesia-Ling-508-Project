CREATE DATABASE dictionary;
ALTER DATABASE dictionary CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use dictionary;

CREATE TABLE word_info (
    english_form VARCHAR(30),
    romanised_hindi NVARCHAR(30),
    devanagari NVARCHAR(30),
    pos VARCHAR(30),
    gender VARCHAR(30),
    definition VARCHAR(300));

INSERT INTO word_info
(english_form, romanised_hindi, devanagari, pos, gender, definition)
VALUES
('book', N'kitaab', N'किताब', 'noun', 'f','physical object consisting of a number of pages bound together'),
('tea',N'cāya',N'चाय','noun','f','a beverage made by steeping tea leaves in water'),
('water',N'pānī',N'पानी','noun','m','a liquid that descends from the clouds as rain, forms streams, lakes, and rivers'),
('you',N'tuma',N'तुम','pronoun',NULL,'the one being addressed, pronoun of the second person singular')
