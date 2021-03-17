import requests
import json
import imdb_db #olusturulan veritabani

def tvShowsNFilms():
    #getTitle fonksiyonu parametre olarak aldigi id'leri kullanarak elde ettigi veriden dizi ve filmlerin 
    #ismini cekip return ediyor.
    def getTitle(x):


        url = "https://imdb8.p.rapidapi.com/title/get-plots"

        querystring = {"tconst": x}

        headers = {
            'x-rapidapi-key': "3ee414594bmsh95d08663d649adap12c8cbjsnf6e902276553",
            'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.text)

        return(result['base']['title'])
    


    #####
    #bu kisimda imdb'nin get-rated-tv-shows endpointi kullanarak id'lerin bir kismini elde ettik ve 
    #fonksiyona gonderdik.
    url = "https://imdb8.p.rapidapi.com/title/get-top-rated-tv-shows"

    headers = {
        'x-rapidapi-key': "3ee414594bmsh95d08663d649adap12c8cbjsnf6e902276553",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response1 = requests.request("GET", url, headers=headers)
    result1 = json.loads(response1.text)
    for i in range(0,5):
        name1 = getTitle(result1[i]["id"][7:-1]) 
        #result1'den donen json verisinden id'yi cektik: "id": /title/tt0349793-> tt03459793
        imdb_db.insertName(name1,0)
        #veritabanina veriyi ekledik


    #####
    #get-most-populer-movies endpointi
    url = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"

    querystring = {"homeCountry":"US","purchaseCountry":"US","currentCountry":"US"}

    headers = {
        'x-rapidapi-key': "3ee414594bmsh95d08663d649adap12c8cbjsnf6e902276553",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response2 = requests.request("GET", url, headers=headers, params=querystring)
    result2 = json.loads(response2.text)
    for i in range(0,5):
        name2 = getTitle(result2[i][7:-1])
        imdb_db.insertName(name2,0)


    #####
    #get-coming-soon-tv-shows endpoint'i

    url = "https://imdb8.p.rapidapi.com/title/get-coming-soon-tv-shows"

    querystring = {"currentCountry":"US"}

    headers = {
        'x-rapidapi-key': "3ee414594bmsh95d08663d649adap12c8cbjsnf6e902276553",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response3 = requests.request("GET", url, headers=headers, params=querystring)
    result3 = json.loads(response3.text)
    for i in range(0,5):
        name3 = getTitle(result3[i][7:-1])
        imdb_db.insertName(name3,0)

