def get_feedback_score(q=None):

    # feedback_rate-in içerisini gostermek və  branch.name ve service.name üzrə qruplasdirma
    unwind_stage = {
        "$unwind": "$feedback_rate"
    }

    group_by_branch_and_service = {
        "$group": {
            "_id": {
                "branch": "$branch.name",
                "service_name": "$feedback_rate.service.name"
            },
            "feedback_rate": {
                "$push": "$feedback_rate"
            }
        }
    }

    group_by_branch = {
        "$group": {
            "_id": "$_id.branch",
            "feedback_rate": {
                "$push": {
                    "service_name": "$_id.service_name",
                    "rate_options": "$feedback_rate.rate_option"
                }
            }
        }
    }

    # Her servis ucun rate optionlardaki reqemleri saymaq
    project_rate_counts = {
        "$project": {
            "feedback_rate": {
                "$map": {
                    "input": "$feedback_rate",
                    "as": "item",
                    "in": {
                        "service_name": "$$item.service_name",
                        "rate_options": "$$item.rate_options",
                        "rate_option_count_1": {
                            "$size": {
                                "$filter": {
                                    "input": "$$item.rate_options",
                                    "as": "rate",
                                    "cond": {"$eq": ["$$rate", 1]}
                                }
                            }
                        },
                        "rate_option_count_2": {
                            "$size": {
                                "$filter": {
                                    "input": "$$item.rate_options",
                                    "as": "rate",
                                    "cond": {"$eq": ["$$rate", 2]}
                                }
                            }
                        },
                        "rate_option_count_3": {
                            "$size": {
                                "$filter": {
                                    "input": "$$item.rate_options",
                                    "as": "rate",
                                    "cond": {"$eq": ["$$rate", 3]}
                                }
                            }
                        },
                        "rate_option_count_4": {
                            "$size": {
                                "$filter": {
                                    "input": "$$item.rate_options",
                                    "as": "rate",
                                    "cond": {"$eq": ["$$rate", 4]}
                                }
                            }
                        },
                        "rate_option_count_5": {
                            "$size": {
                                "$filter": {
                                    "input": "$$item.rate_options",
                                    "as": "rate",
                                    "cond": {"$eq": ["$$rate", 5]}
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    # Neticeleri hesablamaq (score)
    calculate_scores = {
        "$project": {
            "feedback_rate": {
                "$map": {
                    "input": "$feedback_rate",
                    "as": "item",
                    "in": {
                        "service_name": "$$item.service_name",
                        "rate_options": "$$item.rate_options",
                        "rate_option_1": "$$item.rate_option_count_1",
                        "rate_option_2": "$$item.rate_option_count_2",
                        "rate_option_3": "$$item.rate_option_count_3",
                        "rate_option_4": "$$item.rate_option_count_4",
                        "rate_option_5": "$$item.rate_option_count_5",
                        "score": {
                            "$divide": [
                                {  
                                    "$multiply": [
                                        100,
                                        {
                                            "$add": [
                                                {
                                                    "$multiply": ["$$item.rate_option_count_1", 10]
                                                },
                                                {
                                                    "$multiply": ["$$item.rate_option_count_2", 5]
                                                },
                                                {
                                                    "$multiply": ["$$item.rate_option_count_3", 0]
                                                },
                                                {
                                                    "$multiply": ["$$item.rate_option_count_4", -5]
                                                },
                                                {
                                                    "$multiply": ["$$item.rate_option_count_5", -10]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "$multiply": [
                                        {
                                            "$add": [
                                                "$$item.rate_option_count_1",
                                                "$$item.rate_option_count_2",
                                                "$$item.rate_option_count_3",
                                                "$$item.rate_option_count_4",
                                                "$$item.rate_option_count_5"
                                            ]
                                        },
                                        10
                                    ]
                                }
                            ]
                        }
                    }
                }
            }
        }
    }

    rename_branch =  {
        "$project": {
        "branch_name": "$_id",  
        "feedback_rate": 1,  
        "_id": 0,  
    }}
    sort =  {
    "$sort": { "branch.name": 1 } 
    }

    pipeline = [
        unwind_stage,
        group_by_branch_and_service,
        group_by_branch,
        project_rate_counts,
        calculate_scores,
        rename_branch,
        sort
    ]
    if q:
        search_query  = {
                "$match": {
                    "$or": [
                    { "branch.name": { "$regex": q, "$options": "i" } },
                    { "feedback_rate.service.name": { "$regex": q, "$options": "i" } }
                    ]
            }
        }
        pipeline.insert(0,search_query)


    return pipeline

