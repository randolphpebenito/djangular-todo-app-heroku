(function(){
    angular
        .module('todoApp')
        .controller("todoListCtrl", TodoListController); /* Defining a named function instead of anonymous function */

        function TodoListController() {
            var vm = this;
			console.log('whats going on');
            vm.list = 'hello there!';
        }
})();
