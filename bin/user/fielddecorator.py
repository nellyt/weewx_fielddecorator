from weewx.cheetahgenerator import SearchList
import weeutil.weeutil

class FieldDecorator(SearchList):
    """Field Decorator extension"""

    def __init__(self, generator):
        SearchList.__init__(self, generator)
        self.table_dict = generator.skin_dict['FieldDecorator']
 
    def __decoratorColorStub(self, type, value):
        table_options = weeutil.weeutil.accumulateLeaves(self.table_dict[type])
        table = zip(table_options['maxvalues'], table_options['colors'])
        value = self.__lookup(value, table)
        if value == "" :
            htmlLine = ""
        else :
            htmlLine ="background-color:%s" % value
        return htmlLine

    def __decoratorTextStub(self, type, value):
        table_options = weeutil.weeutil.accumulateLeaves(self.table_dict[type])
        table = zip(table_options['maxvalues'], table_options['text1'])
        htmlLine = self.__lookup(value, table)
        return htmlLine

    def get_extension_list(self, timespan, db_lookup):
        print "get_extension_list" # TODO remove

        search_list_extension = {'decorator_color'   : self.__decoratorColorStub,
                                 'decorator_text'    : self.__decoratorTextStub}
        return [search_list_extension]

    def __lookup(self, value, table):
        # print table
        if value is not None:
            for c in table:
                if (value <= float(c[0])):
                    retval = c[1]
                    break
        else:
            retval = "#err_None" # WHITE TODO decide what we return here ?
        return retval
