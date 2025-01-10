-- 创建数据库
-- CREATE DATABASE db_app CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# -- -- 创建user表
create table db_app.tb_user
(
    id int auto_increment
        primary key,
    openid   varchar(30) null UNIQUE,
    username varchar(10) null UNIQUE,
    password varchar(15) null,
    name     varchar(50) null,
    last_login datetime null,
    index  unique_index_openid (openid),
    index  unique_index_username (username)
);
# -- -- 删除user表
# drop table tb_user;
