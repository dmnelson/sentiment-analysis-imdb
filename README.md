# Sentiment Analysis on IMDB Reviews

https://sent-an.herokuapp.com/

This is a simple project created with the intention of putting into practice knowledge learned 
about Machine Learning, Natural Language Processing and Sentiment Anaylisis.

It consists on a recurrent neural network (LSTM) built using Keras that was trained on the IMDB
reviews database. The dataset used for this was the one made available by Andrew Maas (http://ai.stanford.edu/~amaas/data/sentiment/).

### Running it locally

There is a shell script on the root of the project (`download-dataset.sh`) 
that will download the data into the approriate directoy.

Running it can be done by `python sentiment_analysis.py` or using Waitress `waitress-serve sentiment_analysis:app`.

### References
**A. L. Maas, R. E. Daly, P. T. Pham, D. Huang, A. Y. Ng, and C. Potts**. Learning word vectors for sentiment analysis.
In *Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies*, 
pages 142-150, Portland, Oregon, USA, June 2011. Association for Computational Linguistics [(view online)](http://www.aclweb.org/anthology/P11-1015).
