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
    $scope.user_id = 1;
    $scope.user_ids = [];
    $scope.user_index = 0;
    $scope.loadRecommendations = function (user_id) {
        var httpRequest = $http({
            method: 'GET',
            url: '/get-recommendations/' + user_id,
        }).success(function (data, status) {
            $scope.recoms = data.recoms;
            $scope.history = data.history;
            $scope.user_ids = data.user_ids;
        });
    };
    $scope.nextUser = function (incr) {
        $scope.user_index += incr;
        if ($scope.user_index >= $scope.user_ids.length) {
            $scope.user_index = $scope.user_ids.length - 1;
        }
        if ($scope.user_index <= 0) {
            $scope.user_index = 0;
        }
        $scope.user_id = $scope.user_ids[$scope.user_index];
        $scope.loadRecommendations($scope.user_id);
    }
    // at the bottom of your controller
    var init = function () {
       // check if there is query in url
       // and fire search in case its value is not empty
       $scope.loadRecommendations($scope.user_id);
    };
    // and fire it after definition
    init();
});