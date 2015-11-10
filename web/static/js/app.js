
var app = angular.module('schedule', []);

app.controller('scheduleCtrl', function($scope, $http) {
    $scope.schedule = [];
    $scope.loadSchedule = function () {
        var httpRequest = $http({
            method: 'GET',
            url: '/get-schedule/',
        }).success(function (data, status) {
            $scope.schedule = data.schedule;
        });
    };
    $scope.deleteFromSchedule = function (id) {
        var index = 0;
        for (var i = 0; i < $scope.schedule.length; i++) {
            if($scope.schedule[i].id == id) {
                index = i;
                break;
            }
        }
        $scope.schedule.splice(index, 1);
    }
});