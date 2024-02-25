# To see diagrams below go to PlantUML, paste and copy the scripts
https://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000

# Class Diagram

@startuml
left to right direction

class Species {
    - «PK»id: Integer
    - name: String
    - habitat: String
    - temperature: Integer
    - humidity: Integer
    - light_intensity: Integer

}


class Animal {
    - «PK»id: Integer
    - name: String
    - age: Integer
    - diet: String
    - «FK»species: Integer
    - «FK»venue: Integer

}


class Venue {
    - «PK»id: Integer
    - name: String
    - type: String
    - location: String
    - size: Integer
    - temperature: Integer
    - humidity: Integer
    - light_intensity: Integer

}


Species "1" --> "0..*" Animal: has
Venue "1" --> "0..*" Animal: has

@enduml
