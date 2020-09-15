class Student {
    fullName: string;
    constructor(public firstName: string, public lastName: string){
        this.fullName = firstName + "." + lastName;
    }
}

interface Person {
    firstName: string;
    lastName: String;
}

function greeter(person: Person) {
    return "hello, " + person.firstName + " " + person.lastName;
}

let user = { firstName: "Jane", LastName: 'AAA'};

let user1 = new Student("Bu", "Zehao");

// document.body.innerHTML = greeter(user);
document.body.innerHTML = greeter(user1);