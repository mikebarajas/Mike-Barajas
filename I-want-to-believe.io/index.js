// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $dateSearch = document.querySelector("#datetime");
var $citySearch = document.querySelector("#city");
var $stateSearch = document.querySelector("#state");
var $countrySearch = document.querySelector("#country");
var $shapeSearch = document.querySelector("#shape");
var $searchBtn = document.querySelector("#search");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);

// Set filteredAddresses to data initially
var filteredUFO = ufoData;

// renderTable renders the filteredAddresses to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filteredUFO.length; i++) {
    // Get get the current address object and its fields
    var UFO = filteredUFO[i];
    var fields = Object.keys(UFO);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the address object, create a new cell at set its inner text to be the current value at the current address's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = UFO[field];
    }
  }
}

  function handleSearchButtonClick() {
    filteredUFO = ufoData
    // create a list of searches
    var searches ={
      dateTime: $dateSearch.value, 
      city: $citySearch.value.trim().toLowerCase(), 
      state: $stateSearch.value.trim().toLowerCase(), 
      country: $countrySearch.value.trim().toLowerCase(), 
      shape: $shapeSearch.value.trim().toLowerCase()
    }
    // filter through keys and values
    var searchParameter = Object.keys(searches)
    var searchFilter = Object.values(searches)
    filteredUFO = filteredUFO.filter(x => {
      for (i = 0; i < 5; i++) {
        if (searchFilter[i] !=="") {
            if (x[searchParameter[i]] !== searchFilter[i]){
              return false  
            }
        }
      } 
      return true 
    })
    renderTable();
  }
// Render the table for the first time on page load
renderTable();


