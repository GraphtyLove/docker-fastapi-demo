
city_mapper = {
    "bruxelles": 1,
    "charleroi": 2,
    "ixelles": 3,
}


def preprocess(data: dict) -> dict:
    print("preprocessing data...")
    city = data['city']
    data['city'] = city_mapper[city]
    print("data preprocessed!")
    return data