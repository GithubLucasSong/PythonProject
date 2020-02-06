/*
2，建立教师表
teacher(Tid,Tname)
--Tid 教师编号,Tname 教师姓名
插入一些测试数据，并查询出有多少姓李的老师
*/

CREATE DATABASE live04hw CHARSET=utf8;

USE live04hw;

CREATE TABLE t_teacher(
Tid INT,
Tname VARCHAR(32)
);

INSERT INTO t_teacher VALUES(1,'张三');
INSERT INTO t_teacher VALUES(2,'李四');
INSERT INTO t_teacher VALUES(3,'赵五');
INSERT INTO t_teacher VALUES(4,'王六');
INSERT INTO t_teacher VALUES(5,'李七');

SELECT * FROM t_teacher WHERE Tname LIKE '李%'


/*
3，建立学员成绩表：
表中包含学生id，姓名，所属班级，最近一次考试的成绩
插入测试数据
查询出成绩在60到80之间都有谁
查询成绩为85，86或88的都有谁
查询“py28”班的学生人数
查询成绩最高的学生id和姓名
*/

CREATE TABLE t_score
(id INT PRIMARY KEY,
NAME VARCHAR(32),
class VARCHAR(32),
score INT);

INSERT INTO t_score VALUES(01,'alex','py27',56);
INSERT INTO t_score VALUES(02,'blex','py27',60);
INSERT INTO t_score VALUES(03,'clex','py27',64);
INSERT INTO t_score VALUES(04,'dlex','py27',68);
INSERT INTO t_score VALUES(05,'elex','py27',72);
INSERT INTO t_score VALUES(06,'flex','py28',76);
INSERT INTO t_score VALUES(07,'glex','py28',80);
INSERT INTO t_score VALUES(08,'hlex','py28',84);
INSERT INTO t_score VALUES(09,'ilex','py28',88);
INSERT INTO t_score VALUES(10,'jlex','py28',92);

SELECT NAME FROM t_score WHERE 60<=score<=80;

SELECT NAME FROM t_score WHERE score=85 OR score=86 OR score=88

SELECT COUNT(id) FROM t_score WHERE class='py28';

SELECT NAME,id FROM t_score WHERE score=(SELECT MAX(score) FROM t_score);






