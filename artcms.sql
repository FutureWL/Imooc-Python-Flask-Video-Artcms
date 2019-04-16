/*
用户表
1.编号
2.账号
3.密码
4.注册时间
*/

create table if not exists user
(
    id      int unsigned not null auto_increment key comment '主键ID',
    name    varchar(20)  not null comment '账号',
    pwd     varchar(100) not null comment '密码',
    addtime datetime     not null comment '注册时间'
) engine = InnoDB
  default charset = utf8 comment '会员';

/*
文章表
1.编号
2.标题
3.分类
4.作者
5.封面
6.内容
7.发布时间
*/
create table if not exists art
(
    id      int unsigned     not null auto_increment key comment '主键ID',
    title   varchar(100)     not null comment '标题',
    cate    tinyint unsigned not null comment '分类',
    user_id int unsigned     not null comment '作者',
    logo    varchar(100)     not null comment '封面',
    content mediumtext       not null comment '文章',
    addtime datetime         not null comment '发布时间'
) engine = InnoDB
  default charset = utf8 comment '文章';