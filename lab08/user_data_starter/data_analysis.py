import re

class UserData:
    def __init__(self, input_data):
        data_list = input_data.split(",")
        self.email = data_list[3]
        self.languague = data_list[-1]

    def __repr__(self):
        return f"({self.email}, {self.languague})"

class DataAnalysis:


    def __init__(self, file):
        # TODO: set up the necessary instance variables
        self.read_data(file)

    def read_data(self, file_name):
        # TODO: read the data and get the counts
        self.email = {}
        self.language = {}
        
        try:
            f = open(file_name, "r")
        except FileNotFoundError:
            print("Can't find", file_name)
            return
        
        lines = f.readlines()
        
        for line in lines[1:]:
            line = line.strip("\n")
            user = UserData(line)
            find_dot = user.email.rfind(".")
            if len(user.email[find_dot+1:]) == 2:
                key = user.email[find_dot+1:]
                if key in self.email:
                    self.email[key] += 1
                else:
                    self.email[key] = 1
            lang_key = user.languague
            
            if lang_key in self.language:
                self.language[lang_key] += 1
            else:
                self.language[lang_key] = 1


    # TODO:
    # Implement top_n_lang_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing languages
    # and their frequencies in the data, ordered from
    # highest frequency to lowest.
    def top_n_lang_freqs(self, num):
        
        language_by_count = sorted(
            self.language.items(),
            key=lambda x: x[1],
            reverse=True
        )
        lang_display = language_by_count[:num]
        total = 0
        for lang, count in self.language.items():
            total += count
        ret = []
        for lang, count in lang_display:
            ret.append((lang, count/total))
        return ret 
    # TODO:
    # Implement top_n_country_tlds_freqs()
    # Should take a number N as an argument and return
    # an N-length list of tuples representing country (2-letter)
    # top-level domain identifiers (e.g. 'jp', 'uk', 'cn', 'ca')
    # and their frequencies as email domains the data, ordered 
    # from highest frequency to lowest.
    def top_n_country_tlds_freqs(self, num):
        country_by_count = sorted(
            self.email.items(),
            key=lambda x: x[1],
            reverse=True
        )
        country_display = country_by_count[:num]
        total = 0
        for country, count in self.email.items():
            total += count
        ret = []
        for country, count in country_display:
            ret.append((country, count/total))
        return ret 
