CREATE UNIQUE INDEX ix_transactiontypes
	ON "TransactionDetails".transactiontypes
	USING btree
	(transactiontypesid ASC);

ALTER TABLE IF EXISTS "TransactionDetails".transactiontypes
	CLUSTER ON ix_transactiontypes;

CREATE INDEX ix_transactions_ttypes
	ON "TransactionDetails".transactions
	USING btree
	(TransactionType ASC);

