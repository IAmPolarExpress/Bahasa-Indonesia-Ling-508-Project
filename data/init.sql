CREATE DATABASE demobahasa;
ALTER DATABASE demobahasa CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use demobahasa;

CREATE TABLE senses (
    id INT NOT NULL AUTO_INCREMENT,
    pos ENUM('NOUN','VERB','ADJECTIVE','ADVERB','PREPOSITION','CONJUNCTION','INTERJECTION'),
    definition VARCHAR(30)
);

CREATE TABLE lexicon (
    id INT NOT NULL AUTO_INCREMENT,
    written_form NVARCHAR(30),
    origin ENUM('DUTCH','JAPANESE','ENGLISH','MALAY','OTHER'),
    surface_ipa NVARCHAR(50),
    senses VARCHAR(200),
    surface_simple NVARCHAR(30)
);

INSERT INTO senses
    (pos, definition)
VALUES
    ('ADJECTIVE','male'),
    ('PREPOSITION','but'),
    ('VERB','study');

INSERT INTO lexicon
    (written_form, origin, surface_ipa, senses, surface_simple)
VALUES
    ('laki-laki', 'MALAY', 'ˈlakilaki', 1, 'laki-laki'),
    ('untuk', 'MALAY', 'ˈuntuk', 2, 'untuk'),
    ('belajar', 'MALAY', 'bəˈladʒar', 3, 'bəlajar')

