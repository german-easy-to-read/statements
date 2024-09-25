# Statement Segmentation in German Easy Language (StaGE)
## About
German Easy Language (Leichte Sprache) is a controlled, simple language for which there have been several guidelines in the past. The draft of DIN SPEC 33429 has the potential to become the authoritative guideline. It describes several characteristics of German Easy language. Two of these are the number of statements and to format enumerations as lists. We have, therefore, segmented Easy Language sentences and annotated how well these aspects of DIN SPEC 33429 are implemented in web texts in German Easy language. 

With this shared task, we want to analyze both the number and the segments of the statements and automate this annotation. According to our definition, a statement contains only obligatory additions and no optional (omissible) additions following the concept of verb valency.
Example: 
`"Das Glas steht heute Abend auf dem Tisch." (engl.: "The glass is on the table tonight.", literally: "the glass stands today evening on the table.") (Local adverbial: auf dem Tisch; temporal adverbial: heute Abend). `
In this example, the local adverbial is obligatory because `"stehen" (eng: "standing")` requires a place. The temporal adverbial is not obligatory and thus forms a new statement. Therefore, this example contains two statements.

Our aim is to analyze and evaluate existing German Easy language texts. We do not want to enforce the use of one-statement sentences but merely analyze the density of statements. One target group is German Easy language authors who can check their own texts automatically. These annotations can also serve as a data basis for machine learning applications in the field of readability analysis and fact checking.

## License
The theme is available as open source under the terms of the [MIT License](https://github.com/alshedivat/al-folio/blob/master/LICENSE).

The draft proceedings are available at [draft.pdf](./draft.pdf) and licensed as stated by [ACL](https://aclanthology.org/faq/copyright/): *to the general public under a liberal usage policy that allows unlimited reproduction, distribution and hosting of materials on any other website or medium, for non-commercial purposes.*

Everything else falls under [CC BY-SA 3.0 DEED](https://creativecommons.org/licenses/by-sa/3.0)

## Cite Us
```tex
@inproceedings{schomacker-etal-2024-overview,
    title = "Overview of the {G}erm{E}val 2024 Shared Task on Statement Segmentation in {G}erman Easy Language ({S}ta{GE})",
    author = {Schomacker, Thorben  and
      Ansch{\"u}tz, Miriam  and
      Stodden, Regina  and
      Groh, Georg  and
      Tropmann-Frick, Marina},
    editor = {Schomacker, Thorben  and
      Ansch{\"u}tz, Miriam  and
      Stodden, Regina},
    booktitle = "Proceedings of GermEval 2024 Shared Task on Statement Segmentation in German Easy Language (StaGE)",
    month = sep,
    year = "2024",
    address = "Vienna, Austria",
    publisher = "Association for Computational Lingustics",
    url = "https://aclanthology.org/2024.germeval-1.1",
    pages = "1--14",
}
```

The complete proceedings of the Shared Task are available at: [https://aclanthology.org/volumes/2024.germeval-1/](https://aclanthology.org/volumes/2024.germeval-1/)