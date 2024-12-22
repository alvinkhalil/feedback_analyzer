from  feedback_analyzer.utils import get_mongo_database

def get_aggregation_results(pipeline):
    db = get_mongo_database()  
    collection = db["feedback"] 
    results = list(collection.aggregate(pipeline))
    return results
