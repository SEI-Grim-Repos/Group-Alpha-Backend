CREATE DATABASE food;

CREATE USER group_alpha_backend_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE food TO group_alpha_backend_admin;

-- to run the .sql file (in the terminal in the virtual env type)
    -- psql -f create-database.sql