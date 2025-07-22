CREATE DATABASE demobahasa;
ALTER DATABASE demobahasa CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use demobahasa;

CREATE TABLE senses (
    id INT NOT NULL AUTO_INCREMENT,
    pos ENUM('NOUN','VERB','ADJECTIVE','ADVERB','PREPOSITION','CONJUNCTION','INTERJECTION'),
    definition VARCHAR(30),
    PRIMARY KEY (id)
);

CREATE TABLE lexicon (
    id INT NOT NULL AUTO_INCREMENT,
    written_form NVARCHAR(30),
    origin ENUM('DUTCH','JAPANESE','ENGLISH','MALAY','OTHER'),
    surface_ipa NVARCHAR(50),
    senses VARCHAR(200),
    surface_simple NVARCHAR(30),
    PRIMARY KEY (id)
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
    /*('laki-laki', 'MALAY', N'test', 1, N'test2'),*/
    /*('untuk', 'MALAY', N'test', 2, N'test2'),*/
    /*('belajar', 'MALAY', N'test', 3, N'test2');*/
    ('laki-laki', 'MALAY', N'ˈlakilaki', 1, N'laki-laki'),
    ('untuk', 'MALAY', N'ˈuntuk', 2, N'untuk'),
    ('belajar', 'MALAY', N'bəˈladʒar', 3, N'bəlajar');

