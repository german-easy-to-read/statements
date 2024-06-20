---
layout: default
permalink: /faq/
title: frequently asked questions
description: faqs
nav: true
nav_order: 20
---

# Frequently asked questions


## Can I only participate in Subtask 1 (Identifying Number of Statements)?
Yes, you can participate in both subtasks or only in Subtask 1. If you only want to participate in Subtask 1, please add an empty statement_spans column to your prediction file. In this case, the statement spans will be considered as null.

## Can I only participate in Subtask 2 (Identifying Segments of Statements)?
No, Subtask 2 is dependent on Subtask 1. You cannot only participate in Subtask 2. But, it is possible to submit your results only to Subtask 1.

## What tools are allowed to solve the task?
  All technological solutions are welcome. To foster scientific reproducibility, we encourage you to use open-source software and data solutions whenever possible. Nevertheless, we don't prohibit using any tool, software, or model.

## Why do you split sentences like `Eine Angel ist eine Schnur mit einem Haken` into two statements?
  Our statements focus mostly on chunks of information that need to be understood by the readers. From a content perspective, a fishing rod always consists of a string and a hook, so splitting these into two statements makes no sense. However, the reader still has to parse two separate statements independently: 1) there is a string, and 2) there is a hook. Therefore, we decided to split the sentence into two statements.

## How did you annotate your data?
  We tried to describe our process in detail in our [Annotation Guidelines](https://german-easy-to-read.github.io/statements/annotations)

## Why are there empty tokens? Can we delete them?
  The data from the Hurraki homepage is quite noisy. We decided to keep the noise to reflect upon noisy real-world data. These empty tokens are not annotated in the statement spans. So, you can, of course, remove them in your (pre-)processing. However, make sure that the span annotations still use the original numbering.
