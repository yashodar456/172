function searchMovie(){

    let movie = document.getElementById("movieInput").value;

    let result = document.getElementById("result");

    if(movie === ""){
        result.innerHTML = " Please enter a movie name.";
    }
    else{
        result.innerHTML = `
            <h3>${movie}</h3>
            <p> Rating: 8.5/10</p>
            <p> Genre: Action / Drama</p>
            <p>Status: Available</p>
        `;
    }
}