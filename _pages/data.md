---
layout: default
permalink: /data/
title: data
description: data
nav: true
nav_order: 3
---

The basis of the task will be a dataset consisting of several thousand entries. This dataset will be made public in several stages (see start page). Starting with the trial dataset, which is already available at [data/trial.csv](https://github.com/german-easy-to-read/statements/blob/master/data/trial.csv). The trial dataset gives participants an early opportunity to familiarize themselves with the structure and possible ways of processing the data. We also welcome any feedback and are happy to answer questions via e-mail. 

---
Our data structure:

|Column name | Description | Example value |
|---|---|---|
|**topic**| Topic. Defined by the lower-case title of the hurraki article title. | abfalltrennung | 
|**phrase**| Original phrase. | Der Abfall kommt in Tonnen oder Säcke. | 
|**phrase_number**| Number of the phrase. `_long` indicates, that the phrase belongs to `Genaue Erklärung` | 6_long | 
|**genre**| Genre(s) extracted based on the hurraki _Kategorien_ (categories) | Entsorgung\|Öffentliche_Verwaltung\|Seiten_mit_defekten_Dateilinks | 
|**timestamp**| Time of the article's last modification. | 2016-07-28T07:55:27Z | 
|**phrase_tokenized**| Phrase separated in tokens. Each token is given an index for referencing. | 0:=Der 1:=Abfall 2:=kommt 3:=in 4:=Tonnen 5:=oder 6:=Säcke. | 
|**num_statements**| Number of the statements. | 2 | 
|**statement_spans**| List of statements. Each statement is a span of word, represented by their indices.  | `[ [4], [6] ]` | 
|**author**| Pseudonymized (md5-hash) author id | `76bf1508c054395f67a605468d76c22f` |
|**notes**| Optional notes by the annotators. | disjunctive coordinating conjunction used |

---



Here is an example of how to process the data in python using pandas:

{::nomarkdown}
{% assign jupyter_path = "assets/jupyter/trial.ipynb" | relative_url %}
{% capture notebook_exists %}{% file_exists assets/jupyter/trial.ipynb %}{% endcapture %}
{% if notebook_exists == "true" %}
{% jupyter_notebook jupyter_path %}
{% else %}

<p>Sorry, the notebook you are looking for does not exist.</p>
{% endif %}
{:/nomarkdown}
