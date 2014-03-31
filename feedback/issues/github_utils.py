def github_get_label(github_repo, label_text):
    """
    Return a github issue object for supplied label_text
    """
    labels = github_repo.get_labels()
    #labels = github_repo.get_labels(name='CMS') # Not supported, add add patch
    for label in labels:
        if label.name == label_text:
            return label
    return False


def github_get_milestone(github_repo, milestone_title):
    """
    Return a github milestone object for supplied label_text
    """
    milestones = github_repo.get_milestones()
    for milestone in milestones:
        if milestone.title == milestone_title:
            return milestone
    return False
