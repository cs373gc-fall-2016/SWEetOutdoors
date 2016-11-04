var app = angular.module("myApp", []);
app.controller("repeatController", function($scope) {
    $scope.records = [
    "Alfreds Futterkiste",
    "Berglunds snabbköp",
    "Centro comercial Moctezuma",
    "Ernst Handel",
  ]

  $scope.parks = [

	  {
	  		parkName: 'Death Valley National Park',
	  		price: '$10',
	  		hours: '8 am-10pm',
	  		website: 'wwww.something.com',
	  		upcomingEvent: 'asdf',
	  		bestCamground: 'sadf'
	  },
	  
	  {
	  		parkName: 'Death Valley National Park',
	  		price: '$10',
	  		hours: '8 am-10pm',
	  		website: 'wwww.something.com',
	  		upcomingEvent: 'asdf',
	  		bestCamground: 'sadf'
	  },

	  {
	  		parkName: 'Death Valley National Park',
	  		price: '$10',
	  		hours: '8 am-10pm',
	  		website: 'wwww.something.com',
	  		upcomingEvent: 'asdf',
	  		bestCamground: 'sadf'
	  }	  

	]

  
});



