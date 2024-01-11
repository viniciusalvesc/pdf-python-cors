"""
Nome do arquivo: script.sql
Autor: Vinicius Alves Campello
Data de desenvolvimento: 11/01/2024
Descrição: Arquivo para armazenar comandos feitos no banco de dados mariaDB.
"""
/* Criação de tabelas com os relacionamentos */

CREATE TABLE users (
    id VARCHAR(36) PRIMARY KEY NOT NULL,
    role ENUM('admin', 'manager', 'user', 'guest') NOT NULL DEFAULT 'guest',
    email VARCHAR(255) UNIQUE DEFAULT NULL,
    password VARCHAR(255) DEFAULT NULL,
    status ENUM('inactive', 'active') NOT NULL DEFAULT 'inactive',
    created_location VARCHAR(255) DEFAULT NULL,
    created_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    deleted_at TIMESTAMP(6) NULL
);


CREATE TABLE user_info (
    id VARCHAR(36) PRIMARY KEY NOT NULL,
    user_id VARCHAR(255) UNIQUE DEFAULT NULL,
    first_name VARCHAR(255) DEFAULT NULL,
    last_name VARCHAR(255) DEFAULT NULL,
    cpf VARCHAR(255) DEFAULT NULL,
    birthdate TIMESTAMP DEFAULT NULL,
    gender enum('male','woman','other','not_specified') NOT NULL DEFAULT 'not_specified',
    phone_number VARCHAR(255) DEFAULT NULL,
    user_avatar_url VARCHAR(255) DEFAULT NULL,
    created_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    deleted_at TIMESTAMP(6) NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL ON UPDATE CASCADE
);


CREATE TABLE user_address (
    id VARCHAR(36) PRIMARY KEY NOT NULL,
    user_id VARCHAR(255) UNIQUE,
    zipcode VARCHAR(255),
    country VARCHAR(255),
    state VARCHAR(255),
    city VARCHAR(255),
    neighborhood VARCHAR(255),
    street VARCHAR(255),
    number VARCHAR(255),
    complement VARCHAR(255),
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    deleted_at DATETIME(6),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL ON UPDATE CASCADE
);