CREATE PROCEDURE "CustomerDetails".spu_inscustomer(
	FirstName varchar(50),
	LastName varchar(50),
	CustTitle int,
	CustInitials varchar(10),
	AddressId int,
	AccountNumber varchar(15),
	AccountTypeId int
)
LANGUAGE plpgsql
AS $$
BEGIN
	INSERT INTO "CustomerDetails".customers (
		customertitleid,
		customerfirstname,
		customerotherinitials,
		customerlastname,
		addressid,
		accountnumber,
		accounttypeid,
		clearebalance,
		unclearebalance)
	VALUES (
		custtitle,
		firstname,
		custinitials,
		lastname,
		addressid,
		accountnumber,
		accounttypeid,
		0,
		0);
END
$$