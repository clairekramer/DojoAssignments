USE lead_gen_business;
SELECT * FROM clients;
INSERT INTO clients (first_name, last_name, email, joined_datetime) VALUES('Claire', 'Kramer', 'kramerclaire@me.com', NOW());
DELETE FROM clients WHERE id = 11;
UPDATE clients SET first_name = 'Thomas' WHERE id = 9;