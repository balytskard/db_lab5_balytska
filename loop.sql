DO $$
    DECLARE
        i INT;
    BEGIN
        FOR i IN 1..2
            LOOP
                INSERT INTO ratings (user_id, isbn, book_rating)
                VALUES (
                        CASE i
                            WHEN 1 THEN 301
                            WHEN 2 THEN 387
                        END,
                        CASE i
                            WHEN 1 THEN '2710676413'
                            WHEN 2 THEN '6419765825'
                        END,
                        CASE i
                            WHEN 1 THEN 8
                            WHEN 2 THEN 4
                        END
                       );
            END LOOP;
    END
    $$;

SELECT * FROM ratings;