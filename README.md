# SocialMediaPlatform

go to /venv/bin and type source activate

go to SocialMediaPlatform folder and type:

export FLASK_APP=socialMediaPlatform.py
flask run

and then copy/paste the url and you should be good to go!


###Workflow
<pre>
  Update local repo
    - git checkout master
    - git pull origin master
  Create working branch
    - git checkout -b WORKING_BRANCH
  Make changes on WORKING_BRANCH
  Add and commit changes once satisfied
    - git add /files/you/changed
    - git commit -m "Message describing changes"
  Push changes to master
    - git checkout master
    - git pull origin master
    - git merge WORKING_BRANCH
    - git push origin master
</pre>
