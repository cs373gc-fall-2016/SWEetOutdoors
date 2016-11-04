var app = angular.module("myApp", []);
app.controller("repeatController", function($scope) {
    $scope.records = [
    "Alfreds Futterkiste",
    "Berglunds snabbköp",
    "Centro comercial Moctezuma",
    "Ernst Handel",
  ]

  $scope.states = [

	  {
	  		name: 'Texas',
	  		description: 'Big',
	  		total_area: '10000',
	  		population: '1000000',
	  		highestPoint: '3000'
	  },
	  
	  {
	  		name: 'Florida',
	  		description: 'South',
	  		total_area: '5000',
	  		population: '400000',
	  		highestPoint: '2000'
	  },

	  {
	  		name: 'California',
	  		description: 'West',
	  		total_area: '8000',
	  		population: '2000000',
	  		highestPoint: '2500'
	  }	  

	]

  
});



