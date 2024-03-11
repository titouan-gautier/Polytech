------------------- PRE REQUIS -------------------

-- 1
create table unicode as select * from dataset.unicode;

-- 2
alter table unicode add constraint pk_unicode primary key (codepoint);
alter table unicode add constraint fk_upper foreign key (uppercase) references unicode(codepoint);
alter table unicode add constraint fk_lower foreign key (lowercase) references unicode(codepoint);
alter table unicode add constraint fk_title foreign key (titlecase) references unicode(codepoint);


------------------- PRISE EN MAIN -------------------

-- 1
EXPLAIN PLAN for
SELECT u1.codepoint, u1.charname
FROM unicode u1 JOIN unicode u2 ON u2.codepoint = u1.uppercase
WHERE u2.category_ = 'Lu';

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));
-- 1400 rows

-- 2

-- 3

-- 4

EXPLAIN PLAN for
SELECT u1.codepoint, u1.charname
FROM unicode u1
WHERE exists(
    SELECT u2.codepoint
    FROM unicode u2
    WHERE u2.codepoint = u1.uppercase
    and u2.category_ = 'Lu'
);

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

EXPLAIN PLAN for
SELECT u1.codepoint, u1.charname
FROM unicode u1 JOIN unicode u2 ON u2.codepoint = u1.uppercase
WHERE u2.category_ in 'Lu';

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

EXPLAIN PLAN for
SELECT u1.codepoint, u1.charname
FROM unicode u1 JOIN unicode u2 ON u2.codepoint = u1.uppercase
WHERE u2.category_ = 'Lu'
and (u1.COMBINING > 0 or u1.COMBINING <= 0);

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));


EXPLAIN PLAN for
SELECT u1.codepoint, u1.charname
FROM unicode u1 JOIN unicode u2 ON u2.codepoint = u1.uppercase
WHERE u2.category_ = 'Lu'
and (u1.digit > 0 or u1.digit <= 0 or u1.COMBINING > 0 or u1.COMBINING <= 0);

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

----------------------- Stats -----------------------

-- 6
BEGIN
    dbms_stats.delete_table_stats('E217657J', 'unicode');
    --dbms_stats.gather_table_stats('E217657J', 'unicode');
END;

select * from user_tab_statistics us where us.table_name = 'UNICODE';
select * from user_tab_col_statistics uc where uc.table_name = 'UNICODE';

/*
    USER_TAB_STATISTICS :
        NUM_ROWS: Le nombre total de lignes dans la table.
        BLOCKS: Le nombre de blocs alloués pour stocker les données de la table.
        EMPTY_BLOCKS: Le nombre de blocs vides dans la table.
        AVG_SPACE: L'espace moyen utilisé par une ligne dans la table.
        CHAIN_CNT: Le nombre de chaînes de migration, qui indique le nombre de blocs nécessaires pour stocker une ligne à la suite d'une autre.
        AVG_ROW_LEN: La longueur moyenne d'une ligne en octets.

    USER_TAB_COL_STATISTICS :
        NUM_DISTINCT: Le nombre de valeurs distinctes dans la colonne.
        LOW_VALUE et HIGH_VALUE: Les valeurs minimale et maximale de la colonne.
        DENSITY: La densité, qui est le nombre moyen de valeurs distinctes par bloc.
        NUM_NULLS: Le nombre de valeurs nulles dans la colonne.
        NUM_BUCKETS: Le nombre de compartiments utilisés pour l'histogramme.
        SAMPLE_SIZE: La taille de l'échantillon utilisée pour collecter les statistiques.
 */

-- 7

BEGIN
    dbms_stats.gather_table_stats('E217657J', 'unicode');
END;

SELECT *
FROM USER_TAB_COL_STATISTICS
WHERE TABLE_NAME = 'UNICODE' AND HISTOGRAM <> 'NONE';

/*
    La colonne CATEGORY_ possède un histogramme. un histogramme est souvent construit sur une colonne lorsque la
    distribution des valeurs dans cette colonne n'est pas uniforme, et cela permet à l'optimiseur de prendre des
    décisions plus intelligentes lors de l'évaluation des plans d'exécution des requêtes.
*/

-- 8

BEGIN
    dbms_stats.delete_table_stats('E217657J', 'unicode');
END;

EXPLAIN PLAN for
SELECT u1.codepoint, u1.charname
FROM unicode u1 JOIN unicode u2 ON u2.codepoint = u1.uppercase
WHERE u2.category_ = 'Lu';

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

------------------------- Les Indexes ----------------------------

select * from user_indexes where table_name = 'UNICODE';
select * from user_segments where segment_name = 'UNICODE';

SELECT segment_name, bytes, blocks
FROM user_segments
where segment_name = 'UNICODE';

/*

    INDEX_NAME : Le nom de l'index.
    TABLE_NAME : Le nom de la table sur laquelle l'index est créé.
    TABLE_OWNER : Le propriétaire de la table.
    TABLE_TYPE : Le type de la table (par exemple, "TABLE" pour une table standard).
    UNIQUENESS : Indique si l'index est unique ("UNIQUE") ou non ("NONUNIQUE").
    COMPRESSION : Indique si l'index utilise la compression ("ENABLED") ou non ("DISABLED").
    STATUS : Indique si l'index est actif ("VALID") ou invalide ("INVALID").
    PARTITIONED : Indique si l'index est partitionné ("YES") ou non ("NO").
    NUM_ROWS : Nombre approximatif de lignes dans l'index.
    BLOCKS : Nombre de blocs alloués à l'index.
    INDEX_TYPE : Type d'index (par exemple, "NORMAL" pour un index standard).

 */

/*

    SEGMENT_NAME : Le nom du segment.
    SEGMENT_TYPE : Le type de segment (par exemple, "TABLE" pour une table, "INDEX" pour un index).
    TABLE_NAME : Le nom de la table associée au segment (si applicable).
    TABLESPACE_NAME : Le nom de l'espace de table (tablespace) où le segment est stocké.
    BYTES : La taille en octets du segment.
    BLOCKS : Le nombre de blocs alloués pour le segment.
    SEGMENT_CREATED : La date à laquelle le segment a été créé.

 */

--- 2

ALTER TABLE unicode
ADD CONSTRAINT unicite_oldname UNIQUE (oldname);

select index_name, table_name, uniqueness
from user_indexes
where table_name = 'UNICODE';

--- 3
explain plan for
CREATE INDEX idx_unicode_covering
ON unicode (codepoint, uppercase, category_, charname);

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

--- 4

CREATE table unicode2 (
    codepoint NVARCHAR2(6) PRIMARY KEY,
    charname NVARCHAR2(100),
    uppercase NVARCHAR2(6),
    category_ NCHAR(2),
    FOREIGN KEY (codepoint) REFERENCES UNICODE(CODEPOINT)
)
ORGANIZATION INDEX
INCLUDING category_ overflow;

insert into unicode2 (codepoint, charname, uppercase, category_)
SELECT u1.codepoint, u1.charname, u1.uppercase, u1.category_ from unicode u1;

select index_name, table_name, table_owner from user_indexes where table_name='UNICODE2';

--- 5

EXPLAIN PLAN for
SELECT u1.codepoint, u1.charname
FROM unicode u1 JOIN unicode u2 ON u2.codepoint = u1.uppercase
WHERE u2.category_ = 'Lu';

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

EXPLAIN PLAN for
SELECT u1.codepoint, u1.charname
FROM unicode2 u1 JOIN unicode2 u2 ON u2.codepoint = u1.uppercase
WHERE u2.category_ = 'Lu';

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

BEGIN
    dbms_stats.gather_table_stats('E217657J', 'unicode2');
END;

alter table unicode drop constraint unicite_oldname;
drop table unicode2;


---------------------------- Partie 2 -----------------------

BEGIN
    dbms_stats.delete_table_stats('E217657J', 'unicode');
END;

BEGIN
    dbms_stats.gather_table_stats('E217657J', 'unicode');
END;

--- 1

EXPLAIN PLAN for
select charname
from unicode
where category_ = 'Lu'
and charname like 'LATIN%'
order by charname asc;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

--- 2

EXPLAIN PLAN for
select count(codepoint)
from unicode
where bidi = 'ON';

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

--- 3
EXPLAIN PLAN FOR
select u.codepoint,
			 u.charname,
			 u.category_,
			 u.combining,
			 u.bidi,
			 u.decomposition,
			 u.decimal_,
			 u.digit,
			 u.numeric_,
			 u.mirrored,
			 u.oldname,
			 u.comment_,
			 lc.charname as lowercase,
			 uc.charname as uppercase,
			 tc.charname as titlecase
from unicode u left outer join unicode lc on u.lowercase=lc.codepoint
left outer join unicode uc on u.uppercase=uc.codepoint
left outer join unicode tc on u.titlecase=tc.codepoint
where u.codepoint='0405';

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

--- 4

EXPLAIN PLAN FOR
select avg(length(u.charname))
from unicode u
join unicode uc on u.uppercase = uc.codepoint
where uc.oldname like '%GREEK%';

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

-------------------------------- Partie 3 ---------------------------------

-- index range scan
create index index_digit on unicode(digit);

explain plan for
select u1.codepoint
from unicode u1
where u1.DIGIT > 2;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

drop index index_digit;

-- index skip scan

create index index_skip on unicode(category_, charname);

explain plan for
select u1.codepoint
from unicode u1
where 'LATIN' = u1.CHARNAME;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

drop index index_skip;

-- nested loops

EXPLAIN PLAN for
SELECT u1.codepoint, u1.charname
FROM unicode u1
INNER JOIN unicode u2 ON u2.codepoint = u1.uppercase
WHERE u1.category_ = 'Lu'
  AND u2.CHARNAME LIKE 'LATIN%';

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

-- merge join

EXPLAIN PLAN for
select /*+ use_merge(u1,u2) */ u1.UPPERCASE, u2.LOWERCASE
from unicode u1 join unicode u2 on u1.UPPERCASE = u2.LOWERCASE;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

---- triple jointure

EXPLAIN PLAN FOR
SELECT /*+ use_merge(u2,u4) */ u1.UPPERCASE, u2.LOWERCASE
FROM unicode u1
JOIN unicode u2 on u2.LOWERCASE = u1.CODEPOINT and u2.UPPERCASE = u1.CODEPOINT
JOIN unicode u3 on u3.UPPERCASE = u1.CODEPOINT
JOIN unicode u4 on u4.LOWERCASE = u2.CODEPOINT;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));


----- sort unique

EXPLAIN PLAN for
SELECT distinct u1.DIGIT
from unicode u1
order by u1.DIGIT;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

-------- hash group by

EXPLAIN PLAN FOR
select u1.CATEGORY_, count(*)
from unicode u1
group by U1.CATEGORY_;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE'));

drop table unicode;







