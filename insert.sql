use demo;

insert into assignee values(1, 'Fujino', 'Intern');
insert into assignee values(2, 'MacBook', 'pc');
insert into assignee values(3, 'Dog', 'walk');



insert into todo values(1, 'cleaning', '2022-05-21 01:30:00', false, now(), now(), now());
insert into todo values(2, 'create PR', '2022-04-01 08:30:00', false, now(), now(), now());


insert into todo_assignee values(1,2,1);
