import akkadian.transliterate as akk
from akkadian.data import load_object_from_file
from akkadian.combine_algorithms import overall_classifier, combine_tags
from akkadian.__init__ import hmm_path, memm_path, bilstm_path
from datetime import datetime

# --- 1. LOAD THE DATA ---
print("Loading all models... please wait.")

# Unpack the HMM container 
# Note: 'e' here is the HMM Emission probabilities
most_common_tag, possible_tags, q, e, S, total_tokens, q_bi_counts, q_uni_counts, lambda1, lambda2, _ = \
    load_object_from_file(hmm_path)

# Unpack the MEMM container
logreg, vec, idx_to_tag_dict, _ = load_object_from_file(memm_path)

# Unpack the BiLSTM container
model, predictor, sign_to_id, id_to_tran, _ = load_object_from_file(bilstm_path)

# Constants for the combined logic
gamma1 = 0.4
gamma2 = 0.2

print("Models loaded successfully!")

def main():
    log_file = "full_comparison_log.txt"
    
    while True:
        raw_input = input("\nEnter Signs: ").strip()
        if raw_input.lower() in ['exit', 'quit']: break
        if not raw_input: continue

        sentence = akk.sanitize(raw_input)

        print("\n" + "="*85)
        print(f"{'MODEL':<15} | {'TRANSLITERATION'}")
        print("-" * 85)

        # 1. Get results from individual package functions
        res_bilstm = akk.transliterate_bilstm(sentence)
        res_hmm = akk.transliterate_hmm(sentence)
        res_memm = akk.transliterate_memm(sentence)

        print(f"{'BiLSTM':<15} | {res_bilstm}")
        print(f"{'HMM':<15} | {res_hmm}")
        print(f"{'MEMM':<15} | {res_memm}")

        # 2. Combined and Highlighting Logic
        try:
            # We fetch raw tag lists for comparison
            tag_logits = predictor.predict(akk.sentence_to_allen_format(sentence, sign_to_id, True))['tag_logits']
            bi1, bi2, bi3, sc1, sc2, sc3 = akk.logits_to_trans(tag_logits, model, id_to_tran)
            
            hmm_input = akk.sentence_to_HMM_format(sentence)
            HMM_pred = akk.hmm_viterbi(hmm_input, total_tokens, q_bi_counts, q_uni_counts, q, e, S, 
                                      most_common_tag, possible_tags, lambda1, lambda2)
            MEMM_pred = akk.memm_greedy(hmm_input, logreg, vec, idx_to_tag_dict)
            
            # Combine them
            algo_tags = (bi1, bi2, bi3, sc1, sc2, sc3, HMM_pred, MEMM_pred)
            res_combined = akk.list_to_tran(combine_tags(algo_tags, gamma1, gamma2))

            # Highlight Disputed signs
            disputed_list = []
            for i in range(min(len(bi1), len(HMM_pred))):
                if bi1[i] != HMM_pred[i]:
                    disputed_list.append(f"[{bi1[i]}/{HMM_pred[i]}]")
                else:
                    disputed_list.append(bi1[i])
            res_disputed = akk.list_to_tran(disputed_list)

        except Exception as err:
            res_combined = f"Error in calculation: {err}"
            res_disputed = "N/A"
            
        print(f"{'Combined':<15} | {res_combined}")
        print("-" * 85)
        print(f"{'DISPUTED':<15} | {res_disputed}")
        print("="*85)

        # Log it
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] Input: {sentence}\n")
            f.write(f"  Combined: {res_combined}\n")
            f.write(f"  Disputed: {res_disputed}\n")
            f.write("-" * 45 + "\n")

if __name__ == "__main__":
    main()