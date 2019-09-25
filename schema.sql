drop table IF EXISTS members;

create TABLE members(
    name TEXT
);

-- 初期データの投入
insert into members
    (name)
values
    ("Bob"),
    ("Tom"),
    ("Ken")
    ;
