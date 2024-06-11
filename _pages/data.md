---
layout: default
permalink: /data/
title: dataset
description: dataset
nav: false
nav_order: 10
---

The basis of the task will be a dataset consisting of several thousand entries. This dataset will be made public in several stages (see start page). Starting with the trial dataset, which is already available at [data/trial.csv](https://github.com/german-easy-to-read/statements/blob/master/data/trial.csv). The trial dataset gives participants an early opportunity to familiarize themselves with the structure and possible ways of processing the data. We also welcome any feedback and are happy to answer questions via e-mail.  

---

We have started to upload the training data. It is available at [data/train.csv](https://github.com/german-easy-to-read/statements/blob/master/data/train.csv) and will be uploaded iteratively until the evaluation period starts. Be sure to check out the latest version the achieve the best results possible. Please notice, that we have included sentences with `0` statements, which means that those sentences are incomplete or erroneous. In this case, even sentences with multiple statements can be annotated by `0`. Nonetheless, we left them in the data to create a real world experiences.  

---
## Our data structure:

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

## Example: 

Here is an example of how to process the data in python using pandas:

{::nomarkdown}
{% assign jupyter_path = "assets/jupyter/data.ipynb" | relative_url %}
{% capture notebook_exists %}{% file_exists assets/jupyter/data.ipynb %}{% endcapture %}
{% if notebook_exists == "true" %}
{% jupyter_notebook jupyter_path %}
{% else %}

<p>Sorry, the notebook you are looking for does not exist.</p>
{% endif %}
{:/nomarkdown}


## Content notice for sensitive content
This dataset contains descriptions of violence, death, abuse and discrimination. We are including this content, because we randomly selected articles from the source site as a whole without applying any content-aware filtering, in order to maintain a neutral perspective on the data and avoid any cherry-picking. Since we are not the authors of the articles, we do not take responsibility for the content. The chances of success of submissions from participants are independent of the content of the sentences, but are based solely on linguistic and statistical evaluations. 

This notice follows the ideas describe in this [article from Stanford]( https://tlhub.stanford.edu/docs/writing-content-notices-for-sensitive-content)