---
layout: default
permalink: /data/
title: data
description: data
nav: true
nav_order: 3
---


We published an initial trial dataset. Feel free to explore the data.


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
