
var search = document.getElementById("search");
var imgArray = document.getElementsByClassName("banner");
var infoArray = document.getElementsByClassName("desc");

search.addEventListener(("keyup"), function(event) {
    console.log('check');
    if (event.keyCode === 13) {
      console.log("start fetching");
      fetchFromAPI(search.value)
          .then(function(fromDB){
              console.log("results :",fromDB);
              var fetchedData = fromDB.filter(fromDB=>fromDB.backdrop_path);
              for(let i=0; i<8;i++){
                  if(fetchedData[i].backdrop_path===undefined){
                      i++;
                  }
                  
                  imgArray[i].src="https://image.tmdb.org/t/p/w500"+fetchedData[i].backdrop_path;
                  infoArray[i].innerHTML=(`<strong>${fetchedData[i].original_title}</strong>
                                        <br><br>
                                        World Premiere : ${fetchedData[i].release_date}<br>
                                        IMDB : ${fetchedData[i].vote_average}<br>`).fontcolor("white");
              }
          })
          .catch(err=>console.error(err));
    }
  }); 


const fetchFromAPI= async function(query){ 
    const apikey=await fetch(`https://api.themoviedb.org/3/search/movie?api_key=4be8a61c04069692ec71d744ddc0b88f&query=${query}`);
    const data=await apikey.json();
    if(apikey.status!==200){
        alert('Not able to process your request at the moment. Status ${response.status}');
    }
    return data.results;
}

