ALTER TABLE "TransactionDetails".transactions
ADD CONSTRAINT fk_transactions_shared
FOREIGN KEY (relatedshareid)
REFERENCES "SharedDetails".shares(shareid);
