# region Usings
from ravendb import AbstractIndexCreationTask

# endregion

from demo_example import Example, RunParamsBase
from models import Category


class RunParams(RunParamsBase):
    def __init__(self, search_term: str = None):
        self.search_term = search_term


# region Demo
# region Step_1
class Categories_DescriptionText(AbstractIndexCreationTask):
    # endregion
    def __init__(self):
        # region Step_2
        super().__init__()
        self.map = "docs.Categories.Select(category => new { " "    CategoryDescription = category.Description " "})"


class FtsWithStaticIndexSingleField(Example):
    def run(self, run_params: RunParams):
        search_term = run_params.search_term

        # region Demo
        with self.document_store_holder.store().open_session() as session:
            # region Step_4
            categories_with_search_term = list(
                session.query_index_type(Categories_DescriptionText, Category).where_equals(
                    "CategoryDescription", search_term
                )
            )
            # endregion

        # endregion

        return categories_with_search_term
