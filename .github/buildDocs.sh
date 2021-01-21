#!/bin/bash
set -x
################################################################################
# File:    buildDocs.sh
# Purpose: Script that builds our documentation using jupyter-book and updates GitHub
#          Pages. This script is executed by:
#            .github/workflows/docs_pages_workflow.yml
################################################################################
 
###################
# INSTALL DEPENDS #
###################
 
apt-get update
#apt-get -y install git rsync python3-sphinx python3-sphinx-rtd-theme
apt-get -y install git rsync python3-pip 
pip3 install -U sphinx
#pip3 install -U sphinx-rtd-theme
pip3 install -U jupyter-book

#####################
# DECLARE VARIABLES #
#####################
 
pwd
ls -lah
export SOURCE_DATE_EPOCH=$(git log -1 --pretty=%ct)
 
##############
# BUILD DOCS #
##############
# build our documentation with sphinx (see docs/conf.py)
# * https://www.sphinx-doc.org/en/master/usage/quickstart.html#running-the-build

cd edunum-sec2/config/eleve/

rm -rf _build/
jupyter-book build .

cd ../../..

cd edunum-sec2/config/maitre/

rm -rf _build/
jupyter-book build .

cd ../../..

# > make_log.txt  2>&1
#cp make_log.txt _build/html/

#######################
# Update GitHub Pages #
#######################
 
git config --global user.name "${GITHUB_ACTOR}"
git config --global user.email "${GITHUB_ACTOR}@users.noreply.github.com"

# go into temporary folder and create copies of builds
docroot=`mktemp -d`
#rsync -av "edunum-sec2/config/eleve/_build/html/" "${docroot}/"

mkdir "${docroot}/eleve"
rsync -av "edunum-sec2/config/eleve/_build/html/" "${docroot}/eleve/"
mkdir "${docroot}/maitre"
rsync -av "edunum-sec2/config/maitre/_build/html/" "${docroot}/maitre/"

pushd "${docroot}"
 
git init
git remote add deploy "https://token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
git checkout -b gh-pages
 
# add .nojekyll to the root so that github won't 404 on content added to dirs
# that start with an underscore (_), such as our "_content" dir..
touch .nojekyll
 
# Add default README
cat > README.md <<EOF
# Readme autocompilation

This documentation is the result of the auto compilation of the master branch using github workflows.
EOF

 
# copy the resulting html pages built from sphinx above to our new git repo
git add .
 
# commit all the new files
msg="Updating Docs for commit ${GITHUB_SHA} made on `date -d"@${SOURCE_DATE_EPOCH}" --iso-8601=seconds` from ${GITHUB_REF} by ${GITHUB_ACTOR}"
git commit -am "${msg}"
 
# overwrite the contents of the gh-pages branch on our github.com repo
git push deploy gh-pages --force
 
popd # return to main repo sandbox root
 
# exit cleanly
exit 0
