import subprocess
import os


def run_script(script_path):
    subprocess.run(["python", script_path], check=True)


def main():
    try:
        # Run Data Collection
        print("Running Data Collection...")
        run_script(os.path.join(
            "src", "data_collection", "twitter_collection.py"))

        # Run Data Preprocessing
        print("Running Data Preprocessing...")
        run_script(os.path.join("src", "data_preprocessing", "preprocess.py"))

        # Run Sentiment Analysis
        print("Running Sentiment Analysis...")
        run_script(os.path.join(
            "src", "sentiment_analysis", "sentiment_analysis.py"))

        # Run Visualization
        print("Running Visualization...")
        run_script(os.path.join("src", "visualization", "visualize.py"))

        # Run Additional Analysis
        print("Running Additional Analysis - Topic Modeling...")
        run_script(os.path.join(
            "src", "additional_analysis", "topic_modeling.py"))

        print("Running Additional Analysis - Influencer Identification...")
        run_script(os.path.join("src", "additional_analysis",
                   "influencer_identification.py"))

    except subprocess.CalledProcessError as e:
        print(f"An error occurred in {e.cmd}: {e.output}")


if __name__ == "__main__":
    main()
