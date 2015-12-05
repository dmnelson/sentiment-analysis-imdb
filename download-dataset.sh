#!/bin/bash
echo "### Downloading Andrew Maas' 'Large Movie Review Dataset' - http://ai.stanford.edu/~amaas/data/sentiment/"
echo " "
echo " "
curl http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz | tar -xz  -C dataset --strip-components 1
