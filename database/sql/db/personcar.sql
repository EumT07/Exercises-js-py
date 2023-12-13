create table car (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	make VARCHAR(50) NOT NULL,
	model VARCHAR(50) NOT NULL,
	price VARCHAR(50) NOT NULL
);

create table person (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(150) NOT NULL,
	gender VARCHAR(7) NOT NULL,
	born DATE NOT NULL,
	country VARCHAR(50),
    car_id BIGINT REFERENCES car (id),
    UNIQUE(car_id)
);

insert into person (first_name, last_name, email, gender, born, country) values ('Eublan','Mata','eublanmata@gmail.com','Male','1992-04-07','Venezuela');
insert into person (first_name, last_name, email, gender, born, country) values ('Alberto','Mata','albertomata@gmail.com','Male','2003-10-27','Venezuela');
insert into person (first_name, last_name, email, gender, born, country) values ('Stalin','Milano','stalinmilano@gmail.com','Male','1996-09-03','Venezuela');
insert into person (first_name, last_name, email, gender, born, country) values ('Andrea','Medina','andreamedina@hotmail.com','Male','2005-14-12','Venezuela');
insert into car (make,model,price) values ('ForRapto','FORD','23456');
insert into car (make,model,price) values ('Tundra','TOYOTA','80000');
insert into car (make,model,price) values ('G65','MUSTANG','30000');
insert into car (make,model,price) values ('Z-4','Ferrari','150000');