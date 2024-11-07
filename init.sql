CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(50) UNIQUE
);

INSERT INTO users (
    username,
    password,
    email,
    brl_balance
)
VALUES (
    'user1',
    '$2b$12$Gict2l84OArIydY3znRJ1O1KpCDYLb.cjzf8QduCmGANt8RoS6xdm',
    'user1@test.com',
    1000.00
);
