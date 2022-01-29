const axios = require("axios");

const UD_DEFINE_URL = 'https://api.urbandictionary.com/v0/define?term=';
const UD_RANDOM_URL = 'https://api.urbandictionary.com/v0/random'

function parse_urban_json(url) {
    let result = [];
    data = axios.get(url);
    if (json_response === undefined || json_response == "ERROR") {
        throw "Urb: empty results from the Urban Dictionary API";
    } else if (!(json_response) || json_response.getOwnPropertyNames().length == 0) {
        return result;
    };

    for (var definition in data["list"]) {
        result.push({
            "word": definition["word"],
            "definition": definition["definition"],
            "example": definition["example"],
            "upvotes": definition["thumbs_up"],
            "downvotes": definition["thumbs_down"]
        });
    };
    return result;
};

function define(term) {
    json_response = parse_urban_json(`${UD_DEFINE_URL}${term.replace(" ", "+")}`);
    return json_response;
};

function random() {
    json_response = parse_urban_json(UD_RANDOM_URL);
    return json_response;
};
