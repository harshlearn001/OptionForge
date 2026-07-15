from optionforge.repository.repository_exception import *


def test_exception_inheritance():

    assert issubclass(
        RepositoryFileNotFoundError,
        RepositoryError,
    )

    assert issubclass(
        RepositoryValidationError,
        RepositoryError,
    )

    assert issubclass(
        RepositoryCacheError,
        RepositoryError,
    )
