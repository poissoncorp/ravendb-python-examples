# region Usings
from ravendb import AbstractIndexCreationTask
from ravendb.documents.indexes.definitions import FieldIndexing

# endregion

from demo_example import Example, RunParamsBase
from models import LastFm


class RunParams(RunParamsBase):
    def __init__(self, search_term: str = None):
        self.search_term = search_term


# region Demo
# region Step_1
class Song_TextData(AbstractIndexCreationTask):
    # endregion
    def __init__(self):
        # region Step_2
        super().__init__()
        self.map = (
            "docs.LastFms.Select(song => new { "
            "    SongData = new object[] { "
            "        song.Artist, "
            "        song.Title, "
            "        song.Tags, "
            "        song.TrackId "
            "    } "
            "})"
        )
        # endregion

        # region Step_3
        self._index("SongData", FieldIndexing.SEARCH)
        # endregion


class FtsWithStaticIndexMultipleFields(Example):
    def run(self, run_params: RunParams):
        search_term = run_params.search_term
        Song_TextData().execute(self.document_store_holder.store())

        # region Demo
        with self.document_store_holder.store().open_session() as session:
            # region Step_4
            results = list(
                session.query_index_type(Song_TextData, LastFm).where_equals("SongData", search_term).take(20)
            )
            # endregion

        # endregion

        return results
