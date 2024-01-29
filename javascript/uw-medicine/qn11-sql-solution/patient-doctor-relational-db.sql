-- 
-- filename: temp.sql
-- by: Abhay Gupta
--
-- desc:
-- 1. How many sql tables do you need to store doctor/patient data?
-- 2. Write the SQL statements to create the tables and describe what would be stored in each table


-- doctor table
-- the data stores the following doctors' data: 
-- - unique ID, first name, last name, practice address
CREATE TABLE Doctors {
    DoctorId int,
    FirstName varchar(20) NOT NULL,
    LastName varchar(20) NOT NULL,
    PracticeAddress varchar(255)
}

-- patient table
-- the data stores the following patients' data: 
-- - unique ID, first name, last name, gender, age
CREATE TABLE Patients {
    PatientId int, 
    FirstName varchar(20) NOT NULL,
    LastName varchar(20) NOT NULL,
    Gender varchar(1) NOT NULL, 
    Age int
}

-- junction table
-- models the relationship between doctors and patients
-- the id's and the patient/doctor, their corresponding relevent row, and the parent-child relationship via foreign key
CREATE TABLE DoctorPatient {
    DoctorId int,
    PatientId int, 
    PRIMARY KEY (DoctorId, PatientId),
    FOREIGN KEY (DoctorId) REFERENCES Doctors(DoctorId),
    FOREIGN KEY (PatientId) REFERENCES Patients(PatientId),
}