
question_image_order = """
Floorplans-24-0.png
Floorplans-24-10.png
Floorplans-24-11.png
Floorplans-24-12.png
Floorplans-24-13.png
Floorplans-24-14.png
Floorplans-24-15.png
Floorplans-24-16.png
Floorplans-24-17.png
Floorplans-24-18.png
Floorplans-24-19.png
Floorplans-24-1.png
Floorplans-24-20.png
Floorplans-24-21.png
Floorplans-24-22.png
Floorplans-24-23.png
Floorplans-24-2.png
Floorplans-24-3.png
Floorplans-24-4.png
Floorplans-24-5.png
Floorplans-24-6.png
Floorplans-24-7.png
Floorplans-24-8.png
Floorplans-24-9.png
""".split()

from collections import defaultdict
import statistics
from colors import *
import matplotlib.pyplot as plt


class FloorplanCsvAnalyzer(object):

    def __init__(self, input_csv):
        self.rows = []
        for line in open(input_csv, 'r'):
            row = line.split(',')[17:]
            self.rows.append(row)
        self.rows = self.rows[4:]

    def compute_average_csv(self):
        image_to_scores = defaultdict(list)
        for row in self.rows:
            for i, value in enumerate(row):
                value = value.strip()
                if value == '':
                    continue
                image_to_scores[question_image_order[i]].append(int(value))

        return [ (image_to_scores[k], k) for k in image_to_scores.keys() ]
        # return sorted([(statistics.mean(image_to_scores[k]), k) for k in image_to_scores.keys() ])

    def display_computer_vs_human(self):
        averages = self.compute_average_csv()
        score_to_filenum = [ (score, int(filename.replace("Floorplans-24-", "").replace(".png", ""))) for score, filename in averages ]

        human, computer = [], []

        with open('out/id_source_score.csv', 'w') as f:
            f.write("ID,SOURCE,SCORE\n")

            for scores, filenum in score_to_filenum:
                print(scores)
                source = "machine" if filenum < 12 else "human"
                for score in scores:
                    f.write(f"plan-{filenum},{source},{score}\n")

                mean_score = statistics.mean(scores)

                if source == "machine":
                    # print(color(f"{mean_score}, {filenum}", bg='green', fg='black'))
                else:
                    # print(color(f"{mean_score}, {filenum}", bg='orange', fg='black'))







        # plt.hist(human, bins=7)
        # plt.figure()

        # plt.hist(computer, bins=7)
        # plt.show()



if __name__ == "__main__":
    averages = FloorplanCsvAnalyzer("input2.csv").display_computer_vs_human()

