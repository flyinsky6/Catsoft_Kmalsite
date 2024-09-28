# Catsoft_Kmalsite
Catsoft_Kmalsite, a novel malonylation sites prediction model based on ensemble learning and feature fusion, which  utilized tools like Alphafold2 to obtain the tertiary structure information of proteins, and adopted CTDC, EAAC and EGAAC to characterise the sequence and physicochemical property features of proteins, then used CatBoost algorithm to construct two base classifiers for the above features with Bayesian optimization applied to tune these classifiers, and finally employed soft voting strategy to integrate the results. A large number of ablation experiments and research results show that the Catsoft_Kmalsite model has good robustness and generalisation ability.

# Requirement
numpy~=1.23.5
pandas~=1.5.3
streamlit~=1.21.0
requests~=2.28.2
pillow~=9.4.0
matplotlib~=3.7.1
catboost~=1.1.1
sklearn~=0.0.post1
scikit-learn~=1.2.2

# Dataset
This dataset is sourced from the CPLM 4.0 database. After removing redundant proteins using CD-HIT (threshold of 40%), we obtained a total of 3541 malonylation modification sites from 1262 proteins. Then, using a sliding window strategy, we selected 16 amino acids on each side of lysine to form a positive sample with a length of 33. We use the same construction method for negative samples and employ downsampling techniques to obtain a balanced dataset.

# Catsoft_Kmalsite platform
The Catsoft_Kmalsite user interaction platform, dedicated to predicting lysine malonylation sites in mice, was implemented using the Streamlit framework.
Run home.py to enter the platform and switch to the web server page via the left column of the page, where users only need to submit a protein sequence file in FASTA format and a protein structure file in DSSP format to obtain the prediction results.

# Contact
Feel free to contact us if you nedd any help: flyinsky6@189.cn
