<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.nsm.no/aktuelt/nsm-deler-tiltak-mot-sarbarhet-i-azure-api-management/ -->
<!-- fetched_at: 2026-11-25 07:34:15 -->
<!-- sha256: 6618e929476736b25bcb0dacb14cbc8c80cd525e64cedb13f730c67b7f4e4fc1 -->

NSM deler tiltak mot sårbarhet i Azure API Management - Nasjonal sikkerhetsmyndighet

Til innhold

Velg periode

Arkiv

2026 (16)

januar (2)

februar (1)

mars (3)

april (0)

mai (1)

juni (1)

juli (0)

august (1)

september (1)

oktober (2)

november (4)

desember (0)

2025 (12)

januar (0)

februar (1)

mars (0)

april (2)

mai (2)

juni (1)

juli (0)

august (1)

september (0)

oktober (1)

november (1)

desember (3)

2024 (16)

januar (2)

februar (1)

mars (2)

april (1)

mai (4)

juni (1)

juli (0)

august (0)

september (1)

oktober (2)

november (2)

desember (0)

2023 (20)

januar (3)

februar (1)

mars (3)

april (1)

mai (2)

juni (0)

juli (2)

august (1)

september (0)

oktober (4)

november (0)

desember (3)

2022 (26)

januar (3)

februar (4)

mars (4)

april (3)

mai (1)

juni (2)

juli (1)

august (1)

september (3)

oktober (1)

november (2)

desember (1)

2021 (47)

januar (6)

februar (6)

mars (7)

april (5)

mai (2)

juni (4)

juli (3)

august (3)

september (2)

oktober (1)

november (3)

desember (5)

2020 (36)

januar (3)

februar (4)

mars (6)

april (5)

mai (0)

juni (2)

juli (1)

august (3)

september (7)

oktober (4)

november (1)

desember (0)

2019 (15)

januar (1)

februar (0)

mars (1)

april (0)

mai (4)

juni (1)

juli (0)

august (2)

september (0)

oktober (0)

november (4)

desember (2)

2018 (13)

januar (1)

februar (0)

mars (2)

april (1)

mai (0)

juni (2)

juli (0)

august (2)

september (2)

oktober (2)

november (1)

desember (0)

2017 (12)

januar (0)

februar (0)

mars (1)

april (1)

mai (5)

juni (2)

juli (0)

august (0)

september (1)

oktober (0)

november (1)

desember (1)

2016 (8)

januar (0)

februar (1)

mars (2)

april (1)

mai (1)

juni (1)

juli (0)

august (1)

september (1)

oktober (0)

november (0)

desember (0)

2015 (11)

januar (0)

februar (0)

mars (2)

april (1)

mai (0)

juni (1)

juli (1)

august (0)

september (1)

oktober (2)

november (3)

desember (0)

2014 (23)

januar (1)

februar (0)

mars (2)

april (4)

mai (2)

juni (1)

juli (1)

august (4)

september (2)

oktober (3)

november (1)

desember (2)

Publisert: 20.11.2026
Oppdatert: 23.11.2026

Tidligere i uken ble NSM kjent med en sårbarhet i Azure API Management (APIM) som rammer flere norske virksomheter. Nå skal sårbarheten være lukket. NSM ber likevel virksomheter gjøre tiltak.

- NSM har siden sårbarheten ble kjent jobbet målrettet for å forstå betydningen av sårbarheten samt å kartlegge omfang og eventuelt andre berørte virksomheter. Det er fortsatt usikkert hvor omfattende utnyttelsen av sårbarheten er, og har vært. NSM har så langt ingen holdepunkter for at kompromittering eller forsøk på kompromittering har fått konsekvenser for leveranser hos norske virksomheter, sier Martin Albert-Hoff, avdelingsdirektør for operativ cybersikkerhet i NSM.
Tiltak Sårbarhet: En ukjent aktør har aktivt gått etter access tokens, secrets og named values i APIM.
Alle som har Azure API Manager må ta utgangspunkt i at deres secrets og named values er på avveie. Dette innebærer at virksomheten må rullere alle tokens og secrets.
Det er også viktig at virksomheter kartlegger hvilken informasjon som ligger bak APIM instansen sin for å avdekke det potensielle omfanget, dersom bevis for kompromittering avdekkes.
Virksomheter bør sjekke hvorvidt deres APIM-instans er blitt oppdatert. Følg brukerveiledningen:
Åpne https://<your-gateway-hostname>/internal-status-0123456789abcdef og les av RuntimeVersion
0.52.x: patchet dersom siste nummer (x) er 31936 eller høyere
0.53.x: patchet dersom siste nummer (x) er 31938 eller høyere
Andre mønstre (for eksempel 0.53.4608.0 eller 0.52.4150.0): V2 eller Consumption tier hvor denne terskelen ikke gjelder, er ikke sårbar
Lavere nummere, forsatt sårbar
Dersom virksomhetens instans ikke er blitt oppdatert, ber NSM virksomheten kontakte leverandøren direkte. Dersom virksomheten ser tegn på, eller har bekreftet kompromittering, ber vi virksomheten kontakte NSM.

Høyt risikonivå
Equinor og Skagerak Energi er blant virksomhetene som har blitt rammet. Sårbarheten ble først oppdaget av den norske energisektoren, som jobber godt med forebyggende sikkerhet.
- NSM ønsker å berømme Equinor for godt arbeid som førte til tidlig oppdagelse samt rask deling med NSM og de sektorvise responsmiljøene, sier Albert-Hoff.
Sårbarheten treffer flere sektorer i Norge og også utenfor Norges grenser. NSM har tett dialog og samarbeid med nasjonale og internasjonale samarbeidspartnere og virksomheter om situasjonen.
Når en sårbarhet blir kjent, vil flere aktører kunne forsøke å utnytte den. Rask eskalering i bruk av kunstig intelligens (KI) påvirker situasjonen. Dette utgjør en risiko for norske virksomheter.
- Det nasjonale cyberrisikonivået er høyt. Siste ukers hendelser bekrefter at risikoen for cyberoperasjoner er høy. Det er derfor viktig at virksomhetene som benytter tjenesten Azure API Management iverksetter tiltakene som NSM deler, sier Martin Albert-Hoff.
Les også: NSM hever det nasjonale cyberrisikonivået til HØYT
Et høyt risikonivå krever at norske virksomheter iverksetter forebyggende tiltak umiddelbart. Det er også årsaken til at NSM har gått offentlig ut med cyberrisikonivået for noen uker siden. Det er helt nødvendig å styrke både motstandsdyktigheten og evnen til å håndtere cyberoperasjoner i norske virksomheter. NSM har delt mange tiltak, som vi ønsker at virksomheter iverksetter. Alle tiltakene ligger på nsm.no .
Artikkelen er oppdatert 23. november. Det stod ved en feiltakelse at “sårbarheten ble først oppdaget av den norske kraftsektoren”. Dette er rettet til energisektoren.

Finner du det du leter etter?

Ja

Nei

Personvernerklæring for Nasjonal sikkerhetsmyndighet

Tilgjengelighetserklæring (bokmål)
