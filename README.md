# Chunk-file-team-45

## Project Stack
- Python
- Django
- Javascript
- CSS
- HTML

## Collaborating Guidelines

The following are the  guidelines for collaborating on this project:

### For FE and BE guys

1. Clone, don't fork the repository


2. To clone the repository to your local machine on your desktop, 
open command prompt and run: (Be on your desktop directory in your command prompt)

```bash
git clone https://github.com/zuri-training/Chunk-file-team-45.git
```

3. Change to the project directory you just cloned

```bash
cd Chunk-file-team-45
```

### Only BE guys
4. Create a virtual environment for the project and make sure to activate it.

```bash
python -m venv chucky_env
```

5. Change to the project directory folder
```bash
cd chucky
```

### For FE and BE guys

6. Checkout Your Feature Branch

Feature Branching Workflow means you create a new branch for every feature or issue you are working on.
It is a good practice for the branch name to reflect the issue being solved.
So if an issue title is **Update ReadMe.md** then our branch name would be **update-readme**.
create and checkout feature branch by running:

```bash
git checkout -b feature-branch-name
```

### Only BE guys

7. Setup Development Environment, run:

```bash
pip install -r requirements.txt
python manage.py migrate

```
Incase someone installs new package and libs, run:

```bash
pip freeze > requirements.txt
```

### for FE and BE guys

8. After fixing the issue or adding the features, commit the changes and push them to the feature branch of your remote origin

```bash
git add *
git commit -m "descriptive commit message"
git push origin feature-branch-name
```

9. Login to your github account, go to the repo and make a pull request.

### Only FE guys

- Change directory to your workstation and continue from there.

```bash
cd frontend
```