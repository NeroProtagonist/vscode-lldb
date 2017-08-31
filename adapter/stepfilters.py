import re


class StepFilter(object):
    def __init__(self):
        self.combined_regex = None

    def set_filters(self, filterArray):
        validFilters = []
        if filterArray is not None:
            for filt in filterArray:
                try:
                    re.compile(filt)
                    validFilters.append(filt)
                except re.error:
                    # TODO: Inform user
                    pass

        if len(validFilters) != 0:
            self.combined_regex = "(" + ")|(".join(validFilters) + ")"

    def getFilters(self):
        return self.combined_regex;
