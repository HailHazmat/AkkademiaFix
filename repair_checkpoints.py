import torch
from argparse import Namespace

def repair(path, source_lang, target_lang):
    print(f"Repairing {path}...")
    try:
        # Load the checkpoint
        state = torch.load(path, map_location='cpu')
        
        # Define the correct architecture and task settings
        args = Namespace()
        args.arch = 'fconv'           # Changed from 'transformer' to 'fconv'
        args.task = 'translation'
        args.source_lang = source_lang
        args.target_lang = target_lang
        
        # Convolutional models typically do not share embeddings in this project
        args.share_all_embeddings = False 
        
        # Standard criterion for Fairseq translation tasks
        args.criterion = 'label_smoothed_cross_entropy'
        
        state['args'] = args
        
        # Save the updated checkpoint
        torch.save(state, path)
        print(f" -> Success: {path} is now configured as a Convolutional (fconv) model.")
            
    except Exception as e:
        print(f" -> Error: {e}")

if __name__ == "__main__":
    # Paths identified in the diagnostic logs
    c2e_path = "not_divided_by_three_dots_result.LR_0.1.MAX_TOKENS_4000/checkpoint_best.pt"
    t2e_path = "trans_result.LR_0.1.MAX_TOKENS_4000/checkpoint_best.pt"
    
    repair(c2e_path, source_lang='ak', target_lang='en')
    repair(t2e_path, source_lang='tr', target_lang='en')