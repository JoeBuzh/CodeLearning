var Student = /** @class */ (function () {
    function Student(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.fullName = firstName + "." + lastName;
    }
    return Student;
}());
function greeter(person) {
    return "hello, " + person.firstName + " " + person.lastName;
}
var user = { firstName: "Jane", LastName: 'AAA' };
var user1 = new Student("Bu", "Zehao");
// document.body.innerHTML = greeter(user);
document.body.innerHTML = greeter(user1);
