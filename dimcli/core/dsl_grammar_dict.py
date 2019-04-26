#!/usr/bin/python
# -*- coding: utf-8 -*-



#
#
# SYNTAX_DICT is a dictionary representation of operators and other constants of the DSL language 
#
#

SYNTAX_DICT = {
    'allowed_starts': {
        'help' : [],
        'quit' : [],
        'show' : [ 'json_compact'],
        'export_html' : [],
        'export_csv' : [],
        'search': [],
        'describe': [ 'version', 'source', 'entity', 'schema'],
        'check_researcher_ids': [],
        'classify': [],
        'extract_grants': [],
        'extract_terms': [],
    },
    'allowed_starts_dsl_query': ['search' ,'describe', 'check_researcher_ids', 'classify', 'extract_grants', 'extract_terms'],
    'dimensions_urls' : {
        'publications' : 'https://app.dimensions.ai/details/publication/',
        'grants' : 'https://app.dimensions.ai/details/grant/',
        'patents' : 'https://app.dimensions.ai/details/patent/',
        'policy_documents' : 'https://app.dimensions.ai/details/clinical_trial/',
        'clinical_trials' : 'https://app.dimensions.ai/details/policy_documents/',
        'researchers' : 'https://app.dimensions.ai/discover/publication?and_facet_researcher=',
    },
    'lang_all': [
        'search',
        'return',
        'for',
        'where',
        'in',
        'limit',
        'skip',
        'aggregate',
        '=',  # filter operators https://docs.dimensions.ai/dsl/language.html#simple-filters
        '!=',
        '>',
        '<',
        '>=',
        '<=',
        '~',
        'is empty',
        'is not empty',
        "count", # https://docs.dimensions.ai/dsl/language.html#filter-functions
        'sort by',
        'asc',
        'desc',
        "AND", # boolean operators https://docs.dimensions.ai/dsl/language.html#id6
        "OR", 
        "NOT",
        "&&",
        "!",
        "||",
        "+",
        "-",
    ],
    'lang_after_search' : ['in', 'where', 'for', 'return'],
    'lang_after_filter' : ['and', 'or', 'not', 'return', ],
    'lang_after_for_text' : ['and', 'or', 'not', 'return', 'where' ],
    'lang_after_return' : ['sort by', 'asc', 'desc', 'aggregate', 'limit', 'skip' ],
    'lang_filter_operators' : ['=', '!=', '>', '<', '>=', '<=', '~', 'is empty', 'is not empty'],
    'lang_text_operators' : ['AND', 'OR', 'NOT', '&&', '!', '||', '+', '-', '?', '*', '~'],
}


#
# GRAMMAR_DICT is a dictionary rendering of the DSL grammar JSON
# which can be obtained with the query `describe schema`
#
# last updated: v1.16 2019-04-26
# how to create:
#
# In [1]: import dimcli
# In [2]: dsl = dimcli.Dsl()
# In [3]: res = dsl.query("describe schema")
# In [4]: res.json()
#
# then save the results in GRAMMAR_DICT symbol
#
#

GRAMMAR_DICT = {
    'sources': {
        'publications': {
            'fields': {
                'volume': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'pmid': {
                    'type': 'identifier',
                    'description': 'PubMed ID',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'research_org_state_names': {
                    'type': 'string',
                    'description': 'GeoNames state name',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'issn': {
                    'type': 'string',
                    'description': 'International Standard Serial Number',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'research_org_state_codes': {
                    'type': 'states',
                    'description': 'ISO\u200c-3166-2 code and name',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'times_cited': {
                    'type':
                    'count',
                    'description':
                    'Number of citations. Does not support emptiness filters',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'research_orgs': {
                    'type':
                    'orgs',
                    'description':
                    'Note: this field supports :ref:`filter-functions`: ``count``',
                    'long_description':
                    None,
                    'is_entity':
                    True,
                    'is_filter':
                    True,
                    'is_facet':
                    True
                },
                'type': {
                    'type':
                    'string',
                    'description':
                    'Publication type (article, chapter, proceeding, monograph, preprint or book)',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'supporting_grant_ids': {
                    'type': 'identifier',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'altmetric': {
                    'type':
                    'float',
                    'description':
                    'Altmetric attention score. Does not support emptiness filters',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'HRCS_HC': {
                    'type': 'categories',
                    'description': 'HRCS - Health Categories',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'relative_citation_ratio': {
                    'type':
                    'float',
                    'description':
                    'Relative citation performance of an article when compared to others in its area of research. Does not support emptiness filters',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'RCDC': {
                    'type':
                    'categories',
                    'description':
                    'Research, Condition, and Disease Categorization',
                    'long_description':
                    None,
                    'is_entity':
                    True,
                    'is_filter':
                    True,
                    'is_facet':
                    True
                },
                'field_citation_ratio': {
                    'type':
                    'float',
                    'description':
                    'Relative citation performance of article when compared to similarly aged articles in its area of research. Does not support emptiness filters',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'funders': {
                    'type': 'orgs',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'book_series_title': {
                    'type': 'text',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'year': {
                    'type': 'integer',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'book_title': {
                    'type': 'text',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'linkout': {
                    'type': 'text',
                    'description': 'URL address',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'FOR_first': {
                    'type': 'categories',
                    'description': 'Division level FOR',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'references': {
                    'type':
                    'identifier',
                    'description':
                    'Dimensions publication id for documents referencing another document',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'pmcid': {
                    'type': 'identifier',
                    'description': 'PubMed Central ID',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'researchers': {
                    'type':
                    'researchers',
                    'description':
                    'Note: this field supports :ref:`filter-functions`: ``count``',
                    'long_description':
                    None,
                    'is_entity':
                    True,
                    'is_filter':
                    True,
                    'is_facet':
                    True
                },
                'proceedings_title': {
                    'type':
                    'text',
                    'description':
                    'Title of a conference corresponding to documents that are `type` of "proceeding"',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    False,
                    'is_facet':
                    False
                },
                'date_inserted': {
                    'type':
                    'timestamp',
                    'description':
                    'Date when publication was inserted into Dimensions',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'journal': {
                    'type': 'journals',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'issue': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'publisher': {
                    'type': 'label',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'title': {
                    'type': 'text',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'date': {
                    'type': 'date',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'book_doi': {
                    'type': 'identifier',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'HRCS_RAC': {
                    'type': 'categories',
                    'description': 'HRCS – Research Activity Codes',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'doi': {
                    'type': 'identifier',
                    'description': 'Digital object identifier',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'open_access': {
                    'type':
                    'string',
                    'description':
                    'Open Access status for publication. Deprecated in favor of `open_access_categories`',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'recent_citations': {
                    'type':
                    'integer',
                    'description':
                    'Number of citations received in the last two years. Does not support emptiness filters',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'author_affiliations': {
                    'type':
                    'json',
                    'description':
                    "List of JSON lists of researchers' first and last names and affiliations",
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    False,
                    'is_facet':
                    False
                },
                'research_org_cities': {
                    'type': 'cities',
                    'description': 'GeoNames id and name',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'altmetric_id': {
                    'type': 'integer',
                    'description': 'AltMetric Publication ID',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'journal_lists': {
                    'type':
                    'string',
                    'description':
                    'Independent grouping of journals outside of Dimensions',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'id': {
                    'type': 'identifier',
                    'description': 'Dimensions publication id',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'terms': {
                    'type':
                    'text',
                    'description':
                    'Extracted terms. See :ref:`for-terms` regarding searching terms vs phrases',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    False,
                    'is_facet':
                    False
                },
                'funder_countries': {
                    'type': 'countries',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'research_org_countries': {
                    'type':
                    'countries',
                    'description':
                    'Note: this field supports :ref:`filter-functions`: ``count``',
                    'long_description':
                    None,
                    'is_entity':
                    True,
                    'is_filter':
                    True,
                    'is_facet':
                    True
                },
                'mesh_terms': {
                    'type':
                    'label',
                    'description':
                    'Medical Subject Heading terms as used in PubMed.',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    True
                },
                'pages': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'open_access_categories': {
                    'type':
                    'open_access',
                    'description':
                    'Open Access category for publication. Filtering on values is case sensitive.',
                    'long_description':
                    'Open Access category data for publications values:\n\n        * `oa_all`: Article is freely available\n        * `gold_pure`: Version Of Record (VOR) is free under an open licence from a full OA journal\n        * `gold_hybrid`: Version Of Record (VOR) is free under an open licence in a paid-access journal\n        * `gold_bronze`: Freely available on publisher page, but without an open licence\n        * `green_pub`: Free copy of published version in an OA repository\n        * `green_acc`: Free copy of accepted version in an OA repository\n        * `green_sub`: Free copy of submitted version, or where version is unknown, in an OA repository\n        * `closed`: No freely available copy has been identified',
                    'is_entity':
                    True,
                    'is_filter':
                    True,
                    'is_facet':
                    True
                },
                'research_org_country_names': {
                    'type': 'string',
                    'description': 'GeoNames country name',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'FOR': {
                    'type': 'categories',
                    'description': 'ANZSRC Fields of Research classification',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                }
            },
            'fieldsets': ['all', 'basics', 'extras', 'book'],
            'metrics': {
                'count': {
                    'name': 'count',
                    'description': 'Total count'
                },
                'altmetric_median': {
                    'name': 'altmetric_median',
                    'description': 'Median Altmetric attention score'
                },
                'citations_total': {
                    'name': 'citations_total',
                    'description': 'Aggregated number of citations'
                },
                'citations_avg': {
                    'name': 'citations_avg',
                    'description': 'Arithmetic mean of citations'
                },
                'citations_median': {
                    'name': 'citations_median',
                    'description': 'Median of citations'
                },
                'recent_citations_total': {
                    'name':
                    'recent_citations_total',
                    'description':
                    'For a given article, in a given year, the number of citations accrued in the last two year period. Single value stored per document, year window rolls over in July.'
                },
                'rcr_avg': {
                    'name': 'rcr_avg',
                    'description':
                    'Arithmetic mean of `relative_citation_ratio`'
                },
                'fcr_gavg': {
                    'name': 'fcr_gavg',
                    'description': 'Geometric mean of `field_citation_ratio`'
                }
            },
            'search_fields': [
                'noun_phrases', 'authors', 'title_only', 'title_abstract_only',
                'full_data', 'terms_experimental', 'terms', 'researchers'
            ]
        },
        'grants': {
            'fields': {
                'start_year': {
                    'type': 'integer',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'research_org_state_codes': {
                    'type': 'states',
                    'description': 'ISO\u200c-3166-2 code and name',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'research_orgs': {
                    'type': 'orgs',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'funding_gbp': {
                    'type': 'financial',
                    'description': 'Funding amount awarded in GBP',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'original_title': {
                    'type': 'text',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'active_year': {
                    'type': 'integer',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'start_date': {
                    'type': 'timestamp',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'funding_nzd': {
                    'type': 'financial',
                    'description': 'Funding amount awarded in NZD',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'HRCS_HC': {
                    'type': 'categories',
                    'description': 'HRCS - Health Categories',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'funding_usd': {
                    'type': 'financial',
                    'description': 'Funding amount awarded in USD',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'RCDC': {
                    'type':
                    'categories',
                    'description':
                    'Research, Condition, and Disease Categorization',
                    'long_description':
                    None,
                    'is_entity':
                    True,
                    'is_filter':
                    True,
                    'is_facet':
                    True
                },
                'funders': {
                    'type': 'orgs',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'funding_currency': {
                    'type': 'label',
                    'description': 'Original funding currency',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'abstract': {
                    'type': 'text',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'researcher_details': {
                    'type':
                    'json',
                    'description':
                    'Additional details about researchers including affiliations and role',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    False,
                    'is_facet':
                    False
                },
                'title_language': {
                    'type': 'label',
                    'description': 'ISO 639-1 language code used in title',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'linkout': {
                    'type': 'text',
                    'description': 'URL linked to grant',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'funding_jpy': {
                    'type': 'financial',
                    'description': 'Funding amount awarded in JPY',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'FOR_first': {
                    'type': 'categories',
                    'description': 'Division level FOR',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'funding_org_acronym': {
                    'type': 'label',
                    'description': 'Acronym for funding organisation',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'funding_org_city': {
                    'type': 'label',
                    'description': 'City name for funding organisation',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'funding_org_name': {
                    'type': 'label',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'researchers': {
                    'type': 'researchers',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'date_inserted': {
                    'type':
                    'timestamp',
                    'description':
                    'Date when publication was inserted into Dimensions',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'funding_cad': {
                    'type': 'financial',
                    'description': 'Funding amount awarded in CAD',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'title': {
                    'type': 'text',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'HRCS_RAC': {
                    'type': 'categories',
                    'description': 'HRCS – Research Activity Codes',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'funding_chf': {
                    'type': 'financial',
                    'description': 'Funding amount awarded in CHF',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'resulting_publication_ids': {
                    'type':
                    'identifier',
                    'description':
                    'Resulting Publication IDs. Deprecated, use `publications` field `supporting_grant_ids` instead',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'project_num': {
                    'type': 'identifier',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'funding_eur': {
                    'type': 'financial',
                    'description': 'Funding amount awarded in EUR',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'research_org_cities': {
                    'type': 'cities',
                    'description': 'GeoNames id and name',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'end_date': {
                    'type': 'timestamp',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'funding_aud': {
                    'type': 'financial',
                    'description': 'Funding amount awarded in AUD',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'research_org_name': {
                    'type': 'label',
                    'description': 'Name for research organisation',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'id': {
                    'type': 'identifier',
                    'description': 'Dimensions grant id',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'research_org_countries': {
                    'type': 'countries',
                    'description': 'GeoNames code and name',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'funder_countries': {
                    'type': 'countries',
                    'description': 'GeoNames code and name',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'language': {
                    'type': 'label',
                    'description': 'ISO 639-1 language codes',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'FOR': {
                    'type': 'categories',
                    'description': 'ANZSRC Fields of Research classification',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                }
            },
            'fieldsets': ['all', 'basics', 'extras'],
            'metrics': {
                'count': {
                    'name': 'count',
                    'description': 'Total count'
                },
                'funding': {
                    'name': 'funding',
                    'description': None
                }
            },
            'search_fields':
            ['full_data', 'researchers', 'title_only', 'title_abstract_only']
        },
        'patents': {
            'fields': {
                'ipcr': {
                    'type':
                    'identifier',
                    'description':
                    'International Patent Classification Reform number for a patent',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'filed_year': {
                    'type': 'integer',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'times_cited': {
                    'type': 'count',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'reference_ids': {
                    'type': 'identifier',
                    'description': 'Patents which are cited by this patent',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'additional_filters': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'HRCS_HC': {
                    'type': 'categories',
                    'description': 'HRCS - Health Categories',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'cited_by_ids': {
                    'type': 'identifier',
                    'description': 'Patents which cite this patent',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'RCDC': {
                    'type':
                    'categories',
                    'description':
                    'Research, Condition, and Disease Categorization',
                    'long_description':
                    None,
                    'is_entity':
                    True,
                    'is_filter':
                    True,
                    'is_facet':
                    True
                },
                'funders': {
                    'type': 'orgs',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'year': {
                    'type': 'integer',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'cpc': {
                    'type':
                    'identifier',
                    'description':
                    'Cooperative Patent Classification number for a patent',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'abstract': {
                    'type': 'text',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'granted_year': {
                    'type': 'integer',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'legal_status': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'inventor_names': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'FOR_first': {
                    'type': 'categories',
                    'description': 'Division level FOR',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'assignees': {
                    'type': 'orgs',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'date_inserted': {
                    'type':
                    'timestamp',
                    'description':
                    'Date when publication was inserted into Dimensions',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'original_assignee_names': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'filing_status': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'publication_date': {
                    'type': 'timestamp',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'title': {
                    'type': 'text',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'date': {
                    'type': 'timestamp',
                    'description': 'Date when the patent was filed',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'filed_date': {
                    'type': 'timestamp',
                    'description': 'Deprecated in favor of `filed_date`',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'original_assignees': {
                    'type': 'orgs',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'funder_groups': {
                    'type': 'org_groups',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'HRCS_RAC': {
                    'type': 'categories',
                    'description': 'HRCS – Research Activity Codes',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'status': {
                    'type': 'string',
                    'description': 'Deprecated in favor of `legal_status`',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'jurisdiction': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'priority_date': {
                    'type': 'timestamp',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'current_assignee_names': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'assignee_state_names': {
                    'type': 'label',
                    'description': 'GeoNames name',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'current_assignees': {
                    'type': 'orgs',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'assignee_state_codes': {
                    'type': 'states',
                    'description': 'GeoNames code and name',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'assignee_countries': {
                    'type': 'countries',
                    'description': 'GeoNames code and name',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'assignee_cities': {
                    'type': 'cities',
                    'description': 'GeoNames id and name',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'id': {
                    'type': 'identifier',
                    'description': 'Dimensions patent id',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'expiration_date': {
                    'type': 'timestamp',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'publication_ids': {
                    'type': 'identifier',
                    'description': 'Related publication IDs',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'assignee_names': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'associated_grant_ids': {
                    'type': 'identifier',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'FOR': {
                    'type': 'categories',
                    'description': 'ANZSRC Fields of Research classification',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                }
            },
            'fieldsets': ['all', 'basics', 'extras'],
            'metrics': {
                'count': {
                    'name': 'count',
                    'description': 'Total count'
                }
            },
            'search_fields':
            ['full_data', 'title_only', 'title_abstract_only']
        },
        'clinical_trials': {
            'fields': {
                'active_years': {
                    'type': 'integer',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'HRCS_HC': {
                    'type': 'categories',
                    'description': 'HRCS - Health Categories',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'conditions': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'RCDC': {
                    'type':
                    'categories',
                    'description':
                    'Research, Condition, and Disease Categorization',
                    'long_description':
                    None,
                    'is_entity':
                    True,
                    'is_filter':
                    True,
                    'is_facet':
                    True
                },
                'funders': {
                    'type': 'orgs',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'organizations': {
                    'type':
                    'orgs',
                    'description':
                    'IDs of any organizations involved in any way, e.g. as sponsors or collaborators',
                    'long_description':
                    None,
                    'is_entity':
                    True,
                    'is_filter':
                    True,
                    'is_facet':
                    True
                },
                'abstract': {
                    'type': 'text',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'linkout': {
                    'type': 'text',
                    'description': 'URL linked to clinical trial',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'gender': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'FOR_first': {
                    'type': 'categories',
                    'description': 'Division level FOR',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'phase': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'date_inserted': {
                    'type':
                    'timestamp',
                    'description':
                    'Date when publication was inserted into Dimensions',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'investigators': {
                    'type':
                    'json',
                    'description':
                    'JSON with names, titles, & roles (no ids) of involved researchers for display purposes',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    False,
                    'is_facet':
                    False
                },
                'date': {
                    'type': 'timestamp',
                    'description': 'Start date of a clinical trial',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'title': {
                    'type': 'text',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'funder_groups': {
                    'type': 'org_groups',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'HRCS_RAC': {
                    'type': 'categories',
                    'description': 'HRCS – Research Activity Codes',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'registry': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'id': {
                    'type': 'identifier',
                    'description': 'Dimensions clinical trial id',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'funder_countries': {
                    'type': 'countries',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'publication_ids': {
                    'type': 'identifier',
                    'description': 'Linked Publication IDs',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'associated_grant_ids': {
                    'type': 'identifier',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'FOR': {
                    'type': 'categories',
                    'description': 'ANZSRC Fields of Research classification',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                }
            },
            'fieldsets': ['all', 'basics', 'extras'],
            'metrics': {
                'count': {
                    'name': 'count',
                    'description': 'Total count'
                }
            },
            'search_fields':
            ['full_data', 'researchers', 'title_only', 'title_abstract_only']
        },
        'policy_documents': {
            'fields': {
                'year': {
                    'type': 'integer',
                    'description': 'Policy posted on year',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'health_research_areas': {
                    'type': 'categories',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'linkout': {
                    'type': 'text',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'HRCS_HC': {
                    'type': 'categories',
                    'description': 'HRCS - Health Categories',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'RCDC': {
                    'type':
                    'categories',
                    'description':
                    'Research, Condition, and Disease Categorization',
                    'long_description':
                    None,
                    'is_entity':
                    True,
                    'is_filter':
                    True,
                    'is_facet':
                    True
                },
                'broad_research_areas': {
                    'type': 'categories',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'title': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'id': {
                    'type': 'identifier',
                    'description': 'Dimensions policy document id',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'grid_id': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'FOR_first': {
                    'type': 'categories',
                    'description': 'Division level FOR',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'HRCS_RAC': {
                    'type': 'categories',
                    'description': 'HRCS – Research Activity Codes',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'city': {
                    'type': 'cities',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'country': {
                    'type': 'countries',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'publication_ids': {
                    'type': 'identifier',
                    'description': 'Referenced Publication IDs',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'date_inserted': {
                    'type':
                    'date',
                    'description':
                    'Date when policy document was inserted into Dimensions',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'state': {
                    'type': 'states',
                    'description': None,
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'FOR': {
                    'type': 'categories',
                    'description': 'ANZSRC Fields of Research classification',
                    'long_description': None,
                    'is_entity': True,
                    'is_filter': True,
                    'is_facet': True
                },
                'source_name': {
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                }
            },
            'fieldsets': ['all', 'basics', 'categories'],
            'metrics': {
                'count': {
                    'name': 'count',
                    'description': 'Total count'
                }
            },
            'search_fields': ['full_data', 'title_only']
        },
        'researchers': {
            'fields': {
                'total_publications': {
                    'type': 'integer',
                    'description': 'Total publications count',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'last_grant_year': {
                    'type': 'integer',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'first_name': {
                    'type': 'string',
                    'description': 'First Name',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'last_publication_year': {
                    'type': 'integer',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'total_grants': {
                    'type': 'integer',
                    'description': 'Total grants count',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'first_grant_year': {
                    'type': 'integer',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'research_orgs': {
                    'type':
                    'orgs',
                    'description':
                    'All research organizations linked to the researcher',
                    'long_description':
                    None,
                    'is_entity':
                    True,
                    'is_filter':
                    True,
                    'is_facet':
                    True
                },
                'id': {
                    'type': 'identifier',
                    'description': 'Dimensions researcher id',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'current_research_org': {
                    'type':
                    'orgs',
                    'description':
                    'The most recent research organization linked to the researcher',
                    'long_description':
                    None,
                    'is_entity':
                    True,
                    'is_filter':
                    True,
                    'is_facet':
                    True
                },
                'last_name': {
                    'type': 'string',
                    'description': 'Last Name',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': False
                },
                'first_publication_year': {
                    'type': 'integer',
                    'description': None,
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': True,
                    'is_facet': True
                },
                'redirect': {
                    'type':
                    'identifier',
                    'description':
                    'Indicates status of obsolete researcher ID. Empty means that the researcher ID was deleted. Otherwise ID provided means that is the new id into which the obsolete one was redirected. If multiple values are available, it means that the original researcher ID was split into multiple IDs.',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                },
                'orcid_id': {
                    'type': 'text',
                    'description': '`ORCID <https://orcid.org/>`_ ID',
                    'long_description': None,
                    'is_entity': False,
                    'is_filter': False,
                    'is_facet': False
                },
                'obsolete': {
                    'type':
                    'integer',
                    'description':
                    'Indicates researcher ID status. 0 means that the researcher ID is still active, 1 means that the researcher ID is no longer valid. See redirect field for further information on invalid researcher IDs. Also see function ``check_researcher_ids`` in :ref:`supported-functions`.',
                    'long_description':
                    None,
                    'is_entity':
                    False,
                    'is_filter':
                    True,
                    'is_facet':
                    False
                }
            },
            'fieldsets': ['all', 'basics', 'extras'],
            'metrics': {
                'count': {
                    'name': 'count',
                    'description': 'Total count'
                }
            },
            'search_fields': ['researcher']
        }
    },
    'entities': {
        'categories': {
            'fields': {
                'id': {
                    'name': 'id',
                    'type': 'string',
                    'description': 'Dimensions category id',
                    'long_description': None,
                    'is_filter': True
                },
                'name': {
                    'name': 'name',
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_filter': True
                }
            },
            'fieldsets': ['all', 'basics']
        },
        'cities': {
            'fields': {
                'id': {
                    'name': 'id',
                    'type': 'identifier',
                    'description': 'Dimensions city id',
                    'long_description': None,
                    'is_filter': True
                },
                'name': {
                    'name': 'name',
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_filter': True
                }
            },
            'fieldsets': ['all', 'basics']
        },
        'countries': {
            'fields': {
                'id': {
                    'name': 'id',
                    'type': 'string',
                    'description': 'Dimensions city id',
                    'long_description': None,
                    'is_filter': True
                },
                'name': {
                    'name': 'name',
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_filter': True
                }
            },
            'fieldsets': ['all', 'basics']
        },
        'journals': {
            'fields': {
                'id': {
                    'name': 'id',
                    'type': 'string',
                    'description': 'Dimensions journal id',
                    'long_description': None,
                    'is_filter': True
                },
                'title': {
                    'name': 'title',
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_filter': True
                }
            },
            'fieldsets': ['all', 'basics']
        },
        'org_groups': {
            'fields': {
                'id': {
                    'name': 'id',
                    'type': 'identifier',
                    'description': 'Dimensions organization group id',
                    'long_description': None,
                    'is_filter': True
                },
                'name': {
                    'name': 'name',
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_filter': True
                }
            },
            'fieldsets': ['all', 'basics']
        },
        'orgs': {
            'fields': {
                'id': {
                    'name': 'id',
                    'type': 'identifier',
                    'description': 'Dimensions organization id',
                    'long_description': None,
                    'is_filter': True
                },
                'name': {
                    'name': 'name',
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_filter': True
                },
                'acronym': {
                    'name': 'acronym',
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_filter': True
                },
                'country_name': {
                    'name': 'country_name',
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_filter': True
                }
            },
            'fieldsets': ['all', 'basics']
        },
        'states': {
            'fields': {
                'id': {
                    'name': 'id',
                    'type': 'identifier',
                    'description': 'Dimensions state id',
                    'long_description': None,
                    'is_filter': True
                },
                'name': {
                    'name': 'name',
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_filter': True
                }
            },
            'fieldsets': ['all', 'basics']
        },
        'publications_entity': {
            'fields': {
                'id': {
                    'name': 'id',
                    'type': 'identifier',
                    'description': 'Dimensions publication id',
                    'long_description': None,
                    'is_filter': True
                },
                'doi': {
                    'name': 'doi',
                    'type': 'identifier',
                    'description': 'Digital object identifier',
                    'long_description': None,
                    'is_filter': True
                },
                'pmid': {
                    'name': 'pmid',
                    'type': 'identifier',
                    'description': 'PubMed ID',
                    'long_description': None,
                    'is_filter': True
                },
                'pmcid': {
                    'name': 'pmcid',
                    'type': 'identifier',
                    'description': 'PubMed Central ID',
                    'long_description': None,
                    'is_filter': True
                }
            },
            'fieldsets': ['all', 'basics']
        },
        'open_access': {
            'fields': {
                'id': {
                    'name': 'id',
                    'type': 'identifier',
                    'description': None,
                    'long_description': None,
                    'is_filter': True
                },
                'name': {
                    'name': 'name',
                    'type': 'string',
                    'description': None,
                    'long_description': None,
                    'is_filter': True
                },
                'description': {
                    'name': 'description',
                    'type': 'text',
                    'description': None,
                    'long_description': None,
                    'is_filter': False
                }
            },
            'fieldsets': ['all', 'basics']
        }
    }
}

