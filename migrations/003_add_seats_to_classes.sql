-- Add a number of seats to the class schedule to only allow a certain number of registrations
ALTER TABLE class_schedule ADD number_seats INTEGER NOT NULL; 