-- 
-- by Abhay Gupta
--
-- Description: qn 12 - In the above schema that you created, write the SQL query to find all the patients where their last name starts with "s" and has an age greater or equal to 18 and less than or equal to 99 who are being taken care of by doctors with the name of "Rob Johnston"? 
------


-- steps:
-- query for patient 
-- join patient table w/ doctorpatient table; join doctor table 
-- filter patient, set age and name criteria
SELECT p.FirstName, p.LastName
FROM Patient p
INNER JOIN DoctorPatient dp ON p.PatientId = dp.PatientId
INNER JOIN Doctor d ON dp.DoctorId = d.DoctorId
WHERE p.LastName LIKE 's%'
AND p.Age >= 18 AND p.Age <= 99
AND d.FirstName = 'Rob' AND d.LastName = 'Johnston';