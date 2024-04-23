---
layout: default
permalink: /annotations/
title: annotation guidelines
description: annotation guidelines
nav: false
nav_order: 10
---
# Data annotation guidelines
Our data samples are single sentences. We split sentences at punctuation marks, hence, they can span over several lines. We annotate the sentences by the number of statements contained in them. The tokens in the sentence are separated by whitespace. A statement only contains full tokens; we don't split tokens for subtoken annotations. If a sentence spans several lines (as typical for Leichte Sprache), the line breaks are displayed with ‘\newline’. Newlines could help classification models in the future, and thus, they are given as separate tokens but should be ignored during annotation.

The samples are taken from the Hurraki homepage as they are. We do not correct any typos manually. Thus, the samples can contain punctuation or grammatical errors. If the errors are severe, e.g., if two sentences are merged into one due to missing punctuations, these samples are annotated as erroneous.
<!--- In this file, we discuss the rules for determining the number of statements and how to annotate the separate spans. -->

## Determining the number of statements / Statement separation
Ideally, a statement is formed by a Subject-Verb-Object (SVO) combination or additional adjectives or prepositional constructions that could form a separate sentence. 
Example: `Die moderne Sportart heißt: \newline Splashdiving.` contains 2 statements, one for the main SVO combination `Die Sportart heißt Splashdiving`, and one for the additional adjection `moderne`. The sentences don't have to be in proper SVC order, as subclauses can form a statement without any main clause. As a rule of thumb, one statement contains only one full verb at maximum (yet auxiliary and full verb can be together).

A sentence is split into multiple sentences following these criteria:
#### 1. Separating via conjunctions
Conjunctions are used to connect clauses within a sentence. There are two types of conjunctions:
 1. Coordinating conjunctions connect two main clauses. 
 2. Subordinating conjunctions connect a main clause with a subordinate clause, emphasizing the main clause more than the subordinate clause. 
 
There are only a few different semantic categories of coordinating conjunctions (see [Table 1](#table1)). In contrast, there are numerous different subordinating conjunctions. They can be divided into time, reason, and condition groups. Some subordinating conjunctions do not fit into any of these groups, though.

|Semantic category |coordinating conjunction (examples)| example sentence|
|---|---|---|
|additive |und so, weder – noch, nicht nur – sondern auch|Weder er noch seine Tochter wurden von dem Lärm aufgeweckt.|
|adversative |aber, sondern|Sie fragte ihn, aber er war ahnungslos.|
|disjunctive |entweder – oder|Du kannst entweder dein Zimmer aufräumen oder das Papier wegräumen.|
|explicative|das heißt|Er ist national bekannt, das heißt, man kennt ihn im ganzen Land.|
|causal |denn (umgangssprachlich: weil)|Er ist glücklich, denn er wird bald heiraten.|
|koncessive |wenn auch, wenngleich (+ Adj.)|Es ist ein trauriger, wenn auch ein aufschlussreicher Tag.|
|comparative |als, wie|Er mag sein Auto lieber als seine Frau.|

> <a name="table1"></a> **Table 1**: List of the semantic categories of German coordinating conjunctions \
> Source:[Wikipedia:Konjunktion](https://de.wikipedia.org/wiki/Konjunktion_(Wortart))

##### Special case: `Manche sagen` and `Das heißt`
`Das heißt, ..` is a common construction in Leichte Sprache. These phrases are not counted as separate statements. However, if the phrase contains additional information, such as `Lügen heißt..` or `Manche Politiker sagen..'`, these phrases are annotated as usual. Only the very specific formulations above are an exception.

##### Special case: Parentheses
Information in parentheses is always a separate statement.

#### 2. Separating via single adjectives/adverbials
Nouns are often further described by adjectives. If these adjectives give additional information or restrict the noun to a subgroup, these adjectives form a separate statement. In the example below, the adjective `modern` gives additional information about the sport, so it is extracted as a new statement. In contrast, if the adjective/adverb gives no further restrictions, it is not counted as a separate statement.

If multiple adjectives/adverbs are concatenated into a sequence, each of them forms a single statement. 
Examples:

|Sentence|Number of statements|Explanation|
|---|---|---|
|Die moderne Sportart heißt: \newline Splashdiving.|2|`modern` gives additional information about the sport|
|Der Vorschlag wurde ohne Gegenstimmen angenommen.|2|Modal adverbial `ohne Gegenstimmen`|
|Die Einwohner konnten ihre Lebensmittel ganz normal kaufen.|1|`ganz normal` gives no restrictions|
|Die Mitarbeiter reparieren gemeinsam kaputte Dinge.|2|Sequence: Die Mitarbeiter reparieren gemeinsam. Die Mitarbeiter reparieren kaputte Dinge.|


##### Special case: Quantifiers
Quantifiers like `viele, alle, mache` or counts like `50 Menschen` are no separate statements.

##### Special case: Filler words
Filler words like `sehr`, `oft`, `darum`, or `auch` are no separate statements.

#### 3. Separating via prepositional phrase
Prepositional often specify things and actions, e.g., by indicating ownership (`von ..`), a direction (`nach ..`), or modality (`mit ..`). Similar to adjectives, this additional information forms a new statement. For example, the sentence `Man kann mit einem Fahr-stuhl nach oben fahren.` contains the prepositional phrases `mit einem Fahrstuhl` and `nach oben`, thus containing two statements. If multiple prepositional phrases are stacked after another, each of them forms a separate statement.

##### Special case: Composites
Prepositional phrases that can be rephrased to a single word (e.g., `Religion der Christen` -> `Christentum`; `Mitglied in der Partei` -> `Parteimitglied`) are no additional statement.
##### Special case: Trivial prepositions
Sometimes, the verb already contains the information in the prepositional phrase (e.g., `in die Luft sprengen`). Then, we don't annotate the prepositional phrases as separate statements.
##### Special case: Date and year specifications
Dates are annotated as separate statements except if the remaining statement only states that something exists or was born. For example, in the sentence `Im Jahr 1877 heiraten Alexander Graham Bell und Mabel Hubbard.`, the year and the marriage itself are two different statements. However, in the sentence `Angela Merkel wurde am 17. Juli 1954 geboren.`, the information that she was born is trivial. Thus, the sentence contains only 1 statement.
In contrast, abstract time information like `manchmal` or `immer` is no separate statement.

#### 4. 0-statement sentences or un-parseable sentences (= erroneous samples) <a name="zero-statements"></a>
There can be samples that don't contain a statement, e.g., if there are problems with the pre-processing and there are multiple sentences in the sample. Also, sentences that don't contain a verb, like `An der Universität Boston.`, are annotated with 0.

## Annotating the statement spans
We enumerate the tokens in the sentence to simplify referring to them in the statement span annotations. The statement spans are only annotated for samples with more than 1 statement. In this case, we annotate the tokens that belong to the different spans as a set of statements spans:
* The order of the spans and the order of tokens within the spans is not important and can be altered.
* Articles, coordinating conjunctions, and `\newline` are never included in the spans. In contrast, subordinating conjunctions, relative pronouns, or [filler words](special-case-filler-words) are included.
* Only the mutually exclusive parts are annotated, i.e., tokens that are contained in all statements are not annotated.

|Sentence|Number of statements|Statement spans|Explanation|
|---|---|---|---|
|0:=Die 1:=moderne 2:=Sportart 3:=heißt: 4:= 5:=\newline 6:=Splashdiving|2|[[1],[3,6]]|Tokens 0, 4, 5 are never annotated. Token 2 (Sportart) is in both spans, so it is not stated explicitly.|
|0:=Der 1:=Vorschlag 2:=wurde 3:=ohne 4:=Gegenstimmen 5:=angenommen.|2|[[1,2,5],[3,4]]|No overlaps between statements|
|0:=Die 1:=Einwohner 2:=konnten 3:=ihre 4:=Lebensmittel 5:=ganz 6:=normal 7:=kaufen.|1||No spans for sentences with one statement|
|0:=Die 1:=Mitarbeiter 2:=reparieren 3:=gemeinsam 4:=kaputte 5:=Dinge.|2|[[3],[4,5]]|We identified two statements in this sentence (`0:=Die 1:=Mitarbeiter 2:=reparieren 3:=gemeinsam.` and `0:=Die 1:=Mitarbeiter 2:=reparieren 4:=kaputte 5:=Dinge.`). The tokens 2 and 3 (Mitarbeiter reparieren) are contained in both statements, so we don't include them in the annotations. The tokens 3 (gemeinsam) and 4,5 (kaputte Dinge) are independant, and hence, form the two statement spans.|
