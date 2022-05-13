DROP DATABASE IF EXISTS blogly_db;

CREATE DATABASE blogly_db;

\c blogly_db

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    image_url TEXT
);

-- INSERT INTO users (first_name, last_name)
-- VALUES 
-- ('Erik', 'Higgins'),
-- ('Antonio', 'Flowers'),
-- ('Clifford', 'Krueger'),
-- ('Joel', 'Holden'),
-- ('Javier', 'Larsen'),
-- ('Rafael', 'Orr');

-- SELECT * FROM users;