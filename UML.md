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

# Use Case Diagram

@startuml

left to right direction

actor "Tourist" << human >> as T
actor "ZooStaff" << human >> as ZS

rectangle "Digital Zoo\nManagement System" {
  
  rectangle "Staff Portal" << application >> {
     
    rectangle "Animal\nManagement"{
      usecase (CRUD Animal) as UC1

    }

  }

  rectangle "Tourist Interface" << application >> {


    usecase (Browse Informantion) as UC5

  }
  
  rectangle "Database Server" << server >> {
    usecase (Store Data) as UC7
    usecase (Return Data) as UC8
  }
  
}

ZS --> UC1

UC1 --> UC7

UC8 --> ZS

T --> UC5

UC5 --> UC8

UC8 --> T
@enduml