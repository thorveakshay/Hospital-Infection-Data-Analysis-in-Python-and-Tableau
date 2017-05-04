# Hospital-Infection-Data-Analysis-in-Python-and-Tableau
Hospital-Infection-Data-Analysis-in-Python-and-Tableau

Table creation query

CREATE TABLE `processed_infection_data` (
  `infection_id` int(11) NOT NULL,
  `hospital_name` text,
  `measure_id` text,
  `score` double DEFAULT NULL,
  `infection_name` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
