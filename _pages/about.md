---
layout: about
title: about
permalink: /

news: true # includes a list of news items
selected_papers: false # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page
---

This workshop is a GermEval-task and will be co-located with [KONVENS 2024](https://konvens-2024.univie.ac.at/). We welcome contributions in English (preferred) and German. Submissions can tackle one or two of the sub tasks, deciding for only one sub task has no effect on the acceptance of the submission. Prior to submitting a contribution, we kindly ask every participant / participating team to register via our [form](https://docs.google.com/forms/d/e/1FAIpQLSeD7W4jvrw0PKufz44NA4KgP-cSlHCl5hofBtvBoR30oc4krg/viewform?usp=sf_link), this helps us to more effectively organize the event.

---

German Easy Language (Leichte Sprache) is a controlled, simple language for which there have been several guidelines in the past. The draft of DIN SPEC 33429 has the potential to become the authoritative guideline. It describes several characteristics of German Easy language. Two of these are the number of statements and to format enumerations as lists. We have, therefore, segmented Easy Language sentences and annotated how well these aspects of DIN SPEC 33429 are implemented in web texts in German Easy language. 

With this shared task, we want to analyze both the number and the segments of the statements and automate this annotation. According to our definition, a statement contains only obligatory additions and no optional (omissible) additions following the concept of verb valency.
Example: 
`"Das Glas steht heute Abend auf dem Tisch." (engl.: "The glass is on the table tonight.", literally: "the glass stands today evening on the table.") (Local adverbial: auf dem Tisch; temporal adverbial: heute Abend). `
In this example, the local adverbial is obligatory because `"stehen" (eng: "standing")` requires a place. The temporal adverbial is not obligatory and thus forms a new statement. Therefore, this example contains two statements.

The shared task comprises two subtasks:  
**Subtask 1: Detemining the number of statements**  
In the first subtask, the number of statements in the sentences should be predicted. The target is a whole number.  
**Subtask 2: Annotating the statement spans**  
In this subtask, the spans of the previously identified statements will be extracted. For details about the annotation and statement extraction, see our [annotation guidelines](https://german-easy-to-read.github.io/statements/annotations/). 

Our aim is to analyze and evaluate existing German Easy language texts. We do not want to enforce the use of one-statement sentences but merely analyze the density of statements. One target group is German Easy language authors who can check their own texts automatically. These annotations can also serve as a data basis for machine learning applications in the field of readability analysis and fact checking.


---

We are looking forward to an interesting workshop at KONVENS 2024. Please see the timetable or contact us for more information:

|           |                      |                                                                                                |
|-----------|----------------------|----------------------------------------------------------------------------------------------- |
|09.03.24 | Trial data ready       | [data/trial.csv](https://github.com/german-easy-to-read/statements/blob/master/data/trial.csv) |
|14.04.24 | Train data ready (final update 14.05.24, bug fixes 04.06.2024) | [data/train.csv](https://github.com/german-easy-to-read/statements/blob/master/data/train.csv) |
|18.05.24 | Test data ready      | [data/test.csv](https://github.com/german-easy-to-read/statements/blob/master/data/test.csv) |
|17.06.24 | Evaluation 1st phase: Development (test data)     | please submit via [CodaBench](https://www.codabench.org/competitions/3244) | 
|28.06.24 | Evaluation 2nd phase: Final (eval data)       |please submit via [CodaBench](https://www.codabench.org/competitions/3244) |
|12.07.24 | Evaluation end (last submissions possible)       | please submit via [CodaBench](https://www.codabench.org/competitions/3244)|
|01.07.24 | Paper submission due | | 
|02.08.24 | Camera ready due     | |
|13.09.24 | Workshop date        | |
