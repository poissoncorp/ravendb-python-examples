from demo_example import Example, RunParamsBase


class RunParams(RunParamsBase):
    def __init__(
        self,
        document_id: str,
        attachment: bytes,
        attachment_name: str,
        content_type: str,
    ):
        self.document_id = document_id
        self.attachment = attachment
        self.attachment_name = attachment_name
        self.content_type = content_type


class StoreAttachment(Example):
    _DEFAULT_DOCUMENT_ID = "companies/2-A"

    def run(self, run_params: RunParams) -> None:
        document_id = run_params.document_id or self._DEFAULT_DOCUMENT_ID
        attachment_name = run_params.attachment_name
        content_type = run_params.content_type
        attachment = run_params.attachment

        # region Demo
        with self.document_store_holder.store().open_session() as session:
            # region Step_1
            session.advanced.attachments.store(document_id, attachment_name, attachment, content_type)
            # endregion

            # region Step_2
            session.save_changes()
            # endregion
        # endregion
