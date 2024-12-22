from django.shortcuts import render
from app.aggreagator.aggregator import get_aggregation_results
from app.aggreagator.query import get_feedback_score

def index(request):

    if request.method == 'POST' and request.POST.get("q"):
        q = request.POST.get("q")

        feedback_query = get_feedback_score(q)

    else:
        feedback_query = get_feedback_score()
        
    feedback_query = get_aggregation_results(feedback_query)
    return render(request, 'feedback_score.html', {'feedback_scores': feedback_query})
