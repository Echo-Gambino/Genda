
CREATE TABLE TODOLIST(
	Hash 			CHAR(32) 	PRIMARY KEY	NOT NULL,
	DateModified 	DATE 					NOT NULL,
	Data   			TEXT,
	Important		INT 					NOT NULL
);

