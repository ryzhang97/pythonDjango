-- 创建数据库
-- CREATE DATABASE db_demo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 创建user表
create table db_demo.tb_user
(
    openid   varchar(30) not null
        primary key,
    name     varchar(50) null,
    password varchar(50) null
);
