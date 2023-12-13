create table carUid (
	car_uuid UUID NOT NULL PRIMARY KEY,
	make VARCHAR(50) NOT NULL,
	model VARCHAR(50) NOT NULL,
	price VARCHAR(50) NOT NULL
);

create table personUid (
	person_uuid UUID NOT NULL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(150) NOT NULL,
	gender VARCHAR(7) NOT NULL,
	born DATE NOT NULL,
	country VARCHAR(50),
    car_uuid UUID REFERENCES carUid (car_uuid),
    UNIQUE(car_uuid)
);

insert into personUid (person_uuid,first_name, last_name, email, gender, born, country) values (uuid_generate_v4(),'Eublan','Mata','eublanmata@gmail.com','Male','1992-04-07','Venezuela');
insert into personUid (person_uuid,first_name, last_name, email, gender, born, country) values (uuid_generate_v4(),'Alberto','Mata','albertomata@gmail.com','Male','2003-10-27','Venezuela');
insert into personUid (person_uuid,first_name, last_name, email, gender, born, country) values (uuid_generate_v4(),'Stalin','Milano','stalinmilano@gmail.com','Male','1996-09-03','Venezuela');
insert into personUid (person_uuid,first_name, last_name, email, gender, born, country) values (uuid_generate_v4(),'Andrea','Medina','andreamedina@hotmail.com','Male','2005-14-12','Venezuela');
insert into carUid (car_uuid,make,model,price) values (uuid_generate_v4(),'ForRapto','FORD','23456');
insert into carUid (car_uuid,make,model,price) values (uuid_generate_v4(),'Tundra','TOYOTA','80000');
insert into carUid (car_uuid,make,model,price) values (uuid_generate_v4(),'G65','MUSTANG','30000');
insert into carUid (car_uuid,make,model,price) values (uuid_generate_v4(),'Z-4','Ferrari','150000');