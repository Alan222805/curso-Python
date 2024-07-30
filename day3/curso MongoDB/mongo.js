[
    {
        "username": "user1",
        "email" : "user1@gmail.com",
        "age": 23,
        "status" : "inactive"
    },    
    {
        "username": "user2",
        "email" : "user2@gmail.com",
        "age": 24,
        "status" : "inactive"
    },
    {
        "username": "user3",
        "email" : "user3@gmail.com",
        "age": 25,
        "status" : "inactive"
    },
    {
        "username": "user4",
        "email" : "user4@gmail.com",
        "age": 26,
        "status" : "inactive"
    },
    {
        "username": "user5",
        "email" : "user5@gmail.com",
        "age": 27,
        "status" : "inactive"
    },
    {
        "username": "user6",
        "email" : "user6@gmail.com",
        "age": 28,
        "status" : "inactive"
    },    
    {
        "username": "user7",
        "email" : "user7@gmail.com",
        "age": 29,
        "status" : "inactive"
    },
    {
        "username": "user8",
        "email" : "user8@gmail.com",
        "age": 30,
        "status" : "inactive"
    },
    {
        "username": "user9",
        "email" : "user9@gmail.com",
        "age": 31,
        "status" : "inactive"
    }     
]

//Seleccionar el usuario con username user7
db.users.findOne({username: "user7"})

//Obtener todos los usuarios con una age mayor a 10
db.users.find({
    age : { $gt : 10 }
})

//Obtener la cantidad de usuarios con una age menor a 50

db.users.find({
    age : {$lt : 10}
}).count()

//Obtener todos los usuarios con una age mayor a 10 y cuyo estatus sea activo
db.users.find({
    $and : [
        {age : {$gt : 10}},
        {status : "active"}
    ]
}) 

//Obtener todos los usuarios cuya age no sea 11
db.users.find({
    age : {$ne : 11}
})

//Obtener todos los usuarios que tengan por age : 27 0 40 0 11

db.users.find({
    $or: [
        {age : 27},
        {age: 40},
        {age: 11}
    ]
})

//Obtener todos los usuarios con atributo status
db.users.find({
    status : {$exists : 1} // 1 or true is equal
})

//Obtener todos los usuarios con status activo
db.users.find({
    $and : [
        {status : {$exists : true}},
        {status : "active"}
    ]
})


//Obtener todos los usuarios con status activo y correo electronico

db.users.find({
    $and : [
        {status : {$exists : true}},
        {status : "active"},
        {email : {$exists : true}}
    ]
})


//Obtener el usuario con mayor edad

db.users.find().sort({
    age : -1 // descendente => -1 ||| ascendente => 1
}).limit(1)


// Obtener a los tres usuarios más jovenes

db.users.find().sort(age).limit(3)


//Obtener los usuarios cuyo email termine con ".com"

db.users.find({
    email : /.com$/
})

//obtener los usuarios cuyos email inician con "user1"

db.users.find({
    email : /^user/
})

//Obtener los usuarios que contienen un 'outlook' en todo el email

db.users.find({
    email : /outlook/
})