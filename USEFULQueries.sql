-- This is NOT a good query!
SELECT usery.user_name AS creator, lists.name AS list, short_text.entry AS entry
FROM usery, short_text, lists
WHERE usery.id = short_text.user_id AND lists.user_id = short_text.user_id
GROUP BY creator, list, entry
ORDER BY creator, list, entry;



SELECT usery.user_name as creator, short_text.entry as entry, short_text.row_id as row
FROM usery, short_text
WHERE usery.id = short_text.user_id
--GROUP BY creator, entry, row
ORDER BY row;