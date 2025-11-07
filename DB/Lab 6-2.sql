CREATE OR REPLACE FUNCTION "TransactionDetails".fn_returntransactions (
	CustID bigint)
RETURNS TABLE (
	transactionid bigint,
	customerid bigint,
	transactiondescription varchar(30),
	dateentered timestamp(0),
	amount money)
SECURITY INVOKER
AS $$
SELECT
	t.transactionid as transactionid,
	t.customerid as customerid,
	tt.transactiondescription as transactiondescription,
	t.dateentered as dateentered,
	t.amount as amount
FROM "TransactionDetails".transactions t
JOIN "TransactionDetails".transactiontypes tt
	ON tt.transactiontypesid = t.transaction_type
WHERE t.customerid = CustID;
$$ LANGUAGE sql;



SELECT * FROM "TransactionDetails".transactions t;
--SELECT * FROM  "TransactionDetails".transactiontypes tt;

ALTER TABLE TransactionDetails 