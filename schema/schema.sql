DROP TABLE IF EXISTS users;

CREATE TABLE "users" (
	"username"		TEXT UNIQUE,
	"password"		TEXT,
	"first_name"	TEXT,
	"last_name"		TEXT,
	"email_address"	TEXT,
	PRIMARY KEY("username")
);

INSERT INTO users (username, password, first_name, last_name, email_address)
    VALUES (?, ?, ?, ?, ?), ('12345', 'Password', 'Ryan', 'Hawcroft', '12345@email.com');

