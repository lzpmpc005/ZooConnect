# To see diagrams below go to PlantUML, paste and copy the scripts
https://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000

# Class Diagram
@startuml
left to right direction

class Staff{
    - «PK»id: Integer
    - username: String
    - password: String
}

class Zookeeper{
    - «PK»id: Integer
    - «FK»responsibility: Integer
    - «FK»qualification: Integer
}

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
    - status: String
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

class CareLog{
    - «PK»log_id: Integer
    - «FK»animal_id: Integer
    - «FK»zookp_id: Integer
    - weight: Integer
    - temperature: Integer
    - diet: String
    - medicine: String
    - date: String
}

class Tour{
    - «PK»id: Integer
    - «FK»staff: Integer
    - route: Dictionary
    - duration: Dictionary
    - activity: Dictionary
    - animal: Dictionary

}


Zookeeper --|> Staff

Species "1" --> "0..*" Animal: has
Venue "1" --> "0..*" Animal: has
Animal "1" --> "0..*" CareLog: has
Zookeeper "1" --> "0..*" CareLog: has


@enduml
# Use Case Diagram

@startuml

left to right direction

actor "Tourist" << human >> as T
actor "ZooStaff" << human >> as ZS

rectangle "Digital Zoo\nManagement System" {
  
  rectangle "Staff Portal" << application >> {
   
    rectangle "Animal Info\nManagement"{
      usecase (Create Animal) as UC1
      usecase (Delete Animal) as UC2
      usecase (Search Animal) as UC3
      usecase (Update Animal) as UC4
    }
    rectangle "Animal Care\nRecord"{
      usecase (Add log of daliy routine) as UC9

    }
    rectangle "Tour Route\nManagement"{
      usecase (Create route for tour) as UC11

    }


  }

  rectangle "Tourist Interface" << application >> {


    usecase (Browse Informantion) as UC5
    usecase (Give Feedback) as UC10

  }
  
  rectangle "Database Server" << server >> {
    usecase (Store Data) as UC7
    usecase (Request Data) as UC8
  }
  
}

ZS --> UC1
ZS --> UC2
ZS --> UC3
ZS --> UC4
ZS --> UC9
ZS --> UC11

UC1 --> UC7
UC2 --> UC7
UC3 --> UC7
UC4 --> UC7
UC9 --> UC7
UC10 --> UC7
UC11 --> UC7


T --> UC5
T --> UC10

UC5 --> UC8