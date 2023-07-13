from demo_example import Example, RunParamsBase

# region Usings
from ravendb import AbstractIndexCreationTask


class RunParams(RunParamsBase):
    def __init__(self, country: str):
        self.country = country


# region Demo
# region Step_1
class Employees_ByCountry(AbstractIndexCreationTask):
    # endregion
    def __init__(self):
        # region Step_2
        super().__init__()
        self.map = (
            "docs.Employees.Select(employee => new { "
            "    Country = employee.Address.Country, "
            "    CountryCount = 1 "
            "})"
        )
        # endregion
        # region Step_3
        self.reduce = (
            "results.GroupBy(result => result.Country).Select(g => new { "
            "    country = g.Key, "
            "    country_count = Enumerable.Sum(g, x => x.CountryCount) "
            "})"
        )
        # endregion

    # region Step_4
    class Result:
        def __init__(self, country: str, country_count: int):
            self.country = country
            self.country_count = country_count

    # endregion


class MapReduceIndex(Example):
    def run(self, run_params: RunParams) -> int:
        country = run_params.country
        # region Demo
        with self.document_store_holder.store().open_session() as session:
            # region Step_5
            query_result = (
                session.query_index_type(Employees_ByCountry, Employees_ByCountry.Result)
                .where_equals("Country", country)
                .first()
            )
            number_of_employees_in_country = query_result.country_count if query_result is not None else 0
            # endregion
        # endregion

        return number_of_employees_in_country
