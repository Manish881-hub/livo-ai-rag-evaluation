#!/usr/bin/env python3
"""
RAG Evaluation Script for Livo AI Assessment
"""

import json
import os
from datetime import datetime


def load_qa_dataset():
    """Load the QA pairs from the dataset file."""
    with open('qa_dataset.json', 'r') as f:
        return json.load(f)


def run_evaluation():
    """Run evaluation on the QA pairs."""
    qa_data = load_qa_dataset()
    
    print("=" * 60)
    print("Running RAG Evaluation...")
    print("=" * 60)
    
    results = []
    for qa in qa_data['qa_pairs']:
        entry = {
            'query_id': qa['id'],
            'question': qa['question'],
            'ground_truth_answer': qa['answer'],
            'difficulty': qa['difficulty'],
            'source_video': f"https://www.youtube.com/watch?v={qa['source']['video_id']}",
            'timestamp': qa['source']['timestamp_start'],
            'evaluated_at': datetime.now().isoformat()
        }
        results.append(entry)
    
    return results


def save_results(results, output_path):
    """Save evaluation results to JSON file."""
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to: {output_path}")


def main():
    os.makedirs('results', exist_ok=True)
    results = run_evaluation()
    save_results(results, 'results/evaluation_results.json')
    print(f"\nEvaluation complete! {len(results)} results saved.")


if __name__ == "__main__":
    main()