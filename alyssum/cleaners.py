import re


class Cleaner(object):
    @staticmethod
    def clean(string):
        if string != '#':
            result = re.sub("[^A-za-z0-9 ]", "", string)
            result = "_".join(result.split())
            match = re.search("^([0-9]+)(.*)", result)
            if match:
                result = "_" + result

            result = result.lower()
            return result
        else:
            return '#'


class Convert(object):

    @staticmethod
    def str_type(string):
        result=(None, None, None)
        regex_list={
            'none_big_formal'           :'^((?:[A-Z])(?:[a-z|0-9]?)+)+$',         # AaaaAaaa
            'none_little_formal'        :'^([a-z]+)((?:[A-Z])(?:[a-z|0-9]?)+)+$', # aaaaAaaa
            'underline_little_unformal' :'^(?:[a-z])(_?(?:[a-z|0-9])+)+$',        # aaaa_aaaa
            'underline_little_formal'   :'^(?:[a-z])((_[A-Z])?(?:[a-z|0-9])*)+$', # aaaa_Aaaa
            'underline_big_formal'      :'^(?:[A-Z])((_[A-Z])?(?:[a-z|0-9])*)+$', # Aaaa_Aaaa
            'hyphen_little_unformal'    :'^(?:[a-z])(-?(?:[a-z|0-9])+)+$',        # aaaa-aaaa
            'hyphen_little_formal'      :'^(?:[a-z])((-[A-Z])?(?:[a-z|0-9])*)+$', # aaaa-Aaaa
            'hyphen_big_formal'         :'^(?:[A-Z])((-[A-Z])?(?:[a-z|0-9])*)+$', # Aaaa-Aaaa
            'space_little_unformal'     :'^(?:[a-z])( ?(?:[a-z|0-9])+)+$',        # aaaa aaaa
            'space_little_formal'       :'^(?:[a-z])(( [A-Z])?(?:[a-z|0-9])*)+$', # aaaa Aaaa
            'space_big_formal'          :'^(?:[A-Z])(( [A-Z])?(?:[a-z|0-9])*)+$', # Aaaa Aaaa

        }

        for name, regex in regex_list.items():
            match = re.search(regex,string)
            if match:
                result = tuple(name.split('_'))
        return result
    @staticmethod
    def none_to_underline(string):
        filter1 = re.compile(r'(.)([A-Z][a-z]+)')
        filter2 = re.compile(r'([a-z0-9])([A-Z])')

        return filter2.sub(r'\1_\2', filter1.sub(r'\1_\2', string))

    @staticmethod
    def hyphen_to_underline(string):
        return string.replace('-', '_')

    @staticmethod
    def space_to_underline(string):
        return string.replace(' ', '_')

    @staticmethod
    def formal_to_unformal(string):
        return string[0]+string[1:].lower()

    @staticmethod
    def big_to_little(string):
        return string[0].lower()+string[1:]

