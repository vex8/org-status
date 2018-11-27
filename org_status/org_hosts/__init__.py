class OrgHost:
    """
    TODO: StatusProvider should easily be swapable.
    TODO: Lazy authenticate to facilitate caching support.
    TODO: Cache list of repo's in an org.
    TODO: Add proper error messages eg: org not found.
    TODO: Support private org/repositories.
    """
    HostName = None
    StatusProvider = None

    def __init__(self, status_provider=None, verbose=False, **kargs):
        self.StatusProvider = status_provider or self.StatusProvider
        if self.StatusProvider is None:
            raise NotImplementedError()

        self.verbose = verbose

    def print_status(self, repo_url):
        if self.verbose:
            print('processing {url}'.format(url=repo_url))

    def process_repository(self, repo):
        raise NotImplementedError()

    @classmethod
    def get_host_status(cls):
        raise NotImplementedError()

    @property
    def repositories(self):
        raise NotImplementedError()


class RepoStatus:

    def __init__(self, repo_url, repo_status):
        self.repo_url = repo_url
        self.repo_status = repo_status


def get_all_supported_hosts():
    from org_status.org_hosts.github import GitHubOrg
    from org_status.org_hosts.gitlab import GitLabOrg

    return (
        GitHubOrg,
        GitLabOrg,
    )
