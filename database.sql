CREATE TABLE "so"(
"id" SERIAL,
"release" VARCHAR(100),
"nodename" VARCHAR(100),
"kernelv" VARCHAR(100),
"machine" VARCHAR(100),
"processor" VARCHAR(100),
"os" VARCHAR(100),
"hardware" VARCHAR(100)
);

INSERT INTO "so" VALUES 
(1,'release','node','ibm','200mb','x64','ms-dos','old');

