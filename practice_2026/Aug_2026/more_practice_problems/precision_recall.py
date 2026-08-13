
def get_precision_recall(target_intent: str, ground_truth: list[dict], predictions: list[dict]) -> dict[str, float]:
    """
    Calculates precision and recall for a specific target intent.
    
    Args:
        target_intent: The intent to evaluate (e.g., 'PlayMusic')
        ground_truth: List of dicts e.g., [{'request_id': '123', 'intent': 'PlayMusic'}, ...]
        predictions: List of dicts e.g., [{'request_id': '123', 'intent': 'PlayMusic'}, ...]
        
    Returns:
        A dictionary with 'precision' and 'recall'. 
        Return 0.0 for a metric if its denominator is 0.
    """
    entry_log = {}
    result = {}

    # TP
    # truth = 1
    # pred = 1

    # FP
    # truth = 0
    # pred = 1

    # FN
    # truth = 1
    # pred = 0

    # TN
    # truth = 0
    # pred = 0

    truth_dict = {log['request_id']: log['intent'] for log in ground_truth}
    pred_dict = {log['request_id']: log['intent'] for log in predictions}
    print(truth_dict)

    common_keys = truth_dict.keys() & pred_dict.keys()

    print(common_keys)

    inner_join_result = {key: {"truth": truth_dict[key], "pred": pred_dict[key]} for key in common_keys}

    print(inner_join_result)




    # for l in ground_truth:
    #     if l['request_id'] not in entry_log:
    #         entry_log[l['request_id']] = {}
    #     if l['intent'] == target_intent:
    #         entry_log[l['request_id']]["truth"] = 1
    #     else:
    #         entry_log[l['request_id']]["truth"] = 0

    # for l in predictions:
    #     if l['request_id'] not in entry_log:
    #         entry_log[l['request_id']] = {}
    #     if l['intent'] == target_intent:
    #         entry_log[l['request_id']]["pred"] = 1
    #     else:
    #         entry_log[l['request_id']]["pred"] = 0

    

    # for k in entry_log:
    #     v = entry_log[k]
    #     if len(v) > 1:
    #         if target_intent not in result:
    #             result[target_intent] = {"tp": 0, "fp": 0, "tn": 0, "fn": 0}
    #         if v.get('truth') == 1 and v.get('pred') == 1:
    #             result[target_intent]["tp"] += 1
                
    #         elif v.get('truth') == 0 and v.get('pred') == 1:
    #             result[target_intent]["fp"] += 1

    #         elif v.get('truth') == 1 and v.get('pred') == 0:
    #             result[target_intent]["fn"] += 1

    #         else:
    #             result[target_intent]["tn"] += 1


    # TP = result[target_intent]["tp"]
    # FP = result[target_intent]["fp"]
    # FN = result[target_intent]["fn"]
    # Precision = TP / (TP + FP)
    # Recall = TP / (TP + FN)
    # return print({'precision': Precision, 'recall': Recall})  


# --- TEST CASES ---
truth_logs = [
    {'request_id': 'A1', 'intent': 'PlayMusic'},
    {'request_id': 'B2', 'intent': 'SetTimer'},
    {'request_id': 'C3', 'intent': 'PlayMusic'},
    {'request_id': 'D4', 'intent': 'Weather'}, # Missing in predictions
]

pred_logs = [
    {'request_id': 'B2', 'intent': 'SetTimer'},
    {'request_id': 'A1', 'intent': 'PlayMusic'},
    {'request_id': 'C3', 'intent': 'SetTimer'}, # Incorrect prediction
    {'request_id': 'E5', 'intent': 'PlayMusic'}, # Missing in truth
]

get_precision_recall('PlayMusic', truth_logs, pred_logs)

# Expected output for target_intent = 'PlayMusic':
# 'A1' -> Truth: PlayMusic, Pred: PlayMusic (True Positive)
# 'B2' -> Truth: SetTimer, Pred: SetTimer (True Negative for PlayMusic)
# 'C3' -> Truth: PlayMusic, Pred: SetTimer (False Negative)
# 'D4' -> Dropped (no prediction)
# 'E5' -> Dropped (no truth)

# True Positives = 1 ('A1')
# False Positives = 0
# False Negatives = 1 ('C3')

# Precision = TP / (TP + FP) = 1 / 1 = 1.0
# Recall = TP / (TP + FN) = 1 / 2 = 0.5
# Expected: {'precision': 1.0, 'recall': 0.5}

#Pruned
# def get_precision_recall(target_intent: str, ground_truth: list[dict], predictions: list[dict]) -> dict[str, float]:
#     entry_log = {}
    
#     # [1] PRE-INITIALIZE to prevent KeyError if no logs overlap
#     result = {target_intent: {"tp": 0, "fp": 0, "tn": 0, "fn": 0}}

#     for l in ground_truth:
#         if l['request_id'] not in entry_log:
#             entry_log[l['request_id']] = {}
#         if l['intent'] == target_intent:
#             entry_log[l['request_id']]["truth"] = 1
#         else:
#             entry_log[l['request_id']]["truth"] = 0

#     for l in predictions:
#         if l['request_id'] not in entry_log:
#             entry_log[l['request_id']] = {}
#         if l['intent'] == target_intent:
#             entry_log[l['request_id']]["pred"] = 1
#         else:
#             entry_log[l['request_id']]["pred"] = 0

#     for k in entry_log:
#         v = entry_log[k]
#         if len(v) > 1:
#             if v.get('truth') == 1 and v.get('pred') == 1:
#                 result[target_intent]["tp"] += 1
                
#             elif v.get('truth') == 0 and v.get('pred') == 1:
#                 result[target_intent]["fp"] += 1

#             elif v.get('truth') == 1 and v.get('pred') == 0:
#                 result[target_intent]["fn"] += 1

#             else:
#                 result[target_intent]["tn"] += 1

#     TP = result[target_intent]["tp"]
#     FP = result[target_intent]["fp"]
#     FN = result[target_intent]["fn"]
    
#     # [2] SAFE DIVISION to prevent ZeroDivisionError
#     Precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0
#     Recall = TP / (TP + FN) if (TP + FN) > 0 else 0.0
    
#     # [3] RETURN directly, don't print
#     return {'precision': Precision, 'recall': Recall}