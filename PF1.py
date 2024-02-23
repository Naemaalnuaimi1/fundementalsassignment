from enum import Enum


class Gender(Enum):
    """ Enumerator for gender"""
    MALE = 1
    FEMALE = 2


class Passenger:
    """ Class representing the passenger"""

    def __init__(self, firstName, lastName, email, passportNumber, gender):
        """ attributes of intialized object"""
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.passportNumber = passportNumber
        self.gender = gender

    # Setter and getters

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, firstName):
        self.firstName = firstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getPassportNumber(self):
        return self.passportNumber

    def setPassportNumber(self, passportNumber):
        self.passportNumber = passportNumber

    def getGender(self):
        return self.gender

    def setGender(self, gender):
        self.gender = gender

    def checkIn(self):  ###
        pass

    def showIdentification(self):  ##
        pass


class Flight:
    """ Class representing a flight """

    def __init__(self, flightNumber, departureLocation, destination, terminal, takeOffTime, arrivalTime):
        """ attributes of intialized object"""
        self.flightNumber = flightNumber
        self.departureLocation = departureLocation
        self.destination = destination
        self.terminal = terminal
        self.takeOffTime = takeOffTime
        self.arrivalTime = arrivalTime

    # setter and getter

    def getFlightNumber(self):
        return self.flightNumber

    def setFlightNumber(self, flightNumber):
        self.flightNumber = flightNumber

    def getDepartureLocation(self):
        return self.departureLocation

    def setDepartureLocation(self, departureLocation):
        self.departureLocation = departureLocation

    def getDestination(self):
        return self.destination

    def setDestination(self, destination):
        self.destination = destination

    def getTerminal(self):
        return self.terminal

    def setTerminal(self, Terminal):
        self.Terminal = Terminal

    def getTakeOffTime(self):
        return self.takeOffTime

    def setTakeOffTime(self, TakeOffTime):
        self.takeOffTime = takeOffTime

    def getArrivalTime(self):
        return self.arrivalTime

    def setArrivalTime(self, arrivalTime):
        self.arrivalTime = arrivalTime


class BoardingPass:
    """ Class representing a boarding pass"""

    def __init__(self):
        """ attributes of intialized object"""
        self.passenger = None
        self.flight = None
        self.seat = ""
        self.boardingTime = ""
        self._class = ""
        self.electronicTicketNum = 0

    # setter and getter

    def setPassenger(self, passenger):
        self.passenger = passenger

    def getPassenger(self):
        return self.passenger

    def setFlight(self, Flight):
        self.Flight = Flight

    def getFlight(self):
        return self.Flight

    def setSeat(self, Seat):
        self.Seat = Seat

    def getSeat(self):
        return self.Seat

    def setBoardingTime(self, boardingTime):
        self.boardingTime = boardingTime

    def getBoardingTime(self):
        return self.boardingTime

    def setClass(self, _class):
        self._class = _class

    def getClass(self):
        return self._class

    def setElectronicTicketNum(self, electronicTicketNum):
        self.electronicTicketNum = electronicTicketNum

    def getElectronicTicketNum(self):
        return self.electronicTicketNum



class AirportStaff:
    """ Class represting the airport staff """

    def __init__(self, staffFirstName, staffLastName, staffID, staffRole, gender):
        """ attributes of intialized object"""
        self.staffFirstName = staffFirstName
        self.staffLastName = staffLastName
        self.staffID = staffID
        self.staffRole = staffRole
        self.gender = gender

    # setter and getter

    def getStaffFirstName(self):
        return self.staffFirstName

    def setStaffFirstName(self, staffFirstName):
        self.staffFirstName = staffFirstName

    def getStaffLastName(self):
        return self.staffLastName

    def setStaffLastName(self, staffLastName):
        self.staffLastName = staffLastName

    def getStaffID(self):
        return self.staffID

    def setStaffID(self, staffID):
        self.staffID = staffID

    def getStaffRole(self):
        return self.staffRole

    def setStaffRole(self, staffRole):
        self.staffRole = staffRole

    def getGender(self):
        return self.gender

    def setGender(self, gender):
        self.gender = gender

    def issue_boarding_pass(self, passenger, flight_number, seat_number, departure_time, gate):
        boarding_pass = BoardingPass(passenger.get_name(), flight_number, seat_number, departure_time, gate)
        return boarding_pass

    def check_identification(self, passenger):
        pass


class SecurityStaff:
    """ Class representing a security staff """

    def __init__(self, employeeName, employeeID):
        self.employeeName = employeeName
        self.employeeID = employeeID

    def getEmployeeName(self):
        return self.employeeName

    def setEmployeeName(self, employeeName):
        self.employeeName = employeeName

    def getEmployeeID(self):
        return self.employeeID

    def setEmployeeID(self, employeeID):
        self.employeeID = employeeID

    def checkSecurityScreening(self, passeneger):
        pass


class Luggage:
    """ Class representing a luggage """

    def __init__(self, passenger_name, weight, destination, is_checked):
        self.passenger_name = passenger_name
        self.weight = weight
        self.destination = destination
        self.is_checked = False

    # Getter and Setter methods for attributes
    def get_passenger_name(self):
        return self.passenger_name

    def set_passenger_name(self, passenger_name):
        self.passenger_name = passenger_name

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_destination(self):
        return self.destination

    def set_destination(self, destination):
        self.destination = destination

    def get_is_checked(self):
        return self.is_checked

    def set_is_checked(self, is_checked):
        self.is_checked = is_checked


# I created objects of the classes
passenger = Passenger("James", "Smith", "JamesSmith@gmail.com", 1234, Gender.MALE)
flight = Flight(333, "Chicago - ORD", "New York - JFK", 2, "11:40", "13:30")
airport_staff = AirportStaff("Ali", "Alnuami", 132, "Security", Gender.MALE)
luggage = Luggage("James", 27, "New York", True)
securityStaff = SecurityStaff("Maya", 5555)
# Create a BoardingPass object
boarding_pass = BoardingPass()

# Set passenger, flight, and other details in the boarding pass
boarding_pass.setPassenger(passenger)
boarding_pass.setFlight(flight)
boarding_pass.setSeat("09A")
boarding_pass.setBoardingTime("11:20")
boarding_pass.setClass("First class")
boarding_pass.setElectronicTicketNum(629)

# Display boarding pass details
print("Passeneger Details:")
print("Passenger Name:", boarding_pass.getPassenger().getFirstName(), boarding_pass.getPassenger().getLastName(),
      ", Passenger Email:", boarding_pass.getPassenger().getEmail(), ", Passenger Passport Number:",
      boarding_pass.getPassenger().getPassportNumber())
print('')
print("Flight Details:")
print("Flight Number:", boarding_pass.getFlight().getFlightNumber(), ", Departure Location:",
      boarding_pass.getFlight().getDepartureLocation(), ", Destination:", boarding_pass.getFlight().getDestination(),
      ", Take-off Time:", boarding_pass.getFlight().getTakeOffTime(), ",Arrival Time:",
      boarding_pass.getFlight().getArrivalTime())
print('')
print("Airline Staff Details:")
print("Staff member Name:", airport_staff.getStaffFirstName(), airport_staff.getStaffLastName(), ", Staff ID:",
      airport_staff.getStaffID(), ", Staff Role:", airport_staff.getStaffRole(), ", Gender:",
      airport_staff.getGender().name)
print('')
print("Boarding Pass Details:")
print("Passenger Name:", boarding_pass.getPassenger().getFirstName(), boarding_pass.getPassenger().getLastName())
print("Flight Number:", boarding_pass.getFlight().getFlightNumber())
print("Departure Location:", boarding_pass.getFlight().getDepartureLocation())
print("Destination:", boarding_pass.getFlight().getDestination())
print("Terminal:", boarding_pass.getFlight().getTerminal())
print("Take-off Time:", boarding_pass.getFlight().getTakeOffTime())
print("Arrival Time:", boarding_pass.getFlight().getArrivalTime())
print("Seat:", boarding_pass.getSeat())
print("Boarding Time:", boarding_pass.getBoardingTime())
print("Class:", boarding_pass.getClass())
print("Electronic Ticket Number:", boarding_pass.getElectronicTicketNum())
print("")
print("Luggage details")
print("Passenger Bag: ", luggage.get_passenger_name())
print("Bag Weight : ", luggage.get_weight())
print("Bag destinetion : ", luggage.get_destination())
print("Bag checked:", luggage.get_is_checked())
print("")
print("Security Staff details")
print("Security Staff Name : ", securityStaff.getEmployeeName())
print("Security Staff ID:", securityStaff.getEmployeeID())