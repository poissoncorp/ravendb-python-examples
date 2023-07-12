from database import DocumentStoreHolder


class RunParams:
    def __init__(self, document_id: str):
        self.document_id = document_id


def run(run_params: RunParams) -> None:
    document_id = run_params.document_id

    # region Demo
    with DocumentStoreHolder.document_store().open_session() as session:
        # region Step_1
        session.delete(document_id)
        # endregion

        # region Step_2
        session.save_changes()
        # endregion

    # endregion
