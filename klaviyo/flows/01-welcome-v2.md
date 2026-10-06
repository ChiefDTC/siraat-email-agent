# Welcome Flow v2 · spec en copy

Status: ontwerp 6 oktober 2026. Vervangt "EB | Welcome Flow | Updated 02.03.26" (SiaNLu).

## Waarom opnieuw

| Huidige flow (30 dagen) | |
| --- | --- |
| Mails | 8 live, over 10 dagen, allemaal als afbeeldingsslices (0 tot 2 regels live tekst) |
| Mail 1 | 5 minuten na aanmelding, belooft code HI10 (10 procent). De pop-up belooft nu een giveaway-lot, geen code. |
| Uitschrijf | 1,83 procent totaal; mail 1 2,70 procent, mail 2 2,37 procent, mail 3 2,16 procent |
| Spamklachten | 0,09 procent totaal, mail 1 0,16 procent (Gmail-grens is 0,10) |
| Omzet | $38.565, waarvan $24.416 uit mail 1 |
| Afzender | "Benjamin" als oprichter in mail 2. De brand guidelines noemen Floris van der Heijden als eigenaar. |

Besluiten:
- Vijf mails in zeven dagen in plaats van acht in tien. Eerste mail na 10 minuten, daarna om 10:00 lokale tijd.
- Geen kortingscode in de reeks. Het aanbod op de site (4 gifts, tot 50 procent) is al het aanbod; een extra code kost alleen marge. Mail 5 verwijst naar het site-aanbod zonder code. Later A/B-testen: wel of geen code in mail 5.
- Oprichtersnoot ondertekend door Floris (echte oprichter, "honest by default"). Te bevestigen door Siraat. Als "Benjamin" bewust een persona is, één woord vervangen.
- Live tekst in Inter, koppen als afbeelding (TT Ramillas), één hero-foto per mail. Geen navigatie, geen social footer.
- Bestaande klanten die zich aanmelden krijgen één andere mail, niet de verkoopreeks.

## Structuur

```
Trigger: Added to list "Welcome" (lijst Uw8eZG), zelfde lijst als de giveaway-pop-up
Flow-filter: e-mail bevat niet "test@", nog nooit in deze flow geweest
Herinstap: nooit

Split A: Placed Order > 0 ooit?
  JA  → tak Bestaande klant
        wacht 10 minuten → E0 "You're in (and thank you)" → einde
  NEE → tak Prospect
        wacht 10 minuten → E1 "You're in. One thing before you go."  [A/B op onderwerp]
        wacht 1 dag tot 10:00 → E2 "The coating your pan is hiding from you"
        wacht 2 dagen tot 10:00 → E3 "Does food really not stick? (and 4 other questions)"
        wacht 2 dagen tot 10:00 → E4 "What people say after a month with the pan"
        Split B: Placed Order > 0 sinds start van de flow?
          JA  → einde (post-purchase flow neemt over)
          NEE → wacht 2 dagen tot 10:00 → E5 "The best way to try a Siraat pan"
                wacht 3 dagen tot 10:00
                Split C: Clicked Email in deze flow?
                  JA  → E6 "Still thinking it over?" (tekstmail) → einde
                  NEE → einde
```

Verzendfilter op E2 tot en met E6: Placed Order = 0 sinds start van de flow. Smart sending aan vanaf E2, uit op E0 en E1.
Totaal: 5 mails voor de meeste mensen, 6 voor wie klikt maar niet koopt. Dag 0, 1, 3, 5, 7, 10.

A/B op E1 (50/50, winnaar op unieke kliks, 4 weken):
- A: "You're in. One thing before you go."
- B: "Your entry is confirmed, {{ first_name|default:'friend' }}"

## Copy

Toon: kalm register. Korte zinnen. Eén idee per alinea. Cijfers in plaats van bijvoeglijke naamwoorden. Claims alleen uit de goedgekeurde lijst.

### E0 · Bestaande klant · "You're in (and thank you)"

Preview: Your giveaway entry is confirmed. One thing you might not know we make.

Hi {{ first_name|default:'there' }},

Your entry for Win Your Order For Free is in. Nothing else to do. We draw a winner every month and email them directly.

You already own a Siraat pan, so I'll skip the sales pitch. One thing you might not have seen: we make dishwasher detergent sheets. Plastic-free, phosphate-free, chlorine-free, fresh lemon. They came out of the same question as the pan: what is actually touching the things my family eats from?

If you'd like to try them, they're here. If not, no more emails about them.

And if your pan has given you any trouble at all, reply to this email. A real person reads these and we fix things.

Floris
Founder, Siraat's Kitchen

CTA: See the dishwasher sheets

### E1 · Prospect · dag 0, 10 minuten · "You're in. One thing before you go."

Preview: Your giveaway entry is confirmed. Here's what we'll send you, and what we won't.

Hi {{ first_name|default:'there' }},

Your entry for Win Your Order For Free is in. Nothing else to do. We draw a winner every month and email them directly.

I'm Floris, one of the founders. The short version of why Siraat exists: every nonstick pan I ever owned was a coating with a countdown. It scratched, it wore, and whatever wore off ended up in the food. So we built a pan with no coating at all. A pure titanium cooking surface with a hammered pattern that releases food on its own.

Over the next week I'll send you four short emails:
1. What is actually in a nonstick coating, and what we did instead.
2. Honest answers to the five questions people ask us most. Yes, eggs.
3. What customers say after a month with the pan.
4. The best place to start if you decide to try one.

No daily sale emails. If you ever want out, the unsubscribe link is at the bottom of every email and it works on the first click.

Got a question now? Hit reply. A real person reads these.

Floris

PS. Every order comes with a 100-day home trial and a lifetime warranty. The trial starts the day the box arrives, not the day you order.

CTA: See the pan

Hero: geen hero. Tekstmail met logo bovenaan. Kleine productfoto onder de handtekening (Pan Pro Standard).

### E2 · dag 1, 10:00 · "The coating your pan is hiding from you"

Preview: Why "PFOA-free" does not mean what you think it means.

Hero (vierkant, kop als afbeelding): macro van het gehamerde oppervlak. Kop: "No coating. Nothing to peel."

Eyebrow: WHAT'S IN A NONSTICK PAN

Kop (live, Inter Semi Bold 22): The coating is the product

Most nonstick pans are a thin layer of PTFE over aluminium. The layer starts breaking down around 260°C (500°F). That is why the box says "do not preheat empty" and "no metal utensils". The pan is not fragile. The coating is.

"PFOA-free" sounds reassuring. Consumer Reports tested pans with that label and still found PFAS compounds in the coating, including PFOA, as manufacturing byproducts. The honest way to avoid PFAS is to avoid the coating.

Kop: What we did instead

We skipped the coating. The Titanium Hammered Pan Pro has a pure titanium cooking surface. Titanium is the metal used for surgical implants because it does not react with the body, and it does not react with your food either. Under it sits an aluminium core for even heat and a stainless base for induction. Only the titanium touches your food.

The hammered pattern is not decoration. Food touches less surface, so it releases with less oil. A thin oil film, medium heat, and the pan does the rest.

Bewijsblok (sand-achtergrond, drie regels met middots):
Tested by Light Labs · Free from PFAS, BPA and toxins
Cooking surface · pure titanium, no coatings
Oven safe · 548°C / 1000°F

Kop: What that means in your kitchen

Metal spatula? Fine. A scratch on titanium is a mark, not a leak. Nothing flakes into the eggs. And because there is no coating to wear out, we can put a lifetime warranty on it.

CTA: See how the pan is made

Onder de CTA, klein: Tomorrow: the five questions everyone asks before they buy, answered straight.

### E3 · dag 3, 10:00 · "Does food really not stick? (and 4 other questions)"

Preview: Eggs, induction, the oven, cleaning, and what to do in the first week.

Hero (vierkant): gebakken ei in de pan, van bovenaf. Kop als afbeelding: "Five honest answers"

Intro: These are the five questions we get most, in the order people ask them. Straight answers, including the one that needs a small adjustment on your side.

1. Does food really not stick?
Not like Teflon, and that is on purpose. There is no coating doing the work, so two habits do it instead. Preheat on medium for 2 to 3 minutes, then flick a few drops of water in: when they bead up and dance, add a thin film of oil. Give the food a moment before you flip; it releases on its own. Skip the preheat and it will stick, same as any uncoated pan. Our 2-minute video shows the water test. [link naar instructievideo]

2. Which stoves does it work on?
Gas, induction, electric and ceramic, thanks to the magnetic stainless base. Oven safe to 548°C / 1000°F.

3. How do I clean it?
Let it cool, then warm water and a soft sponge. Thirty seconds on a normal day. Brown marks after a hot sear are heat patina, not damage: a baking soda paste for ten minutes takes them off. No steel wool.

4. What is the pan actually made of?
Three layers. A 0.5 mm pure titanium cooking surface, the only layer that touches your food. A 1 mm aluminium core for even heat. A 0.6 mm stainless base for induction. No coating anywhere. Metal utensils are fine; a mark on titanium is a mark, not a leak.

5. What if it is not for me?
You have 100 days at home to decide. If it is not the pan for you, send it back, free. After that, the lifetime warranty covers the pan itself.

CTA: Watch the 2-minute video

PS. Reply if your question is not here. We answer every one.

### E4 · dag 5, 10:00 · "What people say after a month with the pan"

Preview: Thomas threw out his old pans after a week. Three more stories inside.

Hero (vierkant): flash-stijl foto, mensen aan het koken (flash-duo). Kop als afbeelding: "100,000+ kitchens later"

Reviewblok, drie reviews (crème kaart, 5 sterren in brick, citaat in Instrument Serif Italic 22, naam in Inter 13):
- "I followed your directions, made scrambled eggs and they came out of the pan perfectly. I am getting rid of my non stick pans. I only need the new one." Marilyn B., verified buyer
- "I don't want the forever chemicals. The real test was my egg the next morning. After a very light nudge, the egg released completely and slid around the pan." Michael G., verified buyer
- "The eggs DO NOT STICK! The meat is seared perfectly on the outside and tender inside. No more scrubbing pan!" Jeanne K., verified buyer

Regel onder de reviews: 4.8 out of 5 · 3,281 reviews · 100,000+ customers

Kop (live): Where most people start

Productrij 2x2 (foto, naam, prijs, knop):
- Titanium Hammered Pan Pro, Standard · $134 · The one to start with
- Titanium Hammered Deep Pan Pro · $134 · Stews, sauces, one-pan dinners
- Titanium Hammered Wok Pan Pro · $134 · High heat, fast cooking
- Titanium Cutting Board · $69 · Anti-microbial, plastic-free

CTA: Start with the Pan Pro

### E5 · dag 7, 10:00 · "The best way to try a Siraat pan"

Preview: 4 gifts with every order, a 100-day trial, and a lifetime warranty. No code needed.

Hero (vierkant): productfoto Pan Pro met de vier gifts ernaast. Kop als afbeelding: "Try it for 100 days"

Intro: If you have read this far, you probably want to know what it costs to find out for yourself. Here is everything, in one place.

Aanbodblok (wisselbaar blok, nu het oktober-aanbod):
4 gifts with every order
Free shipping protection · Mystery gift · Cooking e-book · Weekly draw for a $450 PFAS water purifier
Up to 50% off, applied on the site. No code needed.
(The mystery gift is a pack of our plastic-free dishwasher sheets: one sheet, one cycle, no plastic pod.)
Prices are in USD and convert to your currency at checkout.

Garantieblok (drie kolommen, iconen):
100-day home trial · starts the day the box arrives
Lifetime warranty · on every pan
Free shipping · on all orders

Kop (live): Which pan?

If you cook for one or two: the Pan Pro Small. For a family: the Standard or Large. If you want one pan that does everything from eggs to stew: the Deep Pan Pro.

CTA: Choose your pan

PS. Your giveaway entry stays valid whether you order or not. We draw at the end of the month.

### E6 · dag 10, alleen na klik zonder aankoop · "Still thinking it over?"

Preview: One question, no pitch.

Hi {{ first_name|default:'there' }},

You opened a couple of these emails and clicked through, so the pan caught your eye. Something held you back.

I'd rather know what it was than guess. Was it the price, the "will my eggs stick" question, the size, or something else?

Reply with one line. I read every reply, and if it is a question, you'll get a real answer, not a brochure.

Floris

(No CTA button. Only a reply.)

## Wat er nog ingevuld moet worden

- Garantiewoord: brand guidelines zeggen "lifetime warranty", Gorgias-macros "75-year warranty". E-mail gebruikt "lifetime warranty" tot Siraat beslist.
- Naam van de oprichter bevestigen (Floris of Benjamin).
- Link van de instructievideo: https://cdn.shopify.com/videos/c/o/v/a0f401a864224d35b1e30d8dc2b3617e.mp4 (uit de oktober-brief). In e-mail: afbeelding met play-knop die naar een pagina met de video linkt, niet de mp4 zelf.
- Het aanbodblok in E5 is wisselbaar per maand.
