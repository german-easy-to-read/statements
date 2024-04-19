---
layout: about
title: about
permalink: /

news: true # includes a list of news items
selected_papers: false # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page
---

This workshop is a GermEval-task and will be co-located with [KONVENS 2024](https://konvens-2024.univie.ac.at/). We welcome contributions in English (preferred) and German. Prior to submitting a contribution, we kindly ask every participant / participating team to register via our [form](https://docs.google.com/forms/d/e/1FAIpQLSeD7W4jvrw0PKufz44NA4KgP-cSlHCl5hofBtvBoR30oc4krg/viewform?usp=sf_link)

---

German Easy Language (Leichte Sprache) is a controlled, simple language for which there have been several guidelines in the past. The draft of DIN SPEC 33429 has the potential to become the authoritative guideline. It describes several characteristics of German Easy language. Two of these are the number of statements and to format enumerations as lists. We have, therefore, segmented Easy Language sentences and annotated how well these aspects of DIN SPEC 33429 are implemented in web texts in German Easy language. 

With this shared task, we want to analyze both the number and the segments of the statements and automate this annotation. According to our definition, a statement contains only obligatory additions and no optional (omissible) additions following the concept of verb valency.
Example: 
`"Das Glas steht heute Abend auf dem Tisch." (engl.: "The glass is on the table tonight.", literally: "the glass stands today evening on the table.") (Local adverbial: auf dem Tisch; temporal adverbial: heute Abend). `
In this example, the local adverbial is obligatory because `"stehen" (eng: "standing")` requires a place. The temporal adverbial is not obligatory and thus forms a new statement. Therefore, this example contains two statements.

Our aim is to analyze and evaluate existing German Easy language texts. We do not want to enforce the use of one-statement sentences but merely analyze the density of statements. One target group is German Easy language authors who can check their own texts automatically. These annotations can also serve as a data basis for machine learning applications in the field of readability analysis and fact checking.


---

We are looking forward to an interesting workshop at KONVENS 2024. Please see the timetable or contact us for more information:

|             |                      |                                                                                                |
|-------------|----------------------|----------------------------------------------------------------------------------------------- |
|09.03.2024 - | Trial data ready     | [data/trial.csv](https://github.com/german-easy-to-read/statements/blob/master/data/trial.csv) |
|14.04.2024 - | Train data ready     | [data/train.csv](https://github.com/german-easy-to-read/statements/blob/master/data/train.csv) |
|18.05.2024 - | Test data ready      | |
|13.06.2024 - | Evaluation start     | | 
|25.06.2024 - | Evaluation end       | |
|01.07.2024 - | Paper submission due | | 
|20.07.2024 - | Camera ready due     | |
|13.09.2024 - | Workshop date        | |

---

## FAQ

**Q: How did you annotate your data?**

**A:** We tried to describe our process in detail in our [Annotation Guidelines](https://german-easy-to-read.github.io/statements/annotations)