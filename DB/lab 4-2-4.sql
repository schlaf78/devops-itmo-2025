CREATE UNIQUE INDEX ix_shareprices
ON "SharedDetails".shareprices (ShareID ASC, PriceDate DESC, Price);
