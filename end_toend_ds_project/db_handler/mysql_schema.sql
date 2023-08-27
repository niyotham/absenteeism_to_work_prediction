-- USE predicted_outputs;
-- DROP TABLE IF EXISTS predicted_outputs;
CREATE TABLE  predicted_outputs(
reason_1 BOOLEAN NOT NULL,
reason_2 BOOLEAN NOT NULL,
reason_3 BOOLEAN NOT NULL,
reason_4 BOOLEAN NOT NULL,
month_value INTEGER NOT NULL,
transportation_expense INTEGER NOT NULL,
age INTEGER NOT NULL,
body_mass_index INT NOT NULL,
education INTEGER NOT NULL,
children INTEGER NOT NULL,
pet	 BOOLEAN NOT NULL,
probability	 FLOAT NOT NULL,
prediction BOOLEAN NOT NULL
);