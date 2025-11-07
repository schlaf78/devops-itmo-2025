

--ALTER TABLE "CustomerDetails".customers
--ALTER COLUMN customerid
--DROP IDENTITY;

--UPDATE "CustomerDetails".customers
--set customerid = 1;

--SELECT * FROM "CustomerDetails".customers;

--ALTER TABLE "CustomerDetails".customers
--ALTER COLUMN customerid
--ADD GENERATED ALWAYS AS IDENTITY;

INSERT INTO "CustomerDetails".customers
(customertitleid, customerlastname, customerfirstname,
customerotherinitials, addressid, accountnumber,
accounttypeid, clearebalance, unclearebalance)
VALUES
(1, 'Brust', 'Andrew', 'J.', 133, 18176111, 1, 200.00, 2.00),
(3, 'Lobel', 'Leonard', NULL, 145, 53431993, 1, 437.97, -19.56);