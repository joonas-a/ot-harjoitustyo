```mermaid
  sequenceDiagram
    participant main
    participant HKL as laitehallinto
    participant L as rautatietori
    participant R as ratikka6
    participant B as bussi244
    participant K as lippu_luukku
    participant KK as kallen_kortti
    
    main->>HKL: HKLLaitehallinto()
    main->>L: Lataajalaite()
    main->>R: Lukijalaite()
    main->>B: Lukijalaite()
    
    main->>HKL: lisää_lataaja(rautatietori)
    main->>HKL: lisää_lukija(ratikka6)
    main->>HKL: lisää_lukija(bussi244)
    
    main->>K: Kioski()
    main->>K: osta_matkakortti("Kalle")
    K->>KK: Matkakortti("Kalle")
    K-->>main: kallen_kortti
    
    main->>L: lataa_arvoa(kallen_kortti, 3)
    L->>KK: kasvata_arvoa(3)
    
    main->>R: osta_lippu(kallen_kortti, 0)
    R->>KK: arvo
    KK-->>R: 3
    R->>KK: vahenna_arvoa(1,5)
    R-->>main: True
    
    main->>B: osta_lippu(kallen_kortti, 2)
    B->>KK: arvo
    KK-->>B: 1.5
    B-->>main: False
