/*
This application displays user recommendations and his viewing history.

Views:
- user recoms vs. history
( can rate recom, add comment )
- show reviewed recoms
*/
var app = angular.module('recom_review', []);

app.controller('reviewCtrl', function($scope, $http) {
    $scope.recoms = [];
    $scope.user_id = 0;
    $scope.loadRecommendations = function (user_id) {
        var httpRequest = $http({
            method: 'GET',
            url: '/get-recommendations/' + user_id,
        }).success(function (data, status) {
            $scope.recoms = data.recoms;
            $scope.history = data.history;
        });
    };
    // at the bottom of your controller
    var init = function () {
       // check if there is query in url
       // and fire search in case its value is not empty
       $scope.loadRecommendations(0);
    };
    // and fire it after definition
    init();
});