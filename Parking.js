let slots = 10;
let vehicles = [];

function parkVehicle() {

    let vehicle =
    document.getElementById("vehicle").value;

    if(vehicle === ""){
        alert("Enter Vehicle Number");
        return;
    }

    if(slots > 0){

        vehicles.push(vehicle);
        slots--;

        updateDisplay();

        document.getElementById("vehicle").value = "";
    }
    else{
        alert("Parking Full!");
    }
}

function removeVehicle(){

    let vehicle =
    document.getElementById("vehicle").value;

    let index = vehicles.indexOf(vehicle);

    if(index > -1){
        vehicles.splice(index,1);
        slots++;
        updateDisplay();
    }
    else{
        alert("Vehicle Not Found");
    }
}

function updateDisplay(){

    document.getElementById("slots").innerText = slots;

    let list =
    document.getElementById("vehicleList");

    list.innerHTML = "";

    vehicles.forEach(vehicle => {

        let li =
        document.createElement("li");

        li.textContent = vehicle;

        list.appendChild(li);
    });
}