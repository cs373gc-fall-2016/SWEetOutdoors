var app = angular.module("myApp", []);
app.controller("repeatController", function($scope) {
    $scope.records = [
    "Alfreds Futterkiste",
    "Berglunds snabbköp",
    "Centro comercial Moctezuma",
    "Ernst Handel",
  ]

  $scope.events = [

	  {
		latitude = '12'
        longitude = '32'
        topics = "topic"
        startDate = "startDate"
        endDate = "endDate"
        picUrl = "picUrl"
        eventUrl = "eventUrl"
        orgName = "orgName"
        contactPhoneNum = "contactPhoneNum"
        orgUrl = "orgUrl"
        city = "city"
        zipcode = 78700
	  },
	  
	  {
	  	latitude = '12'
        longitude = '32'
        topics = "topic"
        startDate = "startDate"
        endDate = "endDate"
        picUrl = "picUrl"
        eventUrl = "eventUrl"
        orgName = "orgName"
        contactPhoneNum = "contactPhoneNum"
        orgUrl = "orgUrl"
        city = "city"
        zipcode = 78700
	  },

	  {
	    latitude = '12'
        longitude = '32'
        topics = "topic"
        startDate = "startDate"
        endDate = "endDate"
        picUrl = "picUrl"
        eventUrl = "eventUrl"
        orgName = "orgName"
        contactPhoneNum = "contactPhoneNum"
        orgUrl = "orgUrl"
        city = "city"
        zipcode = 78700
	  }	  

	]

  
});