---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
classes: wide
sidebar:
   - title: "ENCOPIA"
     text: "ENabling COnnected PrIvacy Assurance"

---

<div class="publications-list">
  <h2>Publications</h2>
  <ol>
    {% assign publications = site.data.bib.publications %}
    {% for publication in publications %}
      <li>
        <p>
          {% assign authors = publication.author | split: ' and ' %}
          {% for author in authors %}
            {% assign authorNames = author | split: ', ' %}
            {% if authorNames.size > 1 %}
              {% assign lastName = authorNames[0] %}
              {% assign firstInitial = authorNames[1] | slice: 0 %}
              {% if forloop.last %}
                {{ lastName }} {{ firstInitial }}.
              {% else %}
                {{ lastName }} {{ firstInitial }}.,
              {% endif %}
            {% else %}
              {{ author }},
            {% endif %}
          {% endfor %}
          ({% if publication.year %}{{ publication.year }}{% endif %})
          {% if publication.title %}
            {% if publication.year %}. {% endif %}
            <strong>{{ publication.title }}</strong>.
          {% endif %}
          {% if publication.journal %}
            {{ publication.journal }},
          {% endif %}
          {% if publication.booktitle %}
            {{ publication.booktitle }},
          {% endif %}
          {% if publication.volume %}
            {{ publication.volume }},
          {% endif %}
          {% if publication.pages %}
            {{ publication.pages }}
          {% endif %}
          {% if publication.doi %}
            <a href="https://doi.org/{{ publication.doi }}" target="_blank">DOI: {{ publication.doi | remove: ' ' }}</a>
          {% endif %}
        </p>
      </li>
    {% endfor %}
  </ol>
  
  <h2>Talks</h2>
  <ol>
    <li>
      <p>Marco Casagrande & Daniele Antonioli*: BreakMi: Reversing, Exploiting and Fixing Xiaomi (and Fitbit) Fitness Tracking Ecosystems, [hardwear.io USA](https://hardwear.io/usa-2023/speakers/marco-and-daniele.php), 2023.</p>
    </li>
  </ol>
  
  <h2>Previous Work</h2>
  <ol>
    {% assign publications = site.data.bib.previous_work %}
    {% for publication in publications %}
      <li>
        <p>
          {% assign authors = publication.author | split: ' and ' %}
          {% for author in authors %}
            {% assign authorNames = author | split: ', ' %}
            {% if authorNames.size > 1 %}
              {% assign lastName = authorNames[0] %}
              {% assign firstInitial = authorNames[1] | slice: 0 %}
              {% if forloop.last %}
                {{ lastName }} {{ firstInitial }}.
              {% else %}
                {{ lastName }} {{ firstInitial }}.,
              {% endif %}
            {% else %}
              {{ author }},
            {% endif %}
          {% endfor %}
          ({% if publication.year %}{{ publication.year }}{% endif %})
          {% if publication.title %}
            {% if publication.year %}. {% endif %}
            <strong>{{ publication.title }}</strong>.
          {% endif %}
          {% if publication.journal %}
            {{ publication.journal }},
          {% endif %}
          {% if publication.booktitle %}
            {{ publication.booktitle }},
          {% endif %}
          {% if publication.volume %}
            {{ publication.volume }},
          {% endif %}
          {% if publication.pages %}
            {{ publication.pages }}
          {% endif %}
          {% if publication.doi %}
            <a href="https://doi.org/{{ publication.doi }}" target="_blank">DOI: {{ publication.doi | remove: ' ' }}</a>
          {% endif %}
        </p>
      </li>
    {% endfor %}
  </ol>
</div>
