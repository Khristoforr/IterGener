import json

class CoutryIterator():
    def __init__(self, path_to_write):
        self.path_to_write = path_to_write
        print(f'Информация о странах записана в файле {self.path_to_write}')

    def get_country_list(self):
        country_list = []
        with open('countries.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for i in range(len(data)):
                country_list.append(data[i]['name']['common'])
        return country_list

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        try:
            self.cursor += 1
            wiki_link = f'https://en.wikipedia.org/wiki/{str(self.get_country_list()[self.cursor]).replace(" ", "_")}'
            with open(self.path_to_write, 'a', encoding='utf-8') as f:
                f.write(f'{self.get_country_list()[self.cursor]} - {wiki_link}\n')
                return f'Cтрана {self.get_country_list()[self.cursor]} размещена по ссылке {wiki_link}'
        except IndexError:
            raise StopIteration

def main():
    for coutry in CoutryIterator('Task1'):
        print(coutry)

if __name__ == '__main__':
    main()