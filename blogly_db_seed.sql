DROP DATABASE IF EXISTS blogly_db;

CREATE DATABASE blogly_db;

\c blogly_db

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    image_url TEXT
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    post_title TEXT NOT NULL,
    post_content TEXT NOT NULL,
    created_at TEXT,
    user_id INTEGER REFERENCES users (id) ON DELETE CASCADE
);

-- CREATE TABLE tags (
--     id SERIAL PRIMARY KEY,
--     tag_name TEXT UNIQUE NOT NULL
-- );

-- CREATE TABLE post_tag (
--   post_id INTEGER REFERENCES posts (id) ON DELETE CASCADE,
--   tag_id INTEGER REFERENCES tags (id) ON DELETE CASCADE,
--   PRIMARY KEY (post_id, tag_id)
-- );

-- INSERT INTO tags (tag_name)
-- VALUES 
-- ('Fun'),
-- ('True'),
-- ('Interesting'),
-- ('WTF'),
-- ('LOL');


INSERT INTO users (first_name, last_name, image_url)
VALUES 
('Erik', 'Higgins', 'http://michaeljmurphy.com/Michael_J_Murphy.jpg'),
('Antonio', 'Flowers', 'http://michaeljmurphy.com/Michael_J_Murphy.jpg'),
('Clifford', 'Krueger', 'http://michaeljmurphy.com/Michael_J_Murphy.jpg'),
('Joel', 'Holden', 'http://michaeljmurphy.com/Michael_J_Murphy.jpg'),
('Javier', 'Larsen', 'http://michaeljmurphy.com/Michael_J_Murphy.jpg'),
('Rafael', 'Orr', 'http://michaeljmurphy.com/Michael_J_Murphy.jpg');


INSERT INTO posts (post_title, post_content, created_at, user_id)
VALUES 
('Bacon ipsum dolor amet beef.', 'hock turducken brisket Frankfurter pork.', '2022-05-16 12:32:49', 1),
('ball tip drumstick ham ham.', 't-bone kielbasa cow sirloin leberkas.', '2022-05-16 12:32:49', 2),
('hock turducken brisket Frankfurter pork.', 'venison beef swine bresaola tri-tip.', '2022-05-16 12:32:49', 3),
('t-bone kielbasa cow sirloin leberkas.', 'pastrami drumstick corned beef Drumstick.', '2022-05-16 12:32:49', 4),
('venison beef swine bresaola tri-tip.', 'turducken pork chop chicken bacon.', '2022-05-16 12:32:49', 5),
('pastrami drumstick corned beef Drumstick.', 'Jowl cow tri-tip meatloaf beef.', '2022-05-16 12:32:49', 6),
('turducken pork chop chicken bacon.', 'hamburger prosciutto Venison leberkas ground.', '2022-05-16 12:32:49', 1),
('Jowl cow tri-tip meatloaf beef.', 'round hamburger chicken meatloaf sirloin.', '2022-05-16 12:32:49', 2),
('hamburger prosciutto Venison leberkas ground.', 'short ribs rump Kielbasa corned.', '2022-05-16 12:32:49', 3),
('round hamburger chicken meatloaf sirloin.', 'beef porchetta sirloin tail pork.', '2022-05-16 12:32:49', 4),
('short ribs rump Kielbasa corned.', 'loin Pork belly buffalo ham.', '2022-05-16 12:32:49', 5),
('beef porchetta sirloin tail pork.', 'hock tenderloin flank ribeye kevin.', '2022-05-16 12:32:49', 6),
('loin Pork belly buffalo ham.', 'porchetta meatloaf.', '2022-05-16 12:32:49', 1),
('hock tenderloin flank ribeye kevin.', 'Bacon ipsum dolor amet beef.', '2022-05-16 12:32:49', 2),
('porchetta meatloaf.', 'ball tip drumstick ham ham.', '2022-05-16 12:32:49', 3),
('Bacon ipsum dolor amet beef.', 'hock turducken brisket Frankfurter pork.', '2022-05-16 12:32:49', 4),
('ball tip drumstick ham ham.', 't-bone kielbasa cow sirloin leberkas.', '2022-05-16 12:32:49', 5),
('hock turducken brisket Frankfurter pork.', 'venison beef swine bresaola tri-tip.', '2022-05-16 12:32:49', 6),
('t-bone kielbasa cow sirloin leberkas.', 'pastrami drumstick corned beef Drumstick.', '2022-05-16 12:32:49', 1),
('venison beef swine bresaola tri-tip.', 'turducken pork chop chicken bacon.', '2022-05-16 12:32:49', 2),
('pastrami drumstick corned beef Drumstick.', 'Jowl cow tri-tip meatloaf beef.', '2022-05-16 12:32:49', 3),
('turducken pork chop chicken bacon.', 'hamburger prosciutto Venison leberkas ground.', '2022-05-16 12:32:49', 4),
('Jowl cow tri-tip meatloaf beef.', 'round hamburger chicken meatloaf sirloin.', '2022-05-16 12:32:49', 5),
('hamburger prosciutto Venison leberkas ground.', 'short ribs rump Kielbasa corned.', '2022-05-16 12:32:49', 6),
('round hamburger chicken meatloaf sirloin.', 'beef porchetta sirloin tail pork.', '2022-05-16 12:32:49', 1),
('short ribs rump Kielbasa corned.', 'loin Pork belly buffalo ham.', '2022-05-16 12:32:49', 2),
('beef porchetta sirloin tail pork.', 'hock tenderloin flank ribeye kevin.', '2022-05-16 12:32:49', 3),
('loin Pork belly buffalo ham.', 'porchetta meatloaf.', '2022-05-16 12:32:49', 4),
('hock tenderloin flank ribeye kevin.', 'Bacon ipsum dolor amet beef.', '2022-05-16 12:32:49', 5),
('porchetta meatloaf.', 'ball tip drumstick ham ham.', '2022-05-16 12:32:49', 6);



-- SELECT * FROM users;

