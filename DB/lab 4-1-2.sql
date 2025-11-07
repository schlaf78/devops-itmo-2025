CREATE TABLE "TransactionDetails".transactions (
	transaction bigint GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1)
					    PRIMARY KEY NOT NULL,
	customerid bigint NOT NULL,
	transactiontype int NOT NULL,
	dateentered timestamp(0) NOT NULL,
	amount numeric(18,5) NOT NULL,
	notes varchar NULL,
	relatedshareid bigint NULL,
	relatedproductid bigint NOT NULL);