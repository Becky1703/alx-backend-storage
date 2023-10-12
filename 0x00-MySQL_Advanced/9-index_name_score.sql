-- Script creates an index name on the table names with the first letter of the name and the score
CREATE INDEX idx_name_first_score ON names(name(1), score);
