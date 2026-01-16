CREATE DATABASE IF NOT EXISTS car_theft_db; 
USE car_theft_db; 

CREATE TABLE IF NOT EXISTS stolen_reports (
    brand VARCHAR(100) NOT NULL,
    model VARCHAR(100), 
    date_reported DATE 
); 


