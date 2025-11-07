CREATE TABLE "CustomerDetails".customers
(
    customerid bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    customertitleid integer NOT NULL,
    customerfirstname character varying(50)[] NOT NULL,
    customerotherinitials character varying(10)[],
    customerlastname character varying(50)[] NOT NULL,
    addressid bigint NOT NULL,
    accountnumber character(15)[] NOT NULL,
    accounttypeid integer NOT NULL,
    clearebalance money NOT NULL,
    unclearebalance money NOT NULL,
    dateadded date NOT NULL DEFAULT current_date,
    PRIMARY KEY (customerid)
);

ALTER TABLE IF EXISTS "CustomerDetails".customers
    OWNER to postgres;