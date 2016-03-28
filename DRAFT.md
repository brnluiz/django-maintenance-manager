EnquiresList
  - Enquire
    - reference
    - title
    - description
    - user
    - createdAt
    - status
    - Location
      - postalcode
      - city
      - address
      - addressNumber
      - building
      ** flat number
      ** room
    - ReportsList
      - Report
        - details
        ** status
        - createdAt
        - employee

UserList
  User
    - name
    - surname
    - email
    - phone
    - createdAt
    - Location
      - postalcode
      - city
      - address
      - addressNumber
      - building
      - Flat
        - number
        - Room
          - identificator
    - EnquiresList

LocationList
  Location
    - postalcode
    - city
    - address
    - building
    - FlatsList
      - Flat
        - number
        - EnquiresList
        - RoomsList
          - Room
            - identificator

EmployeesList
  Employee
    - name
    - surname
    - email
    - phone
    - Role
      - title

RoleList
  Role
    - title
    - level
    - EmployeesList

StatusList
  - Status
    - title
    - EnquiresList