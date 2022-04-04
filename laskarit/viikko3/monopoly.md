### Tehtävä 1

```mermaid
classDiagram
  Monopoli "1" -- "1" Pelilauta
  Monopoli "1" -- "2-8" Pelaaja
  Pelilauta "1" -- "40" Peliruutu
  Peliruutu "1" --> "1" Seuraava ruutu
  Pelaaja "1" -- "1" Pelinappula
  Monopoli "1" -- "2" Noppa
  Pelaaja "1" ..> "2" Noppa
  Pelinappula "1" --> "1" Peliruutu
 ```
 ### Tehtävä 2
