
```mermaid
graph TD
    %% Atributos Base
    Pelo[Tiene pelo] --> Mamifero((Mamífero))
    Leche[Da leche a crías] --> Mamifero
    Plumas[Tiene plumas] --> Ave((Ave))
    Vuela[Vuela] --> Ave
    Huevos[Pone huevos] --> Ave

    %% Clasificación Mamíferos
    Mamifero -->|Come carne| Carnivoro((Carnívoro))
    Mamifero -->|Tiene pezuñas| Ungulado((Ungulado))
    Mamifero -->|Muy pesado + Cuerno en hocico| Rinoceronte
    Mamifero -->|Enorme + Gris + Vive en agua| Hipopotamo

    %% Clasificación Carnívoros
    Carnivoro -->|Leonado + Manchas oscuras| Guepardo(Guepardo)
    Carnivoro -->|Leonado + Rayas negras| Tigre(Tigre)

    %% Clasificación Ungulados
    Ungulado -->|Cuello largo + Manchas oscuras| Jirafa(Jirafa)
    Ungulado -->|Rayas negras| Cebra(Cebra)

    %% Clasificación Aves
    Ave -->|Nada + Blanco y negro| Pinguino
    Ave -->|Vuela muy bien| Albatros(Albatros)
    Ave -->|Tarsos emplumados| AguilaReal
    Ave -->|Planea estable + No vuela en V| AguilaReal

    %% Regla paralela rinoceronte
    PielGruesa[Piel gruesa en placas + Gris + Come plantas] -.-> Rinoceronte