import openai
import datetime

# 1. NASTAVENÍ (Tvůj klíč)
openai.api_key = "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"

def analyzuj_a_vypis(cesta_k_txt_souboru, jmeno_obchodnika):
    print(f"--- Startuji analýzu pro: {jmeno_obchodnika} ---")
    
    # 2. NAČTENÍ TEXTU ZE SOUBORU
    try:
        with open(cesta_k_txt_souboru, 'r', encoding='utf-8') as f:
            text_hovoru = f.read()
    except FileNotFoundError:
        print(f"Chyba: Soubor '{cesta_k_txt_souboru}' nebyl nalezen ve složce.")
        return

    # 3. METODIKA
    metodika = """
      Jsi Obchodní Mentor & Asistent firmy Izolace Polná. Tvým úkolem je spravedlivě ohodnotit hovor.
    
    POKYNY PRO JEDNOTLIVÉ FÁZE:
    1. Příprava: Uznej pouze tehdy, pokud obchodník věci fyzicky používá nebo na ně odkazuje (např. „podívejte se na fotky“, „tady na iPadu“). Zmínka stačí.
    2. Dochvilnost a důvěra: Small talk a profesionální úvod.
    3. Předběžný souhlas: Otázky typu „Líbí se vám to takto?“ nebo „Jak chcete, aby to vypadalo?“.
    4. Identifikace problémů: Ukázka kritických míst (plísně, mosty) + vysvětlení následků.
    5. Rekapitulace na půdě: Jasné shrnutí analýzy a rizik přímo na místě izolace.
    6. Imunitrelax: Aktivní nabídka ošetření krovů (např. Anti-insect).
    7. Kalkulačka: Srozumitelný výpočet finanční úspory.
    8. Uzavření obchodu: Jasný pokus o administraci („Napíšeme to na vás?“). Pokud zákazník řekne „rozmyslím si to“ a obchodník nepředloží objednávku, je to NESPLNĚNO.
    9. Zvládání námitek: Práce s námitkou, hledání řešení.
    
    BODOVACÍ SYSTÉM (Fér pro všechny):
    - Začni s 10 body.
    - Za každý bod označený jako NESPLNĚNO odečti 1 bod.
    - Výsledek vypiš jako: [Počet bodů] z 10 ([Procenta]%).
    - Přidej zpětnou vazbu na to co udělal dobře a co naopak dobře neudělal a k tomu mu napiš nějakou větu na přístě, jak by se mohl zlepšit.
    """

    # 4. VOLÁNÍ AI 
    response = openai.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {"role": "system", "content": metodika},
            {"role": "user", "content": f"Zanalyzuj tento přepis pro obchodníka {jmeno_obchodnika}: {text_hovoru}"}
        ]
    )
    
    vysledek = response.choices[0].message.content

    # 5. VÝPIS VÝSLEDKU DO TERMINÁLU
    print("\n" + "="*30)
    print(f"VÝSLEDEK PRO: {jmeno_obchodnika}")
    print("="*30)
    print(vysledek)
    print("="*30 + "\n")

    # 6. ZÁPIS DO SOUBORU
    # Vytvoří název souboru: Vysledek_Jmeno_Datum.txt
    datum = datetime.datetime.now().strftime("%Y-%m-%d")
    nazev_vystupu = f"Vysledek_{jmeno_obchodnika.replace(' ', '_')}_{datum}.txt"
    
    with open(nazev_vystupu, 'w', encoding='utf-8') as f_out:
        f_out.write(f"VÝSLEDEK ANALÝZY HOVORU\n")
        f_out.write(f"Obchodník: {jmeno_obchodnika}\n")
        f_out.write(f"Datum analýzy: {datum}\n")
        f_out.write("="*30 + "\n")
        f_out.write(vysledek)
    
    print(f"Hotovo! Hodnocení bylo uloženo do souboru: {nazev_vystupu}")

# --- SPUŠTĚNÍ ---
analyzuj_a_vypis("Izolace_Test_chaoticky_kamaradsky_obchodnik.txt", "Tomaš Kašpar")