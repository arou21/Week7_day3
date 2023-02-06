function getPokemon(name){
    let url = "https://pokeapi.co/api/v2/pokemon/" + name
    fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        },
    })
    .then(response => response.json())
    .then(response => {
        console.log(JSON.stringify(response))
        let result = response 
        ability = result['abilities'][0]['ability']['name']
        name = result['forms'][0]['name']
        baseExperience = result['base_experience']

        subUrl = result['forms'][0]['url']
        fetch(subUrl, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            },
        })
        .then(response => response.json())
        .then(response => {
            let subResult = response
            image = subResult['sprites']['front_default']
            console.log(name,ability, baseExperience, image )
        
        })



        
    })
}

getPokemon("ditto");
getPokemon("bulbasaur");
getPokemon("kakuna");
getPokemon("rattata");
getPokemon("raticate")