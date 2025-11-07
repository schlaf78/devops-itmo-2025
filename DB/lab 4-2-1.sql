CREATE UNIQUE INDEX ix_customers_customerid
    ON "CustomerDetails".customers USING btree
    ((customerid) ASC NULLS LAST)
    WITH (deduplicate_items=True)
;