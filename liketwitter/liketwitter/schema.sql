drop table if exists user;
create table user (
	user_id integer primary key autoincrement,
	username text not null,
	password text not null
);

drop table if exists follower;
create table follower(
	follower_id integer,
	following_id integer
);

drop table if exists message;
create table message (
	message_id integer primary key autoincrement,
	author_id integer not null,
	author_username text not null,
	text text not null,
	publish_date integer
);
