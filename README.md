# Ohjelmistotekniikka, harjoitustyö

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/joonas-a/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Tuntikirjanpito](https://github.com/joonas-a/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

- [Changelog](https://github.com/joonas-a/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

- [Arkkitehtuuri](https://github.com/joonas-a/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

- [Käyttöohje](https://github.com/joonas-a/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

- [Testausdokumentti](https://github.com/joonas-a/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

## Tasohyppelypeli

### Käyttäänotto

- Asenna riippuvuudet ```poetry install```

- Alusta SQLite tietokanta ```poetry run invoke build```

- Tämän jälkeen pelin voi avata suorittamalla ```poetry run invoke start```

- Dokumentaation [Käyttöohje](https://github.com/joonas-a/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)-sivulla ohjeita sovelluksen käyttämiseen liittyen

### Muut komentorivikomennot

- Suorita testi(t) ```poetry run invoke test```

- Generoi testikattavuusraportti ```poetry run invoke coverage-report```

- Pylint tarkastukset ```poetry run invoke pylint```
