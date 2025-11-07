DELETE FROM "CustomerDetails".customers
WHERE customerid - 5;

ALTER TABLE "CustomerDetailes".customers
ALTER COLUMN customerfirstname TYPE character varying(50);

ALTER TABLE "CustomerDetailes".customers
ALTER COLUMN customerotherinitials TYPE character varying(10);

ALTER TABLE "CustomerDetailes".customers
ALTER COLUMN customerlastname TYPE character varying(50);

ALTER TABLE "CustomerDetailes".customers
ALTER COLUMN acountnumber TYPE character varying(15);

