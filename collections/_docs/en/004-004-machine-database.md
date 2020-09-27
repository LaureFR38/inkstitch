---
title: "Machine Database"
permalink: /docs/machine-database/
excerpt: ""
last_modified_at: 2020-04-12
classes: wide

inkstitch-formats:
 - read: 100, 10o, BRO, DAT, DSB, DST, DSZ, EMD, EXP, EXY, FXY, GT, INB, JEF, JPX, KSM, MAX, MIT, NEW, PCD, PCM, PCQ, PCS, PEC, PES, PHB, PHC, SEW, SHV, STC, STX, TAP, TBF, TXT, G-CODE, U01, VP3, XXX, ZXY
   write: CSV, DST, EXP, JEF, PEC, PES, SVG, TXT, G-CODE, U01, VP3

machine-database:
  - brand: Janome
    machines:
    - name: Memory Craft 400E
      file-formats: JEF, DST, DAT
      features: TRIM
      inkstitch-version: 1.27.2
      comments: Das ist ein Test. Kommentare, Kommentare!
  - brand: Brother
    machines:
    - name: Test
      file-formats: keine
      features: TRIM, STOP
      comments: blubber
    - name: Huhu
      file-formats: PES, PEC, DST
      features:
      inkstitch-version: 1.27.2
      comments: Supi
    - name: PE-800
      file-formats: PES, PEC, DST
      features:
      features: TRIM
      inkstitch-version: 1.28
      comments: Disable the ties checkbox in params, because this machine adds ties automatically

headlines:
  - machine:  "Machine"
  - file-formats: "File Formats"
  - features: "Features"
  - inkstitch-version: "Tested with Ink/Stitch Version"
  - comments: "Comments"

---
**Note:** As you can see, this database is just in planing. Don't take the data serious at this point.
{: .notice--warning }

{% include machine-list %}