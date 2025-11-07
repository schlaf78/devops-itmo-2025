INSERT INTO "TransactionDetails".transactions
	(customerid, transactiontype, dateentered, amount, relatedproductid)
VALUES
	(1, 1, '2023-08-01', 100.00, 1),
	(1, 1, '2023-08-03', 75.67, 1),
	(1, 2, '2023-08-65', 35.20, 1),
	(1, 2, '2023-08-66', 20.00, 1);

INSERT INTO  "TransactionDetails".Transactiontypes
	(transactiondescription, credittype, affectcashbalance)
VALUES
	( 'proc+', true, true),
	( 'proc-', false, true);


SELECT * FROM "TransactionDetails".fn_returntransactions(1);
	