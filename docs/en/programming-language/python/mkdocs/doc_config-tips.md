# Document Config Tips

!!! tip

    - The configuration of documents is specified in `nav` of `mkdocs.yml`.
    - When `nav` is set, a list of documents will be displayed on the left side of the screen.
    - Based on the following `nav` setting, it will be easy to manage the configuration suitable for adding and changing documents.

```yaml title="mkdocs.yaml"
nav: # (1)!
  - Home: index.md # (2)!
  - Programming language:
      - ja/programming-language/index.md # (3)!
      - Python:
      - ja/programming-language/python/index.md # (4)!
          - Mkdocs tips:
              - ja/programming-language/python/mkdocs/index.md # (5)!
              - ja/programming-language/python/mkdocs/display-config_tips.md # (6)!
```

1. Set `index.md` as the link destination when `- navigation.indexes` setting is enabled
2. Initial page
3. Initial page in the Programming language section
4. Initial page in the Python section
5. ・Initial page of Mkdocs tips<br/>
   ・The notation `Page1: ja/programming-language/python/mkdocs/index.md` is also possible.<br/>
   ・If not explicitly displayed, the content of the "h1" tag is displayed.
6. Accessible by setting up a link in a subsection or in `index.md

## nav display settings

!!! tip

    For configurations with multiple documents, the following settings are sufficient

```yaml title="mkdocs.yaml"
theme:
  features:
    # Enable link setting on section
    - navigation.indexes
    # Back-to-top button
    - navigation.top
    # groups in the sidebar
    #- navigation.sections
    # expand all collapsible subsections
    #- navigation.expand
```
