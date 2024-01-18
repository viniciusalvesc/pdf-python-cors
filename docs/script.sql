"""
Nome do arquivo: script.sql
Autor: Vinicius Alves Campello
Data de desenvolvimento: 11/01/2024
Descrição: Arquivo para armazenar comandos feitos no banco de dados mariaDB.
"""
/* Criação de tabelas com os relacionamentos */

CREATE TABLE ft_user (
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

CREATE UNIQUE INDEX ft_user_email_index USING BTREE ON fytax_dev_flask.ft_user (email);


CREATE TABLE ft_user_info (
    id VARCHAR(36) PRIMARY KEY NOT NULL,
    user_id VARCHAR(255) DEFAULT NULL,
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
    FOREIGN KEY (user_id) REFERENCES ft_user(id) ON DELETE SET NULL
);


CREATE TABLE ft_user_address (
    id VARCHAR(36) PRIMARY KEY NOT NULL,
    user_id VARCHAR(255),
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
    FOREIGN KEY (user_id) REFERENCES ft_user(id) ON DELETE SET NULL
);

CREATE TABLE ft_processed_item (
    id VARCHAR(36) PRIMARY KEY NOT NULL,
    external_id VARCHAR(255),
    company_cnpj VARCHAR(255),
    user_id VARCHAR(255),
    status enum('success','fail','processing','pending') NOT NULL DEFAULT 'pending',
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    deleted_at DATETIME(6),
    FOREIGN KEY (user_id) REFERENCES ft_user(id) ON DELETE SET NULL
);

CREATE TABLE ft_payment_method (
    id VARCHAR(36) PRIMARY KEY NOT NULL,
    user_id VARCHAR(255),
    name VARCHAR(255),
    card_number VARCHAR(255),
	expiration_date TIMESTAMP DEFAULT NULL,
	cvv VARCHAR(255),
    status ENUM('inactive', 'active') NOT NULL DEFAULT 'inactive',
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    deleted_at DATETIME(6),
    FOREIGN KEY (user_id) REFERENCES ft_user(id)
);

CREATE TABLE ft_payment_address (
    id VARCHAR(36) PRIMARY KEY NOT NULL,
    user_id VARCHAR(255),
    zip_code VARCHAR(255),
    country VARCHAR(255),
    state VARCHAR(255),
    city VARCHAR(255),
    neighborhood VARCHAR(255),
    street VARCHAR(255),
    `number` VARCHAR(255),
    complement VARCHAR(255),
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    deleted_at DATETIME(6),
    FOREIGN KEY (user_id) REFERENCES ft_user(id)
);

CREATE TABLE ft_subscription (
    id VARCHAR(36) PRIMARY KEY NOT NULL,
    user_id VARCHAR(255),
    product_id VARCHAR(255),
    payment_history_id VARCHAR(255),
    start_date TIMESTAMP DEFAULT NULL,
    end_date TIMESTAMP DEFAULT NULL,
    status enum('active','fail','inactive','pending') NOT NULL DEFAULT 'pending',
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    deleted_at DATETIME(6),
    FOREIGN KEY (user_id) REFERENCES ft_user(id)
);

CREATE TABLE ft_payment_history (
    id VARCHAR(36) PRIMARY KEY NOT NULL,
    user_id VARCHAR(255),
    payment_method_id VARCHAR(255),
    payment_address_id VARCHAR(255),
    price DECIMAL(10,0) DEFAULT NULL,
    coupon_id VARCHAR(255),
    discount DECIMAL(10,0) DEFAULT NULL,
    total_paid DECIMAL(10,0) DEFAULT NULL,
    installments INT(11) DEFAULT 1,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    deleted_at DATETIME(6),
    FOREIGN KEY (user_id) REFERENCES ft_user(id),
    FOREIGN KEY (payment_method_id) REFERENCES ft_payment_method(id),
    FOREIGN KEY (payment_address_id) REFERENCES ft_payment_address(id)
);
