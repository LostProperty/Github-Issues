def get_label(github_repo, label_text):
    labels = github_repo.get_labels()
    #labels = github_repo.get_labels(name='CMS') # Not supported, add add patch
    for label in labels:
        if label.name == label_text:
            return label
    return False
