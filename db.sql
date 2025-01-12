-- 创建数据库
# CREATE DATABASE db_app;

use db_app;
CREATE TABLE tb_employee
(
    employeeid INT AUTO_INCREMENT PRIMARY KEY COMMENT '员工唯一标识符',
    name       VARCHAR(100) NOT NULL COMMENT '员工姓名',
    department VARCHAR(100) NOT NULL COMMENT '员工所属部门',
    job_title  VARCHAR(100) NOT NULL COMMENT '员工职位',
    hire_date  DATE         NOT NULL COMMENT '员工入职日期'
) COMMENT ='存储员工信息的表';


CREATE TABLE tb_user
(
    userid      INT AUTO_INCREMENT PRIMARY KEY COMMENT '用户唯一标识符',
    username    VARCHAR(50) UNIQUE NOT NULL COMMENT '用户名，必须唯一',
    password    VARCHAR(255)       NOT NULL COMMENT '用户密码，存储哈希值',
    email       VARCHAR(100) UNIQUE COMMENT '用户电子邮箱，必须唯一',
    mobile      VARCHAR(20) UNIQUE COMMENT '用户电话号码，必须唯一',
    employeeid  INT COMMENT '员工ID，外键引用tb_employee表，可为空',
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',
    last_login  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录最后更新时间',
    is_verified BOOLEAN   DEFAULT FALSE COMMENT '用户是否已验证邮箱或手机号',
    app_bound   BOOLEAN   DEFAULT FALSE COMMENT '用户是否已绑定到某个应用',
    FOREIGN KEY (employeeid) REFERENCES tb_employee (employeeid) ON DELETE SET NULL
) COMMENT ='存储用户信息的表';


CREATE TABLE tb_wx_user
(
    openid     VARCHAR(50) NOT NULL PRIMARY KEY UNIQUE COMMENT '小程序用户的openid，必须唯一',
    unionid    VARCHAR(50) UNIQUE COMMENT '小程序用户的unionid，必须唯一',
    userid     INT COMMENT '用户ID，外键引用tb_user表',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',
    FOREIGN KEY (userid) REFERENCES tb_user (userid) ON DELETE CASCADE
) COMMENT ='存储小程序用户信息的表，与tb_user表建立关联';

-- （可选）创建绑定关系 redis
# userid  app_token
