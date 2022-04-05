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
  Peliruutu "1" <|-- "1" Vankila
  Peliruutu "1" <|-- "1" Aloitusruutu
  Peliruutu "1" <|-- "1" Sattuma
  Peliruutu "1" <|-- "1" Yhteismaa
  Peliruutu "*" <|-- "1" Asemat
  Peliruutu "*" <|-- "1" Laitokset
  Peliruutu "*" <|-- "1" Katu
  Monopoli "1" --> "1" Vankila
  Monopoli "1" --> "1" Aloitusruutu
  Peliruutu "1" --> "1" Toiminto
  Aloitusruutu "1" --> "1" Toiminto
  Vankila "1" --> "1" Toiminto
  Sattuma "1" --> "1" Toiminto
  Yhteismaa "1" --> "1" Toiminto
  Kortti "*" <-- "1" Sattuma
  Kortti "*" <-- "1" Yhteismaa
  Talo "1-4" <-- "1" Katu
  Hotelli "1" <-- "1" Katu
  Raha "*" <-- "1" Pelaaja
  Pelaaja "1" --> "*" Katu
  
  class Kortti {
    Tominto
  }
  ```
