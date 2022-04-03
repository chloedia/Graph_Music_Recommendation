![cover](cover_MLNS.jpg)
# Graph Music Recommendation 🎶 
This is the repository of our Project for the Machine Learning for Network Science (MLNS) course from CentraleSupélec by Chloé Daems, Amir Mahmoudi & Anne-Claire Laisney.

## Motivations ✍️

We want to create a Recommendation System applied to music by using the notions seen in the course. Our work was inspire by the *Katarya, R., Verma, O.P. Efficient music recommender system using context graph and particle swarm. Multimed Tools Appl 77, 2673–2687 (2018).* [paper](URL 'https://link.springer.com/article/10.1007/s11042-017-4447-x') which showed some great results. We are using the same dataset as them, data from the user.getRecentTracks of the [Last.fm](URL 'https://www.last.fm/api/show/user.getRecentTracks') API. 
We have two main tsv files that you can download [here](URL 'http://mtg.upf.edu/static/datasets/last.fm/lastfm-dataset-1K.tar.gz') :

* The *userid_profile.tsv* which regroups informations on the user (userid \t gender \t age \t country \t date of registration);
* The *userid_ ... _logs.tsv* which regroups informations on the log (userid \t timestamp \t artist-id \t artist-name \t track-id \t track-name)

The dataset regroups the whole listening habits (Jan, 27th 2008 till May, 5th 2009) for nearly 1,000 users, regrouping 19,150,868 logs.

## TODO LIST 💻
* Optimize the *get_only_top* function (too long) - if not possibile run it once and save in a file on a public drive - ❌
* Create new track-ids and artist-id with uuid library (some are missing and could make the *get_only_top* function faster) ❌
* Add the part of the day (morning / afternoon / night) or part of the week (week end / week day) nodes ❌
* Implement the different methods of the paper (select which method to try) ❌
* Compare results ❌
* Write the report ❌

## TO DO IF EXTRA TIME
* Recreate a more recent dataset with the same data architecture using the [Last.fm](URL 'https://www.last.fm/api/show/user.getRecentTracks') API ❌

