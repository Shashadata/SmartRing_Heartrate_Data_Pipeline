1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

...
Phase 1 represents the most active period.
Metric 1 (Average): Phase 1 has the highest average heart rate of 87.3.
Metric 2 (Median): Phase 1 also has the highest median of 88.5, showing the heart rate staed high consistently.
Comparison: For a 30-year-old, the target zone(50-85%) starts at 95 bpm. While 87.3 is just below that, it is much closer than any other phase, meaning the participant was likely walking or lightly moving during this time.

2) Which file had the **poorest** data quality? How do you know?

...
Phase 0 had the poorest data quality.
We can tell by looking at the Skipped Rows. Phase 0 had 3 skipped rows, which is more than any other file. This means the sensor failed or recorded "trash" data more often in this phase than the others.

3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.
180 - 68 = 112.
The range is 112.


b) Explain how the extreme value affects the range.
The extreme value(180)makes the range much larger than it should be. Without that one glitch, the range would be only 7(75-68.) It shows that one bad sensor reading can make the whole dataset look very messy.


c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?
Because these statistic focus on the middle part of the data where most numbers are. They "ignore" the 180 glitch, so they give a much more honest picture of the person's real heart rate.