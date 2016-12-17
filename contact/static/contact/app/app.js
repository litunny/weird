angular.module('app', [])
.config(function ($interpolateProvider) {
      $interpolateProvider.startSymbol('<%');
      $interpolateProvider.endSymbol('%>');
})

.controller('ContactController', function($scope, $location) {
    $scope.Redirect = function(id) {
        window.location =  id + "/";
    }
})

;