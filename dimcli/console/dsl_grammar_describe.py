DESCRIBE_OUTPUT = {
    "entities": {
        "categories": {
            "fields": {
                "id": {
                    "description": "Dimensions category id",
                    "is_filter": true,
                    "long_description": null,
                    "name": "id",
                    "type": "string"
                },
                "name": {
                    "description": null,
                    "is_filter": true,
                    "long_description": null,
                    "name": "name",
                    "type": "string"
                }
            },
            "fieldsets": [
                "all",
                "basics"
            ]
        },
        "cities": {
            "fields": {
                "id": {
                    "description": "Dimensions city id",
                    "is_filter": true,
                    "long_description": null,
                    "name": "id",
                    "type": "identifier"
                },
                "name": {
                    "description": null,
                    "is_filter": true,
                    "long_description": null,
                    "name": "name",
                    "type": "string"
                }
            },
            "fieldsets": [
                "all",
                "basics"
            ]
        },
        "countries": {
            "fields": {
                "id": {
                    "description": "Dimensions city id",
                    "is_filter": true,
                    "long_description": null,
                    "name": "id",
                    "type": "string"
                },
                "name": {
                    "description": null,
                    "is_filter": true,
                    "long_description": null,
                    "name": "name",
                    "type": "string"
                }
            },
            "fieldsets": [
                "all",
                "basics"
            ]
        },
        "journals": {
            "fields": {
                "id": {
                    "description": "Dimensions journal id",
                    "is_filter": true,
                    "long_description": null,
                    "name": "id",
                    "type": "string"
                },
                "title": {
                    "description": null,
                    "is_filter": true,
                    "long_description": null,
                    "name": "title",
                    "type": "string"
                }
            },
            "fieldsets": [
                "all",
                "basics"
            ]
        },
        "open_access": {
            "fields": {
                "description": {
                    "description": null,
                    "is_filter": false,
                    "long_description": null,
                    "name": "description",
                    "type": "text"
                },
                "id": {
                    "description": null,
                    "is_filter": true,
                    "long_description": null,
                    "name": "id",
                    "type": "identifier"
                },
                "name": {
                    "description": null,
                    "is_filter": true,
                    "long_description": null,
                    "name": "name",
                    "type": "string"
                }
            },
            "fieldsets": [
                "all",
                "basics"
            ]
        },
        "org_groups": {
            "fields": {
                "id": {
                    "description": "Dimensions organization group id",
                    "is_filter": true,
                    "long_description": null,
                    "name": "id",
                    "type": "identifier"
                },
                "name": {
                    "description": null,
                    "is_filter": true,
                    "long_description": null,
                    "name": "name",
                    "type": "string"
                }
            },
            "fieldsets": [
                "all",
                "basics"
            ]
        },
        "orgs": {
            "fields": {
                "acronym": {
                    "description": null,
                    "is_filter": true,
                    "long_description": null,
                    "name": "acronym",
                    "type": "string"
                },
                "country_name": {
                    "description": null,
                    "is_filter": true,
                    "long_description": null,
                    "name": "country_name",
                    "type": "string"
                },
                "id": {
                    "description": "Dimensions organization id",
                    "is_filter": true,
                    "long_description": null,
                    "name": "id",
                    "type": "identifier"
                },
                "name": {
                    "description": null,
                    "is_filter": true,
                    "long_description": null,
                    "name": "name",
                    "type": "string"
                }
            },
            "fieldsets": [
                "all",
                "basics"
            ]
        },
        "publications_entity": {
            "fields": {
                "doi": {
                    "description": "Digital object identifier",
                    "is_filter": true,
                    "long_description": null,
                    "name": "doi",
                    "type": "identifier"
                },
                "id": {
                    "description": "Dimensions publication id",
                    "is_filter": true,
                    "long_description": null,
                    "name": "id",
                    "type": "identifier"
                },
                "pmcid": {
                    "description": "PubMed Central ID",
                    "is_filter": true,
                    "long_description": null,
                    "name": "pmcid",
                    "type": "identifier"
                },
                "pmid": {
                    "description": "PubMed ID",
                    "is_filter": true,
                    "long_description": null,
                    "name": "pmid",
                    "type": "identifier"
                }
            },
            "fieldsets": [
                "all",
                "basics"
            ]
        },
        "states": {
            "fields": {
                "id": {
                    "description": "Dimensions state id",
                    "is_filter": true,
                    "long_description": null,
                    "name": "id",
                    "type": "identifier"
                },
                "name": {
                    "description": null,
                    "is_filter": true,
                    "long_description": null,
                    "name": "name",
                    "type": "string"
                }
            },
            "fieldsets": [
                "all",
                "basics"
            ]
        }
    },
    "sources": {
        "clinical_trials": {
            "facets": {
                "FOR": {
                    "description": "ANZSRC Fields of Research classification",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "FOR_first": {
                    "description": "Division level FOR",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_HC": {
                    "description": "HRCS - Health Categories",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_RAC": {
                    "description": "HRCS \u2013 Research Activity Codes",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "RCDC": {
                    "description": "Research, Condition, and Disease Categorization",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "active_years": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "funder_countries": {
                    "description": null,
                    "entity_type": "countries",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "countries"
                },
                "funder_groups": {
                    "description": null,
                    "entity_type": "org_groups",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "org_groups"
                },
                "funders": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "organizations": {
                    "description": "IDs of any organizations involved in any way, e.g. as sponsors or collaborators",
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                }
            },
            "fields": {
                "FOR": {
                    "description": "ANZSRC Fields of Research classification",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "FOR_first": {
                    "description": "Division level FOR",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_HC": {
                    "description": "HRCS - Health Categories",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_RAC": {
                    "description": "HRCS \u2013 Research Activity Codes",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "RCDC": {
                    "description": "Research, Condition, and Disease Categorization",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "abstract": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "active_years": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "associated_grant_ids": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "conditions": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "date": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "timestamp"
                },
                "date_inserted": {
                    "description": "Date when publication was inserted into Dimensions",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "timestamp"
                },
                "funder_countries": {
                    "description": null,
                    "entity_type": "countries",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "countries"
                },
                "funder_groups": {
                    "description": null,
                    "entity_type": "org_groups",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "org_groups"
                },
                "funders": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "gender": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "id": {
                    "description": "Dimensions clinical trial id",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "investigators": {
                    "description": "JSON with names, titles, & roles (no ids) of involved researchers for display purposes",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "json"
                },
                "linkout": {
                    "description": "URL linked to clinical trial",
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "organizations": {
                    "description": "IDs of any organizations involved in any way, e.g. as sponsors or collaborators",
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "phase": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "publication_ids": {
                    "description": "Linked Publication IDs",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "registry": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "title": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                }
            },
            "fieldsets": [
                "all",
                "basics",
                "extras"
            ],
            "metrics": {
                "count": {
                    "description": "Total count",
                    "name": "count"
                }
            },
            "search_fields": [
                "title_only",
                "title_abstract_only",
                "full_data",
                "researchers"
            ]
        },
        "grants": {
            "facets": {
                "FOR": {
                    "description": "ANZSRC Fields of Research classification",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "FOR_first": {
                    "description": "Division level FOR",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_HC": {
                    "description": "HRCS - Health Categories",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_RAC": {
                    "description": "HRCS \u2013 Research Activity Codes",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "RCDC": {
                    "description": "Research, Condition, and Disease Categorization",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "active_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "funder_countries": {
                    "description": "GeoNames code and name",
                    "entity_type": "countries",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "countries"
                },
                "funders": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "funding_org_acronym": {
                    "description": "Acronym for funding organisation",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "funding_org_city": {
                    "description": "City name for funding organisation",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "funding_org_name": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "language": {
                    "description": "ISO 639-1 language codes",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "research_org_cities": {
                    "description": "GeoNames id and name",
                    "entity_type": "cities",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "cities"
                },
                "research_org_countries": {
                    "description": "GeoNames code and name",
                    "entity_type": "countries",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "countries"
                },
                "research_org_name": {
                    "description": "Name for research organisation",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "research_org_state_codes": {
                    "description": "GeoNames code and name",
                    "entity_type": "states",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "states"
                },
                "research_orgs": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "researchers": {
                    "description": null,
                    "entity_type": "researchers",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "researchers"
                },
                "start_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "title_language": {
                    "description": "ISO 639-1 language code used in title",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                }
            },
            "fields": {
                "FOR": {
                    "description": "ANZSRC Fields of Research classification",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "FOR_first": {
                    "description": "Division level FOR",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_HC": {
                    "description": "HRCS - Health Categories",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_RAC": {
                    "description": "HRCS \u2013 Research Activity Codes",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "RCDC": {
                    "description": "Research, Condition, and Disease Categorization",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "abstract": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "active_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "date_inserted": {
                    "description": "Date when publication was inserted into Dimensions",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "timestamp"
                },
                "end_date": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "timestamp"
                },
                "funder_countries": {
                    "description": "GeoNames code and name",
                    "entity_type": "countries",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "countries"
                },
                "funders": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "funding_aud": {
                    "description": "Funding amount awarded in AUD",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "financial"
                },
                "funding_cad": {
                    "description": "Funding amount awarded in CAD",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "financial"
                },
                "funding_chf": {
                    "description": "Funding amount awarded in CHF",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "financial"
                },
                "funding_eur": {
                    "description": "Funding amount awarded in EUR",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "financial"
                },
                "funding_gbp": {
                    "description": "Funding amount awarded in GBP",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "financial"
                },
                "funding_jpy": {
                    "description": "Funding amount awarded in JPY",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "financial"
                },
                "funding_org_acronym": {
                    "description": "Acronym for funding organisation",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "funding_org_city": {
                    "description": "City name for funding organisation",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "funding_org_name": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "funding_usd": {
                    "description": "Funding amount awarded in USD",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "financial"
                },
                "id": {
                    "description": "Dimensions grant id",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "language": {
                    "description": "ISO 639-1 language codes",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "linkout": {
                    "description": "URL linked to grant",
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "original_title": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "project_num": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "research_org_cities": {
                    "description": "GeoNames id and name",
                    "entity_type": "cities",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "cities"
                },
                "research_org_countries": {
                    "description": "GeoNames code and name",
                    "entity_type": "countries",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "countries"
                },
                "research_org_name": {
                    "description": "Name for research organisation",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "research_org_state_codes": {
                    "description": "GeoNames code and name",
                    "entity_type": "states",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "states"
                },
                "research_orgs": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "researcher_details": {
                    "description": "Additional details about researchers including affiliations and role",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "json"
                },
                "researchers": {
                    "description": null,
                    "entity_type": "researchers",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "researchers"
                },
                "resulting_publication_ids": {
                    "description": "Resulting Publication IDs. Deprecated, use `publications` field `supporting_grant_ids` instead",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "start_date": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "timestamp"
                },
                "start_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "terms": {
                    "description": "Extracted terms",
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "title": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "title_language": {
                    "description": "ISO 639-1 language code used in title",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                }
            },
            "fieldsets": [
                "all",
                "basics",
                "extras"
            ],
            "metrics": {
                "count": {
                    "description": "Total count",
                    "name": "count"
                },
                "funding": {
                    "description": null,
                    "name": "funding"
                }
            },
            "search_fields": [
                "title_only",
                "title_abstract_only",
                "full_data",
                "terms",
                "researchers",
                "noun_phrases"
            ]
        },
        "patents": {
            "facets": {
                "FOR": {
                    "description": "ANZSRC Fields of Research classification",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "FOR_first": {
                    "description": "Division level FOR",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_HC": {
                    "description": "HRCS - Health Categories",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_RAC": {
                    "description": "HRCS \u2013 Research Activity Codes",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "RCDC": {
                    "description": "Research, Condition, and Disease Categorization",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "assignee_cities": {
                    "description": "GeoNames id and name",
                    "entity_type": "cities",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "cities"
                },
                "assignee_countries": {
                    "description": "GeoNames code and name",
                    "entity_type": "countries",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "countries"
                },
                "assignee_state_codes": {
                    "description": "GeoNames code and name",
                    "entity_type": "states",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "states"
                },
                "assignee_state_names": {
                    "description": "GeoNames name",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "assignees": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "current_assignees": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "filed_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "funder_groups": {
                    "description": null,
                    "entity_type": "org_groups",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "org_groups"
                },
                "funders": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "granted_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "original_assignees": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                }
            },
            "fields": {
                "FOR": {
                    "description": "ANZSRC Fields of Research classification",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "FOR_first": {
                    "description": "Division level FOR",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_HC": {
                    "description": "HRCS - Health Categories",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_RAC": {
                    "description": "HRCS \u2013 Research Activity Codes",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "RCDC": {
                    "description": "Research, Condition, and Disease Categorization",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "abstract": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "additional_filters": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "assignee_cities": {
                    "description": "GeoNames id and name",
                    "entity_type": "cities",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "cities"
                },
                "assignee_countries": {
                    "description": "GeoNames code and name",
                    "entity_type": "countries",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "countries"
                },
                "assignee_names": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "assignee_state_codes": {
                    "description": "GeoNames code and name",
                    "entity_type": "states",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "states"
                },
                "assignee_state_names": {
                    "description": "GeoNames name",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "assignees": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "associated_grant_ids": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "cited_by_ids": {
                    "description": "Patents which cite this patent",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "cpc": {
                    "description": "Cooperative Patent Classification number for a patent",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "current_assignee_names": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "current_assignees": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "date": {
                    "description": "Date when the patent was filed",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "timestamp"
                },
                "date_inserted": {
                    "description": "Date when publication was inserted into Dimensions",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "timestamp"
                },
                "expiration_date": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "timestamp"
                },
                "filed_date": {
                    "description": "Deprecated in favor of `filed_date`",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "timestamp"
                },
                "filed_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "filing_status": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "funder_groups": {
                    "description": null,
                    "entity_type": "org_groups",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "org_groups"
                },
                "funders": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "granted_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "id": {
                    "description": "Dimensions patent id",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "inventor_names": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "ipcr": {
                    "description": "International Patent Classification Reform number for a patent",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "jurisdiction": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "legal_status": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "original_assignee_names": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "original_assignees": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "priority_date": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "timestamp"
                },
                "publication_date": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "timestamp"
                },
                "publication_ids": {
                    "description": "Related publication IDs",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "reference_ids": {
                    "description": "Patents which are cited by this patent",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "status": {
                    "description": "Deprecated in favor of `legal_status`",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "times_cited": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "count"
                },
                "title": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                }
            },
            "fieldsets": [
                "all",
                "basics",
                "extras"
            ],
            "metrics": {
                "count": {
                    "description": "Total count",
                    "name": "count"
                }
            },
            "search_fields": [
                "title_only",
                "title_abstract_only",
                "full_data"
            ]
        },
        "policy_documents": {
            "facets": {
                "FOR": {
                    "description": "ANZSRC Fields of Research classification",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "FOR_first": {
                    "description": "Division level FOR",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_HC": {
                    "description": "HRCS - Health Categories",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_RAC": {
                    "description": "HRCS \u2013 Research Activity Codes",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "RCDC": {
                    "description": "Research, Condition, and Disease Categorization",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "broad_research_areas": {
                    "description": null,
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "city": {
                    "description": null,
                    "entity_type": "cities",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "cities"
                },
                "country": {
                    "description": null,
                    "entity_type": "countries",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "countries"
                },
                "health_research_areas": {
                    "description": null,
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "state": {
                    "description": null,
                    "entity_type": "states",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "states"
                },
                "year": {
                    "description": "Policy posted on year",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                }
            },
            "fields": {
                "FOR": {
                    "description": "ANZSRC Fields of Research classification",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "FOR_first": {
                    "description": "Division level FOR",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_HC": {
                    "description": "HRCS - Health Categories",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_RAC": {
                    "description": "HRCS \u2013 Research Activity Codes",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "RCDC": {
                    "description": "Research, Condition, and Disease Categorization",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "broad_research_areas": {
                    "description": null,
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "city": {
                    "description": null,
                    "entity_type": "cities",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "cities"
                },
                "country": {
                    "description": null,
                    "entity_type": "countries",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "countries"
                },
                "grid_id": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "health_research_areas": {
                    "description": null,
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "id": {
                    "description": "Dimensions clinical trial id",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "linkout": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "publication_ids": {
                    "description": "Referenced Publication IDs",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "source_name": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "state": {
                    "description": null,
                    "entity_type": "states",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "states"
                },
                "title": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "year": {
                    "description": "Policy posted on year",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                }
            },
            "fieldsets": [
                "all",
                "basics",
                "categories"
            ],
            "metrics": {
                "count": {
                    "description": "Total count",
                    "name": "count"
                }
            },
            "search_fields": [
                "title_only",
                "full_data"
            ]
        },
        "publications": {
            "facets": {
                "FOR": {
                    "description": "ANZSRC Fields of Research classification",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "FOR_first": {
                    "description": "Division level FOR",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_HC": {
                    "description": "HRCS - Health Categories",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_RAC": {
                    "description": "HRCS \u2013 Research Activity Codes",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "RCDC": {
                    "description": "Research, Condition, and Disease Categorization",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "funder_countries": {
                    "description": null,
                    "entity_type": "countries",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "countries"
                },
                "funders": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "journal": {
                    "description": null,
                    "entity_type": "journals",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "journals"
                },
                "mesh_terms": {
                    "description": "Medical Subject Heading terms as used in PubMed.",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "open_access_categories": {
                    "description": "Open Access category for publication. Filtering on values is case sensitive.",
                    "entity_type": "open_access",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": "\n        Open Access category data for publications values:\n\n        * `oa_all`: Article is freely available\n        * `gold_pure`: Version Of Record (VOR) is free under an open licence from a full OA journal\n        * `gold_hybrid`: Version Of Record (VOR) is free under an open licence in a paid-access journal\n        * `gold_bronze`: Freely available on publisher page, but without an open licence\n        * `green_pub`: Free copy of published version in an OA repository\n        * `green_acc`: Free copy of accepted version in an OA repository\n        * `green_sub`: Free copy of submitted version, or where version is unknown, in an OA repository\n        * `closed`: No freely available copy has been identified\n        ",
                    "type": "open_access"
                },
                "publisher": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "recent_citations": {
                    "description": "Number of citations received in the last two years. Does not support emptiness filters",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "referenced_pubs": {
                    "description": "Dimensions publication id for documents referencing another document",
                    "entity_type": "publications",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "publications_entity"
                },
                "research_org_cities": {
                    "description": "GeoNames id and name",
                    "entity_type": "cities",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "cities"
                },
                "research_org_countries": {
                    "description": null,
                    "entity_type": "countries",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "countries"
                },
                "research_org_state_codes": {
                    "description": "GeoNames code and name",
                    "entity_type": "states",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "states"
                },
                "research_org_state_names": {
                    "description": "GeoNames state name",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "research_orgs": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "researchers": {
                    "description": null,
                    "entity_type": "researchers",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "researchers"
                },
                "year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                }
            },
            "fields": {
                "FOR": {
                    "description": "ANZSRC Fields of Research classification",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "FOR_first": {
                    "description": "Division level FOR",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_HC": {
                    "description": "HRCS - Health Categories",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "HRCS_RAC": {
                    "description": "HRCS \u2013 Research Activity Codes",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "RCDC": {
                    "description": "Research, Condition, and Disease Categorization",
                    "entity_type": "categories",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "categories"
                },
                "altmetric": {
                    "description": "Altmetric attention score. Does not support emptiness filters",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "float"
                },
                "author_affiliations": {
                    "description": "List of JSON lists of researchers' first and last names and affiliations",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "json"
                },
                "book_doi": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "book_series_title": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "book_title": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "date": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "date"
                },
                "date_inserted": {
                    "description": "Date when publication was inserted into Dimensions",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "timestamp"
                },
                "doi": {
                    "description": "Digital object identifier",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "field_citation_ratio": {
                    "description": "Relative citation performance of article when compared to similarly aged articles in its area of research. Does not support emptiness filters",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "float"
                },
                "funder_countries": {
                    "description": null,
                    "entity_type": "countries",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "countries"
                },
                "funders": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "id": {
                    "description": "Dimensions publication id",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "issn": {
                    "description": "International Standard Serial Number",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "issue": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "journal": {
                    "description": null,
                    "entity_type": "journals",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "journals"
                },
                "journal_lists": {
                    "description": "Independent grouping of journals outside of Dimensions",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "linkout": {
                    "description": "URL address",
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "mesh_terms": {
                    "description": "Medical Subject Heading terms as used in PubMed.",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "open_access": {
                    "description": "Open Access status for publication. Deprecated in favor of `open_access_categories`",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": "\n\n        **DEPRECATED in favor of `open_access_categories`**\n\n        Open Access field data for publications can make reference to information on the host location and the record version.\n\n        **Open Access host location**\n\n        Host location information can describes if the document is either hosted by the publisher or in an institutional repository.\n\n           * **Open access - publisher** means the linked full-text version is served by the article's publisher.\n           * **Open access - repository** means the linked full-text version is served by an Open Access repository.\n\n        **Record Version**\n\n        Record version refers to the version of the content as defined by Unpaywall (see `Unpaywall Data Format <https://unpaywall.org/data-format>`_)\n\n           * **Open access - submitted** means the linked full-text version is not yet peer-reviewed.\n           * **Open access - accepted** means the linked full-text version is peer-reviewed, but lacks publisher-specific formatting.\n           * **Open access - published** means the linked full-text version is the version of record.\n        ",
                    "type": "string"
                },
                "open_access_categories": {
                    "description": "Open Access category for publication. Filtering on values is case sensitive.",
                    "entity_type": "open_access",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": "\n        Open Access category data for publications values:\n\n        * `oa_all`: Article is freely available\n        * `gold_pure`: Version Of Record (VOR) is free under an open licence from a full OA journal\n        * `gold_hybrid`: Version Of Record (VOR) is free under an open licence in a paid-access journal\n        * `gold_bronze`: Freely available on publisher page, but without an open licence\n        * `green_pub`: Free copy of published version in an OA repository\n        * `green_acc`: Free copy of accepted version in an OA repository\n        * `green_sub`: Free copy of submitted version, or where version is unknown, in an OA repository\n        * `closed`: No freely available copy has been identified\n        ",
                    "type": "open_access"
                },
                "pages": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "pmcid": {
                    "description": "PubMed Central ID",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "pmid": {
                    "description": "PubMed ID",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "proceedings_title": {
                    "description": "Title of a conference corresponding to documents that are `type` of \"proceeding\"",
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "publisher": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "recent_citations": {
                    "description": "Number of citations received in the last two years. Does not support emptiness filters",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "referenced_pubs": {
                    "description": "Dimensions publication id for documents referencing another document",
                    "entity_type": "publications",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "publications_entity"
                },
                "references": {
                    "description": "Dimensions publication id for documents referencing another document",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "relative_citation_ratio": {
                    "description": "Relative citation performance of an article when compared to others in its area of research. Does not support emptiness filters",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "float"
                },
                "research_org_cities": {
                    "description": "GeoNames id and name",
                    "entity_type": "cities",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "cities"
                },
                "research_org_countries": {
                    "description": null,
                    "entity_type": "countries",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "countries"
                },
                "research_org_country_names": {
                    "description": "GeoNames country name",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "research_org_state_codes": {
                    "description": "GeoNames code and name",
                    "entity_type": "states",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "states"
                },
                "research_org_state_names": {
                    "description": "GeoNames state name",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "label"
                },
                "research_orgs": {
                    "description": null,
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "researchers": {
                    "description": null,
                    "entity_type": "researchers",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "researchers"
                },
                "supporting_grant_ids": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "terms": {
                    "description": "Extracted terms. See :ref:`for-terms` regarding searching terms vs phrases",
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "times_cited": {
                    "description": "Number of citations. Does not support emptiness filters",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "count"
                },
                "title": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "type": {
                    "description": "Publication type (article, chapter, proceeding, monograph or preprint)",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "volume": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                }
            },
            "fieldsets": [
                "all",
                "basics",
                "extras",
                "book"
            ],
            "metrics": {
                "altmetric_median": {
                    "description": "Median Altmetric attention score",
                    "name": "altmetric_median"
                },
                "citations_avg": {
                    "description": "Arithmetic mean of citations",
                    "name": "citations_avg"
                },
                "citations_median": {
                    "description": "Median of citations",
                    "name": "citations_median"
                },
                "citations_total": {
                    "description": "Aggregated number of citations",
                    "name": "citations_total"
                },
                "count": {
                    "description": "Total count",
                    "name": "count"
                },
                "fcr_gavg": {
                    "description": "Geometric mean of `field_citation_ratio`",
                    "name": "fcr_gavg"
                },
                "rcr_avg": {
                    "description": "Arithmetic mean of `relative_citation_ratio`",
                    "name": "rcr_avg"
                },
                "recent_citations_total": {
                    "description": "For a given article, in a given year, the number of citations accrued in the last two year period. Single value stored per document, year window rolls over in July.",
                    "name": "recent_citations_total"
                }
            },
            "search_fields": [
                "title_only",
                "title_abstract_only",
                "full_data",
                "authors",
                "terms_experimental",
                "terms",
                "researchers",
                "noun_phrases"
            ]
        },
        "researchers": {
            "facets": {
                "current_research_org": {
                    "description": "The most recent research organization linked to the researcher",
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "first_grant_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "first_publication_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "last_grant_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "last_publication_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "obsolete": {
                    "description": "\n        The researcher is obsolete (value=1) if it does not have anymore any ownerships. The \"redirect\" field gives additional information (split, merge, delete).\n        The meta-information listed with the obsolete researcher is the meta-information of the first researcher listed in \"redirect\". If there is None, there is\n        no meta information (the last name gets a \"Not available\" placeholder value).\n        ",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "research_orgs": {
                    "description": "All research organizations linked to the researcher",
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "total_grants": {
                    "description": "Total grants count",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "total_publications": {
                    "description": "Total publications count",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                }
            },
            "fields": {
                "current_research_org": {
                    "description": "The most recent research organization linked to the researcher",
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "first_grant_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "first_name": {
                    "description": "First Name",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "first_publication_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "id": {
                    "description": "Dimensions researcher id",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "last_grant_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "last_name": {
                    "description": "Last Name",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "string"
                },
                "last_publication_year": {
                    "description": null,
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "obsolete": {
                    "description": "\n        The researcher is obsolete (value=1) if it does not have anymore any ownerships. The \"redirect\" field gives additional information (split, merge, delete).\n        The meta-information listed with the obsolete researcher is the meta-information of the first researcher listed in \"redirect\". If there is None, there is\n        no meta information (the last name gets a \"Not available\" placeholder value).\n        ",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "orcid_id": {
                    "description": "`ORCID <https://orcid.org/>`_ ID",
                    "is_entity": false,
                    "is_filter": false,
                    "long_description": null,
                    "type": "text"
                },
                "redirect": {
                    "description": "\n        For obsolete researchers this field defines the other researchers which got the ownerships previously assigned to this record. If there is a single entry,\n        then the obsolete researcher was merged completely into that one. If there are multiple entries, we have a split. If there is no entry, the researcher is deleted,\n        because all of its ownerships were deleted (e.g. by publication delete).\n        ",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "identifier"
                },
                "research_orgs": {
                    "description": "All research organizations linked to the researcher",
                    "entity_type": "orgs",
                    "is_entity": true,
                    "is_filter": true,
                    "long_description": null,
                    "type": "orgs"
                },
                "total_grants": {
                    "description": "Total grants count",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                },
                "total_publications": {
                    "description": "Total publications count",
                    "is_entity": false,
                    "is_filter": true,
                    "long_description": null,
                    "type": "integer"
                }
            },
            "fieldsets": [
                "all",
                "basics",
                "extras"
            ],
            "metrics": {
                "count": {
                    "description": "Total count",
                    "name": "count"
                }
            },
            "search_fields": [
                "researcher"
            ]
        }
    }
}