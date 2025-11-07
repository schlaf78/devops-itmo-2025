CREATE TABLE "TransactionDetails".transactiontypes
(
	transactiontypesid int GENERATED ALWAYS AS IDENTITY NOT NULL,
	transactiondescription varchar(30) NOT NULL,
	credittype boolean NOT NULL
)