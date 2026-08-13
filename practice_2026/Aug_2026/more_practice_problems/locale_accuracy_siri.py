from collections import defaultdict
# def calculate_locale_accuracy(logs: list[dict], conf_score: float) -> dict[str, float]:
#     """
#     Calculate the accuracy per locale, considering only logs where 
#     confidence_score >= confidence_threshold.
    
#     Args:
#         logs: List of dictionaries representing model inferences.
#         confidence_threshold: Minimum confidence score to be evaluated.
        
#     Returns:
#         A dictionary mapping locale strings to their accuracy float.
#     """
#     by_locale = defaultdict(list)
#     for l in logs:
#         by_locale[l["locale"]].append(l)
#     summary = {}
#     for k, v in by_locale.items():
#         correct = 0
#         tot_valid = 0
#         for e in v:
#             if e['actual'] == e['predicted'] and e['confidence'] >= conf_score:
#                 correct += 1
#             if e['actual'] == e['predicted']:
#                 tot_valid += 1

#             accuracy = correct/tot_valid if tot_valid > 0 else None
#         if accuracy > 0:
#             summary[k] = accuracy
#     return print(summary)


def calculate_locale_accuracy(logs: list[dict], confidence_threshold: float) -> dict[str, float]:
    # Store running counts: { 'en-US': {'correct': 1, 'valid': 2} }
    counts = {} 
    
    for log in logs:
        conf = log['confidence']
        
        # Only process logs that meet the threshold
        if conf >= confidence_threshold:
            locale = log['locale']
            
            # Manually initialize the dictionary if we haven't seen this locale yet
            if locale not in counts:
                counts[locale] = {'correct': 0, 'valid': 0}
                
            counts[locale]['valid'] += 1
            
            if log['actual'] == log['predicted']:
                counts[locale]['correct'] += 1
                
    # Calculate final accuracy 
    print(counts)
    summary = {}
    for locale, stats in counts.items():
        summary[locale] = stats['correct'] / stats['valid']
        
    return print(summary)


sample_logs = [
    {'locale': 'en-US', 'actual': 'weather', 'predicted': 'weather', 'confidence': 0.95}, # Correct, Valid
    {'locale': 'en-US', 'actual': 'timer',   'predicted': 'alarm',   'confidence': 0.85}, # Incorrect, Valid
    {'locale': 'en-US', 'actual': 'music',   'predicted': 'music',   'confidence': 0.60}, # Ignored (below threshold)
    {'locale': 'fr-FR', 'actual': 'weather', 'predicted': 'weather', 'confidence': 0.90}, # Correct, Valid
    {'locale': 'fr-FR', 'actual': 'weather', 'predicted': 'weather', 'confidence': 0.92}, # Correct, Valid
    {'locale': 'es-ES', 'actual': 'timer',   'predicted': 'timer',   'confidence': 0.50}, # Ignored (below threshold)
]
conf_score = 0.80
calculate_locale_accuracy(sample_logs, conf_score)




    