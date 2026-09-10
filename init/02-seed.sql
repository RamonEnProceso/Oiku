BEGIN;
SET CONSTRAINTS ALL DEFERRED;

INSERT INTO "bills_account" ("id", "name")
VALUES
  (1, 'Mercado Pago'),
  (2, 'Uala'),
  (3, 'Belo'),
  (4, 'Cash');
INSERT INTO "bills_category" ("id", "name")
VALUES
  (1, 'Income'),
  (2, 'Investment'),
  (3, 'Food'),
  (4, 'Transport'),
  (5, 'Health'),
  (6, 'Supermarket'),
  (7, 'Leisure'),
  (8, 'Material'),
  (9, 'Services'),
  (10, 'Utilities');
INSERT INTO "bills_subcategory" ("id", "category_id", "name", "mindless_spending")
VALUES
  (1, 1, 'Mom''s money', FALSE),
  (2, 1, 'Earnings', FALSE),
  (3, 2, 'CEDEARs', FALSE),
  (4, 2, 'USDs', FALSE),
  (5, 2, 'Mutual fund', FALSE),
  (6, 3, 'Restaurant', FALSE),
  (7, 3, 'Fast food', TRUE),
  (8, 3, 'Snack', TRUE),
  (9, 4, 'SUBE', FALSE),
  (10, 4, 'Ride-share', FALSE),
  (11, 5, 'Therapy Session', TRUE),
  (12, 7, 'Cinema', TRUE),
  (13, 7, 'Fair', TRUE),
  (14, 7, 'Drink', TRUE),
  (15, 8, 'College Supplies', FALSE),
  (16, 8, 'CD Albums', TRUE),
  (17, 8, 'Tech Gadgets', TRUE),
  (18, 8, 'Clothes', FALSE),
  (19, 9, 'Deepseek API', FALSE),
  (20, 9, 'Youtube Music', FALSE),
  (21, 10, 'Internet bill', FALSE),
  (22, 10, 'Gas bill', FALSE),
  (23, 10, 'Electric bill', FALSE),
  (24, 10, 'Water bill', FALSE);

SET CONSTRAINTS ALL IMMEDIATE;
COMMIT;