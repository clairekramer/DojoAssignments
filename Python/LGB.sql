-- Question 1 
SELECT MONTHNAME(charged_datetime) as Month, SUM(amount) as revenue FROM billing
WHERE MONTH(charged_datetime) = 3 AND YEAR(charged_datetime) = 2012;
-- Question 2 
SELECT CONCAT(clients.first_name,' ', clients.last_name) as client, SUM(amount) as revenue
FROM clients
JOIN billing ON clients.client_id = billing.client_id
WHERE clients.client_id = 2;
-- Question 3 
SELECT client_id, domain_name as website
FROM sites
WHERE client_id = 10;
-- Question 4
SELECT client_id, COUNT(site_id) AS num_sites, MONTHNAME(sites.created_datetime) as month_created, YEAR(sites.created_datetime) as year_created
FROM sites
WHERE client_id = 1
GROUP BY MONTH(created_datetime), year(created_datetime);
-- Question 5
SELECT COUNT(leads.leads_id) as num_of_leads, sites.domain_name as website, DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') AS date_registered
FROM sites
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-02-15'
GROUP BY sites.site_id;
-- Question 6
SELECT CONCAT(clients.first_name, ' ', clients.last_name) as client_name, COUNT(leads.leads_id) as num_of_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.leads_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY clients.client_id;
-- Question 7
SELECT CONCAT(clients.first_name, ' ', clients.last_name) as client_name, COUNT(leads.leads_id) as num_of_leads, MONTHNAME(leads.registered_datetime) AS month_registered
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.leads_id
WHERE MONTH(leads.registered_datetime) BETWEEN 1 AND 6
AND YEAR(leads.registered_datetime) = 2011
GROUP BY clients.client_id, MONTH(leads.registered_datetime)
ORDER BY MONTH(leads.registered_datetime);
-- Question 8 
SELECT CONCAT(clients.first_name, ' ', clients.last_name) as client_name, sites.domain_name as website, COUNT(leads.leads_id) as num_of_leads, DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') AS date_registered
FROM clients
JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.leads_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY sites.domain_name
ORDER BY clients.client_id;
-- Question 9 
SELECT CONCAT(clients.first_name, ' ', clients.last_name) as client_name, SUM(billing.amount) as Revenue, MONTHNAME(charged_datetime) as Month_charged, YEAR(billing.charged_datetime) as year_charged
FROM clients 
LEFT JOIN billing ON clients.client_id = billing.client_id
GROUP BY client_name, MONTH(billing.charged_datetime), YEAR(billing.charged_datetime)
ORDER BY clients.client_id;
-- Question 10
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, GROUP_CONCAT(sites.domain_name) as website
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
GROUP BY clients.client_id;
