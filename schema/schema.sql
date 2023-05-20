---------------------------------------------------- USERS TABLE --------------------------------------------------
DROP TABLE IF EXISTS users;

CREATE TABLE "users" (
	"username"	TEXT UNIQUE,
	"password"	TEXT,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"email_address"	TEXT,
	"user_type"	INTEGER,
	PRIMARY KEY("username")
);

INSERT INTO users (username, password, first_name, last_name, email_address, user_type)
    VALUES (?, ?, ?, ?, ?, ?), ('12345', 'Password', 'Ryan', 'Hawcroft', '12345@email.com', 1);

INSERT INTO users (username, password, first_name, last_name, email_address, user_type)
    VALUES (?, ?, ?, ?, ?, ?), ('22345', 'Password', 'Connor', 'Lowe', '22345@email.com', 2);

INSERT INTO users (username, password, first_name, last_name, email_address, user_type)
    VALUES (?, ?, ?, ?, ?, ?), ('32345', 'Password', 'Lucas', 'Nguyen', '32345@email.com', 3);

INSERT INTO users (username, password, first_name, last_name, email_address, user_type)
    VALUES (?, ?, ?, ?, ?, ?), ('42345', 'Password', 'Anthony', 'Jones', '42345@email.com', 2);

INSERT INTO users (username, password, first_name, last_name, email_address, user_type)
    VALUES (?, ?, ?, ?, ?, ?), ('52345', 'Password', 'Greg', 'Pearson', '52345@email.com', 1);

INSERT INTO users (username, password, first_name, last_name, email_address, user_type)
    VALUES (?, ?, ?, ?, ?, ?), ('62345', 'Password', 'Liz', 'Carr', '62345@email.com', 3);


---------------------------------------------------- FRIENDS TABLE --------------------------------------------------
DROP TABLE IF EXISTS friends;

CREATE TABLE "friends" (
	"username"	TEXT,
	"friend_username"	TEXT
);

-- 12345
INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('12345', '22345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('12345', '32345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('12345', '42345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('12345', '52345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('12345', '62345');

-- 22345
INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('22345', '12345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('22345', '32345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('22345', '62345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('22345', '52345');

-- 32345
INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('32345', '12345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('32345', '22345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('32345', '62345');

-- 42345
INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('42345', '12345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('42345', '22345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('42345', '32345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('42345', '52345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('42345', '62345');

-- 52345
INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('52345', '12345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('52345', '22345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('52345', '32345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('52345', '42345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('52345', '62345');


-- 62345
INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('62345', '12345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('62345', '22345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('62345', '32345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('62345', '42345');

INSERT INTO friends (username, friend_username)
    VALUES (?, ?), ('62345', '52345');

----------------------------------------------------  TABLE --------------------------------------------------