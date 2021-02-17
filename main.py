import hashlib
from generator import Countries_gen

if __name__ == '__main__':

    counter = 0
    country_reader = Countries_gen('countries.json')
    with open('output.txt', 'w', encoding='utf8') as file:
        for country in country_reader:
            counter += 1
            file.write(f'{country} - https://wikipedia.org/wiki/{country.replace(" ", "_")}\n')


    def countryReaderIter(filename: str):

        with open(filename, 'r', encoding='utf8') as json_file:
            while True:
                hash = json_file.readline()
                if hash:
                    yield hash
                else:
                    break


    counter = 0
    for country in countryReaderIter('output.txt'):
        counter += 1
        print(hashlib.md5(country.encode('utf8')).hexdigest())