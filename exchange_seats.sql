
SELECT 
        (
            CASE 
                WHEN id%2=0 THEN id-1
                WHEN id%2<>0 and id<>(select max(id) from seat) THEN id+1
            ELSE 
                id
            END
        ) id
        ,student
FROM
    seat
ORDER BY id;