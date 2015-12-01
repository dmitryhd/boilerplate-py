
var app = angular.module('schedule', []);

getScheduleMaxId = function(schedule) {
    var maxId = 0;
    for (var i = 0; i < schedule.length; i++) {
        if(schedule[i].id > maxId) {
            maxId = schedule[i].id;
        }
    }
    return maxId;
}

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
    $scope.scheduleAction = function () {
        newAction = {
            "action": $('#new-action-action').val(),
            "date": $('#new-action-date').val() + ' ' + $('#new-action-time').val() ,
            "id": getScheduleMaxId($scope.schedule) + 1,
        }
        console.log($scope.schedule[0]);
        console.log(newAction);
        $scope.schedule.push(newAction);
        console.log($scope.schedule);
        // TODO and post to server
        $('#addToScheduleModal').modal('hide');
    }
    // at the bottom of your controller
    var init = function () {
       // check if there is query in url
       // and fire search in case its value is not empty
       $scope.loadSchedule();
    };
    // and fire it after definition
    init();
});