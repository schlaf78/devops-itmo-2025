ALTER TABLE IF EXISTS "TransactionDetails".transactions
    ADD CONSTRAINT fk_customers_transactions FOREIGN KEY (customerid)
    REFERENCES "CustomerDetails".customers (customerid) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
CREATE INDEX IF NOT EXISTS fki_fk_customers_transactions
    ON "TransactionDetails".transactions(customerid);