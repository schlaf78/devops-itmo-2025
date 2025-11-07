CREATE TABLE "CustomerDetails".customerproducts
(
	customerfinancialproductid bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
	customerid bigint NOT NULL,
	financialproductid bigint NOT NULL,
	amounttocollect money NOT NULL,
	frequency int NOT NULL,
	lastcollected timestamp(0) NOT NULL,
	lastcollection timestamp(0) NOT NULL,
	renewable boolean NOT NULL
);

CREATE TABLE "CustomerDetails".financialproducts
(
	productid bigint NOT NULL,
	productname varchar(50) NOT NULL
);

CREATE SCHEMA "SharedDetails" AUTHORIZATION postgres;

CREATE TABLE "SharedDetails".shareprices (
	sharedpriceid bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
	shareid bigint NOT NULL,
	price numeric(18,5) NOT NULL,
	pricedate timestamp(0) NOT NULL
);

CREATE TABLE "SharedDetails".shares
(
	shareid bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
	sharedesc varchar(50) NOT NULL,
	shareticketid varchar(50) NULL,
	currentprice numeric(18,5) NOT NULL
);



