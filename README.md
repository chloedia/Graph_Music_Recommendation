![cover](cover_MLNS.jpg)
# Graph Music Recommendation 🎶 
This is the repository of our Project for the Machine Learning for Network Science (MLNS) course from CentraleSupélec by Chloé Daems, Amir Mahmoudi & Anne-Claire Laisney.

## Motivations ✍️

We want to create a Recommendation System applied to music by using the notions seen in course. Our work was inspired by the *Katarya, R., Verma, O.P. Efficient music recommender system using context graph and particle swarm. Multimed Tools Appl 77, 2673–2687 (2018).* [paper](https://link.springer.com/article/10.1007/s11042-017-4447-x) which showed some great results. We are using the same dataset as them i.e. data fetched with the user.getRecentTracks request at the [Last.fm](https://www.last.fm/api/show/user.getRecentTracks) API. 
We have two main tsv files that you can download [here](http://mtg.upf.edu/static/datasets/last.fm/lastfm-dataset-1K.tar.gz) :

* The *userid_profile.tsv* which regroups informations on the user (userid \t gender \t age \t country \t date of registration);
* The *userid_ ... _logs.tsv* which regroups informations on the log (userid \t timestamp \t artist-id \t artist-name \t track-id \t track-name)

The dataset regroups the whole listening habits (Jan, 27th 2008 till May, 5th 2009) of nearly 1,000 users, regrouping 19,150,868 logs.

## VIDEO PRESENTATION 💻
[Here](https://www.youtube.com/watch?v=lA3-o_CAF0s) you can find the link to our project presentation.

