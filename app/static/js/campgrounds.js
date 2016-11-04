var app = angular.module("myApp", []);
app.controller("repeatController", function($scope) {
    $scope.records = [
    "Alfreds Futterkiste",
    "Berglunds snabbköp",
    "Centro comercial Moctezuma",
    "Ernst Handel",
  ]

  $scope.camggrounds = [

	  {
		name: 'Yosemite',
		description: 'In California',
		cost: '10000',
	    longitude = '123'
		latitude = '23'
	    accessibilty = true
	    reservation_url = 'thisisaurl.com'
	    email = 'thisisanemail@hotmail.com'
	    zipcode = 78700
	    state = 'California'
	  },
	  
	  {
	  	name: 'BearCreek',
		description: 'In Texas',
		cost: '10000',
	    longitude = '123'
		latitude = '23'
	    accessibilty = true
	    reservation_url = 'thisisaurl.com'
	    email = 'thisisanemail@hotmail.com'
	    zipcode = 78700
	    state = 'Texas '
	  },

	  {
	    name: 'notBearCreek',
		description: 'In Texas',
		cost: '10000',
	    longitude = '123'
		latitude = '23'
	    accessibilty = true
	    reservation_url = 'thisisaurl.com'
	    email = 'thisisanemail@hotmail.com'
	    zipcode = 78700
	    state = 'Texas '
	  }	  

	]

  
});