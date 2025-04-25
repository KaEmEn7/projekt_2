- Skore je zapisovano do results.txt
- moznost nove hry po dohrani,
- casovac pocita cas
- pocitadlo pokusu

- TODO: FIX: debugger print v určité smyčce kódu píše hádané číslo... - lektor neobjevil. muahahaha - FIXED
- V.2 - upraveny komentáře, definice, main konstrukt atd podle poznámek lektora

  
Hodnotitel tvého projektu: Petr Lorenc

Co by šlo vylepšit:
- změň název funkce. Název 'max_lenght' by měl být 'max_length'.
- nevyužití proměnné. Proměnná 'counter' by měla být inicializována před smyčkou, aby se zabránilo chybám.
- chybějící testování na vstupu. Vstup by měl být validován podrobněji, aby se zajistilo, že je to číslo a nesplňuje specifikace.
- zbytečné porovnávání. Kontrola 'is_unique_number' v případě platného vstupu je redundatní, protože je kontrolována už v podmínce smyčky.
- nejasná implementace. 'bulls_and_cows' funkce by měla více komentářů k vysvětlení počítání bull a cow.
- kód by měl být čitelnější. Je dobré použít konstanty pro magické číslo, jako je 4 pro délku čísla, pro lepší srozumitelnost.
- konzistentní používání uvozovek. Používej buď jednoduché, nebo dvojité uvozovky konzistentně.
- nevyužíváš main konstrukt, je potreba ho pridat aby kod mohl byt importovan bez spusteni
- obecne bych pridal par dokumentacnich komentaru a nemichal definice funkci a jejich volani


