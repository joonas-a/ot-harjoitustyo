```mermaid
classDiagram
index <-- level
index <-- game_Loop
index <-- event_queue
index <-- clock
index <-- renderer
level <|-- player
level <|-- floor
application <|-- index
```
