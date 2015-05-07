
var taskBuilder;

$(document).ready(function(){
    taskBuilder = function(){
        var clientsSelect = $('#task-add-form-client');
        var projectsSelect = $('#task-add-form-project');
        var titleInput = $('#task-add-form-title');
        var dueInput = $('#task-add-form-due');
        var submit = $('#task-add-form-submit');
        var targetElem = $('#async-new-task-placeholder');
        var form =  document.getElementById('async-new-task-form');

        targetElem.css('display', 'none');

        var populateClients = function(){
            var url = '/organizer/async/clients/get'
            jQuery.ajax(url, {
                'success':function(data, textStatus, jqXHR){
                    var clients = data.payload;
                    for(var clientName in clients){
                        var option = document.createElement('option');
                        option.value = clients[clientName];
                        option.innerText = clientName;
                        clientsSelect.append(option);
                        $(clientsSelect).trigger('change');
                    }
                }
            });
        };

        var clientChange = function(){
            var clientId = clientsSelect.val();
            var url = '/organizer/async/projects/get/' + clientId;
            jQuery.ajax(url, {
                'success':function(data, textStatus, jqXHR){
                    var projects = data.payload;
                    projectsSelect.find('option').remove();
                    for(var projectName in projects){
                        var option = document.createElement('option');
                        option.value = projects[projectName];
                        option.innerText = projectName;
                        projectsSelect.append(option);
                        $(projectsSelect).trigger('change');
                    }
                }
            });
        };

        var submitTask = function(){
            var rawData = $(form).serializeArray();
            var formData = {};
            for(var elemi in rawData){
                var elem = rawData[elemi];
                formData[elem.name] = elem.value;
            }
            var url = '/organizer/async/tasks/put';

            jQuery.ajax(url, {
                'data':formData,
                'method':'post',
                'success':function(data, textStatus, jqXHR){
                    location.reload();
                }
            });

            return false;
        };

        var showForm = function(){
            targetElem.show(400);
        };

        var hideForm = function(){
            targetElem.hide(400);
        };

        var setDueSoon = function(futureDays){
            if(futureDays == undefined){
                futureDays = 0;
            }
            var theDate = new Date();
            theDate.setDate(theDate.getDate() + futureDays);

            var day = ("0" + theDate.getDate()).slice(-2);
            var month = ("0" + (theDate.getMonth() + 1)).slice(-2);
            var today = theDate.getFullYear()+"-"+(month)+"-"+(day) ;

            dueInput.val(today);
        }

//        submit.on('click', submitTask);
        clientsSelect.on('change', clientChange);
        populateClients();
        return {
            'hideForm':hideForm,
            'showForm':showForm,
            'clientChange':clientChange,
            'submitTask':submitTask,
            'setDueSoon':setDueSoon,
        };
    }();
})
